from .node import Node


class Variable(Node):
    def __init__(self, file, position, access, comments, name, children):
        super(Variable, self).__init__(file, position, access, comments, children)
        self.name = name
