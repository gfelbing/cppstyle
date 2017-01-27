from .node import Node


class Struct(Node):
    def __init__(self, file, position, access, name, children):
        super(Struct, self).__init__(file, position, access, children)
        self.name = name
