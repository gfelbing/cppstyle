from cppstyle.model import Access, Class, Field, Function, Issue, Method, Variable
from .utils import safe_get


def check(node, config):
    import re
    errors = []
    if isinstance(node, Class):
        regex = safe_get(config, ["naming", "classes"])
        if regex:
            if re.match(regex, node.name) == None:
                errors.append(Issue(
                    node.position,
                    "Class '{}' does not match '{}'".format(node.name, regex)
                ))
    elif isinstance(node, Variable):
        regex = safe_get(config, ["naming", "variables"])
        if regex:
            if re.match(regex, node.name) == None:
                errors.append(Issue(
                    node.position,
                    "Variable '{}' does not match '{}'".format(node.name, regex)
                ))
    elif isinstance(node, Function):
        regex = safe_get(config, ["naming", "functions"])
        if regex:
            if re.match(regex, node.name) == None:
                errors.append(Issue(
                    node.position,
                    "Function '{}' does not match '{}'".format(node.name, regex)
                ))
    elif isinstance(node, Method):
        regex = safe_get(config, ["naming", "methods"])
        if regex:
            if re.match(regex, node.name) == None:
                errors.append(Issue(
                    node.position,
                    "Method '{}' does not match '{}'".format(node.name, regex)
                ))
    elif isinstance(node, Field):
        name = node.name
        regex = ""
        if node.access == Access.PRIVATE:
            regex = safe_get(config, ["naming", "members", "private"])
        elif node.access == Access.PROTECTED:
            regex = safe_get(config, ["naming", "members", "protected"])
        elif node.access == Access.PUBLIC:
            regex = safe_get(config, ["naming", "members", "public"])

        if regex:
            if re.match(regex, name) == None:
                errors.append(Issue(
                    node.position,
                    "Field '{}' does not match '{}'".format(name, regex)
                ))

    return errors
