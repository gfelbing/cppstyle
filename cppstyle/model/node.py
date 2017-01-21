from .position import Position


class Node:
    def __init__(self, file, position, access, children):
        self.file = file
        self.position = position
        self.access = access
        self.children = children

    def __str__(self):
        return "{}({},{},{},{})".format(
            type(self).__name__,
            self.file,
            self.position,
            self.access,
            self.children
        )
