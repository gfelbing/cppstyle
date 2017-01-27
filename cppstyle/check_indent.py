from cppstyle.model.access_specifier import AccessSpecifier
from cppstyle.model.class_node import Class
from cppstyle.model.function import Function
from cppstyle.model.issue import Issue
from cppstyle.model.method import Method
from cppstyle.model.scope import Scope
from cppstyle.model.struct import Struct
from cppstyle.utils import safe_get


def to_issue(node, indent_rule):
    return Issue(
        node.position,
        "Indent is wrong, should be '{}', not '{}'".format(indent_rule, node.position.col)
    )


def check(node, config):
    issues = []
    if isinstance(node, Function):
        indent_config = safe_get(config, ["indent", "function"])
        if indent_config:
            indent_rule = indent_config + node.position.col
            scopes = filter(lambda x: isinstance(x, Scope), node.children)
            children = [child for scope in scopes for child in scope.children]
            wrong_indented = filter(lambda c: c.position.col != indent_rule, children)
            issues += list(map(lambda c: to_issue(c, indent_rule), wrong_indented))

    if isinstance(node, Method):
        indent_config = safe_get(config, ["indent", "method"])
        if indent_config:
            indent_rule = indent_config + node.position.col
            scopes = filter(lambda x: isinstance(x, Scope), node.children)
            children = [child for scope in scopes for child in scope.children]
            wrong_indented = filter(lambda c: c.position.col != indent_rule, children)
            issues += list(map(lambda c: to_issue(c, indent_rule), wrong_indented))

    if isinstance(node, Struct):
        indent_config = safe_get(config, ["indent", "struct"])
        if indent_config:
            indent_rule = indent_config + node.position.col
            children = [child for child in node.children]
            wrong_indented = filter(lambda c: c.position.col != indent_rule, children)
            issues += list(map(lambda c: to_issue(c, indent_rule), wrong_indented))

    if isinstance(node, Class):
        indent_config = safe_get(config, ["indent", "class"])
        if indent_config:
            children = [child for child in node.children]

            if "access_specifier" in indent_config.keys():
                modifier = filter(lambda x: isinstance(x, AccessSpecifier), children)
                children = filter(lambda x: not isinstance(x, AccessSpecifier), children)
                indent_modifier_rule = indent_config["access_specifier"] + node.position.col
                wrong_indented = filter(lambda c: c.position.col != indent_modifier_rule, modifier)
                issues += list(map(lambda c: to_issue(c, indent_modifier_rule), wrong_indented))

            if "default" in indent_config.keys():
                indent_rule = indent_config["default"] + node.position.col
                wrong_indented = filter(lambda c: c.position.col != indent_rule, children)
                issues += list(map(lambda c: to_issue(c, indent_rule), wrong_indented))

    return issues
