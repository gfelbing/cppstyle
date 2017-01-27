from .node import Node


class Class(Node):
    def __init__(self, file, position, access, comments, name, children):
        super(Class, self).__init__(file, position, access, comments, children)
        self.name = name
