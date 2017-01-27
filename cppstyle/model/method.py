from .node import Node


class Method(Node):
    def __init__(self, file, position, access, comments, name, children):
        super(Method, self).__init__(file, position, access, comments, children)
        self.name = name
