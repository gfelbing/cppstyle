from .issue import *

def check_naming(node, config):
    import clang.cindex as ci
    import re
    errors = []
    if node.kind == ci.CursorKind.CLASS_DECL:
        regex = config["naming"]["classes"]
        name = node.spelling
        if re.match(regex, name) == None:
            errors.append(Issue(
                node.location.line, node.location.column,
                "Class '{}' does not match '{}'".format(name, regex)
            ))
    elif node.kind == ci.CursorKind.VAR_DECL:
        regex = config["naming"]["variables"]
        name = node.spelling
        if re.match(regex,name) == None:
            errors.append(Issue(
                node.location.line, node.location.column,
                "Variable '{}' does not match '{}'".format(name, regex)
            ))
    elif node.kind == ci.CursorKind.FIELD_DECL:
        name = node.spelling
        regex = ""
        if node.access_specifier == ci.AccessSpecifier.PRIVATE:
            regex = config["naming"]["members"]["private"]
        elif node.access_specifier == ci.AccessSpecifier.PROTECTED:
            regex = config["naming"]["members"]["protected"]
        elif node.access_specifier == ci.AccessSpecifier.PUBLIC:
            regex = config["naming"]["members"]["public"]

        if re.match(regex, name) == None:
            errors.append(Issue(
                node.location.line, node.location.column,
                "Field '{}' does not match '{}'".format(name, regex)
            ))
    elif node.kind == ci.CursorKind.FUNCTION_DECL:
        regex = config["naming"]["functions"]
        name = node.spelling
        if re.match(regex, name) == None:
            errors.append(Issue(
                node.location.line, node.location.column,
                "Function '{}' does not match '{}'".format(name, regex)
            ))

    for c in node.get_children():
        errors += check_naming(c, config)

    return errors
