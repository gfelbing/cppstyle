from .node import Node


class Function(Node):
    def __init__(self, file, position, access, name, children):
        super(Function, self).__init__(file, position, access, children)
        self.name = name