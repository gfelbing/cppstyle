from .issue import *
from .utils import safe_get

def access_spec_2_string(spec):
    import clang.cindex as ci
    if spec == ci.AccessSpecifier.PUBLIC:
        return "public"
    elif spec == ci.AccessSpecifier.PROTECTED:
        return "protected"
    elif spec == ci.AccessSpecifier.PRIVATE:
        return "private"

def check(node, config):
    import clang.cindex as ci
    import re
    errors = []
    if node.kind == ci.CursorKind.CLASS_DECL:
        if safe_get(config, ["order", "access_specifier_required"]) == True:
            if list(node.get_children())[0].kind != ci.CursorKind.CXX_ACCESS_SPEC_DECL:
                errors.append(Issue(
                    node.location.line, node.location.column,
                    "Class '{}' should have an access specifier at first.".format(node.spelling)
                ))

        specifier_order = safe_get(config, ["order", "access_specifier"])
        if specifier_order:
            specifiers = list(map(
                lambda c: access_spec_2_string(c.access_specifier),
                filter(lambda c: c.kind == ci.CursorKind.CXX_ACCESS_SPEC_DECL, list(node.get_children()))
            ))
            specifier_order = list(filter(
                lambda e: e in specifiers,
                specifier_order
            ))
            if specifiers != specifier_order:
                errors.append(Issue(
                    node.location.line, node.location.column,
                    "Class '{}' has wrong access specifier order: {}, should be {}".format(
                        node.spelling,
                        specifiers,
                        specifier_order
                    )
                ))





    for c in node.get_children():
        errors += check(c, config)

    return errors
