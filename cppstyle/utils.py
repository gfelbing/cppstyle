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


def printNode(node,indent):
    out = "{} {}: {}".format((" "*indent),str(node.kind),node.spelling)
    print(out)

    for c in node.get_children():
        printNode(c,indent+2)