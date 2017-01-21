from .node import Node


class Variable(Node):
    def __init__(self, file, position, access, name, children):
        super(Variable, self).__init__(file, position, access, children)
        self.name = name