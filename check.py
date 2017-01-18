import sys, errno

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

class Issue(object):
    def __init__(self, row, col, message):
        self.row = row
        self.col = col
        self.message = message

    def __str__(self):
        return "[Line {row}, Col {col}]: {msg}".format(row = self.row, col = self.col, msg = self.message)


def checkNaming(node,config):
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
        regex = config["naming"]["members"]
        name = node.spelling
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
        errors += checkNaming(c,config)

    return errors


def printNode(node,indent):
    out = "{} {}: {}".format((" "*indent),str(node.kind),node.spelling)
    print(out)

    for c in node.get_children():
        printNode(c,indent+2)


def runChecks(file,config):
    import clang.cindex as ci
    index = ci.Index.create()
    source = index.parse(file)
    root = source.cursor
    issues = []
    issues += checkNaming(root, config)
    return issues


args = args()
config = config(args.config)

for file in args.files:
    issues = runChecks(file,config)
    if len(issues) > 0:
        print("Found issues in file '{}':".format(file))
        for issue in issues:
            print("    {}".format(issue))
        sys.exit(errno.EFAULT)