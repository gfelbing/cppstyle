from .issue import *
from .utils import safe_get

def check(file, node, config):
    import clang.cindex as ci
    import re
    errors = []
    if file == str(node.location.file):
        if node.kind == ci.CursorKind.CLASS_DECL:
            regex = safe_get(config,["naming","classes"])
            if regex:
                name = node.spelling
                if re.match(regex, name) == None:
                    errors.append(Issue(
                        node.location.line, node.location.column,
                        "Class '{}' does not match '{}'".format(name, regex)
                    ))
        elif node.kind == ci.CursorKind.VAR_DECL:
            regex = safe_get(config,["naming","variables"])
            if regex:
                name = node.spelling
                if re.match(regex,name) == None:
                    errors.append(Issue(
                        node.location.line, node.location.column,
                        "Variable '{}' does not match '{}'".format(name, regex)
                    ))
        elif node.kind == ci.CursorKind.FUNCTION_DECL:
            regex = safe_get(config,["naming","functions"])
            if regex:
                name = node.spelling
                if re.match(regex,name) == None:
                    errors.append(Issue(
                        node.location.line, node.location.column,
                        "Function '{}' does not match '{}'".format(name, regex)
                    ))
        elif node.kind == ci.CursorKind.CXX_METHOD:
            regex = safe_get(config,["naming","methods"])
            if regex:
                name = node.spelling
                if re.match(regex,name) == None:
                    errors.append(Issue(
                        node.location.line, node.location.column,
                        "Method '{}' does not match '{}'".format(name, regex)
                    ))
        elif node.kind == ci.CursorKind.FIELD_DECL:
            name = node.spelling
            regex = ""
            if node.access_specifier == ci.AccessSpecifier.PRIVATE:
                regex = safe_get(config,["naming", "members","private"])
            elif node.access_specifier == ci.AccessSpecifier.PROTECTED:
                regex = safe_get(config,["naming","members","protected"])
            elif node.access_specifier == ci.AccessSpecifier.PUBLIC:
                regex = safe_get(config,["naming","members","public"])

            if regex:
                if re.match(regex, name) == None:
                    errors.append(Issue(
                        node.location.line, node.location.column,
                        "Field '{}' does not match '{}'".format(name, regex)
                    ))

    for c in node.get_children():
        errors += check(file, c, config)

    return errors
