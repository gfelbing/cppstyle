from .node import Node


class Field(Node):
    def __init__(self, file, position, access, name, children):
        super(Field, self).__init__(file, position, access, children)
        self.name = name