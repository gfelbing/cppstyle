def args():
    import argparse as arg
    parser = arg.ArgumentParser(description="Check the style of your C/C++ code.")
    parser.add_argument("--config", default=".cppstyle")
    parser.add_argument("-i", dest="files", default=[], action="append")
    return parser.parse_args()


def config(file):
    import yaml as y
    with open(file) as file:
        return y.safe_load(file)


def printNode(node, indent):
    out = "{} {}: {}".format((" " * indent), str(node.kind), node.spelling)
    print(out)

    for c in node.get_children():
        printNode(c, indent + 2)


def safe_get(dict, keys):
    result = dict
    for key in keys:
        result = result.get(key, {})
    return result


def split(list, split_predicate, append_predicate=lambda x: True):
    result = []
    current = []
    for e in list:
        if split_predicate(e):
            if len(current) > 0:
                result.append(current)
            if append_predicate(e):
                current = [e]
            else:
                current = []
        else:
            if append_predicate(e):
                current.append(e)
    if len(current) > 0:
        result.append(current)
    return result


def findAny(predicate, list):
    for e in list:
        if predicate(e):
            return e
    return None


def camel_case_2_snake_case(name):
    import re
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
