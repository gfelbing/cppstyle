from .node import Node


class Scope(Node):
    def __init__(self, file, position, access, name, children):
        super(Scope, self).__init__(file, position, access, children)
