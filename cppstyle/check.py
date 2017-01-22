from cppstyle import check_naming, check_order


def check(file, node, config):
    issues = []
    if file == node.file:
        issues += check_naming.check(node, config)
        issues += check_order.check(node, config)

    for c in node.children:
        issues += check(file, c, config)

    return issues