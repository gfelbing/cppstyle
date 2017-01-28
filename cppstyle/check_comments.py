import re

from cppstyle import utils
from cppstyle.model import Issue, Parameter


def check(node, config):
    issues = []

    node_type = utils.camel_case_2_snake_case(node.__class__.__name__)
    comment_config = utils.safe_get(config, ["comments", node_type])

    if comment_config and not isinstance(node, Parameter):
        required = comment_config.keys()
        existing = node.comments

        missing = filter(lambda c: c not in [c.type for c in existing], required)
        issues += map(lambda t: Issue(node.position, "Missing a {} comment.".format(t)), missing)

        to_check = filter(lambda c: c.type in required, existing)
        bad_comments = filter(lambda c: not re.match(comment_config[c.type], c.content), to_check)
        issues += map(
            lambda c: Issue(
                node.position,
                "Comment '{}' does not match '{}'".format(c.content, comment_config[c.type])
            ),
            bad_comments
        )

    parameter_comment_config = utils.safe_get(config, ["comments", "parameter"])
    if parameter_comment_config:
        parameters = list(filter(lambda c: isinstance(c, Parameter), node.children))
        comments = list(filter(lambda c: c.type == "@param", node.comments))

        missing = list(filter(
            lambda p: not utils.findAny(
                lambda c: re.match('^{} '.format(p.name), c.content), comments),
            parameters
        ))
        issues += map(lambda p: Issue(p.position, "Parameter '{}' is missing a comment.".format(p.name)), missing)

        bad_comments = filter(lambda c: not re.match(parameter_comment_config, c.content), comments)
        issues += map(
            lambda p: Issue(
                node.position,
                "Parameter comment '{}' does not match '{}'".format(p.content, parameter_comment_config)
            ),
            bad_comments
        )

    return issues
