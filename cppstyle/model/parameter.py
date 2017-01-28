from cppstyle.model import Node


class Parameter(Node):
    def __init__(self, file, position, access, comments, name, children):
        super(Parameter, self).__init__(file, position, access, comments, children)
        self.name = name
