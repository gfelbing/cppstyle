from cppstyle.model.access_specifier import AccessSpecifier
from cppstyle.model.class_node import Class
from cppstyle.model.issue import *
from .utils import safe_get


def check(file, node, config):
    errors = []
    if file == node.file and isinstance(node, Class):
        if safe_get(config, ["order", "access_specifier_required"]) == True:
            if len(node.children) > 0 and not isinstance(node.children[0], AccessSpecifier):
                errors.append(Issue(
                    node.position,
                    "Class '{}' should have an access specifier at first.".format(node.name)
                ))

        specifier_order = safe_get(config, ["order", "access_specifier"])
        if specifier_order:
            specifiers = list(map(
                lambda c: c.access.value,
                filter(
                    lambda c: isinstance(c, AccessSpecifier),
                    node.children
                )
            ))
            specifier_order = list(filter(
                lambda e: e in specifiers,
                specifier_order
            ))
            if specifiers != specifier_order:
                errors.append(Issue(
                    node.position,
                    "Class '{}' has wrong access specifier order: {}, should be {}".format(
                        node.name,
                        specifiers,
                        specifier_order
                    )
                ))

    for c in node.children:
        errors += check(file, c, config)

    return errors
