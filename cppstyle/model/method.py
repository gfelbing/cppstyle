from .node import Node


class Method(Node):
    def __init__(self, file, position, access, name, children):
        super(Method, self).__init__(file, position, access, children)
        self.name = name