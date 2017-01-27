class Node(object):
    def __init__(self, file, position, access, comments, children):
        self.file = file
        self.position = position
        self.access = access
        self.comments = comments
        self.children = children

    def __str__(self):
        return "{}({},{},{},{})".format(
            type(self).__name__,
            self.file,
            self.position,
            self.access,
            self.children
        )
