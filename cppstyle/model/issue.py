from .position import *

class Issue(object):
    def __init__(self, position, message):
        self.position = position
        self.message = message

    def __str__(self):
        return "{pos}: {msg}".format(pos = self.position, msg = self.message)