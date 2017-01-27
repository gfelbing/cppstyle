from .node import Node


class Struct(Node):
    def __init__(self, file, position, access, comments, name, children):
        super(Struct, self).__init__(file, position, access, comments, children)
        self.name = name
