from .node import Node


class Field(Node):
    def __init__(self, file, position, access, comments, name, children):
        super(Field, self).__init__(file, position, access, comments, children)
        self.name = name
