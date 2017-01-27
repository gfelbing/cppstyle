from .node import Node


class Function(Node):
    def __init__(self, file, position, access, comments, name, children):
        super(Function, self).__init__(file, position, access, comments, children)
        self.name = name
