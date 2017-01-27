class Comment(object):
    def __init__(self, type, content):
        self.content = content
        self.type = type

    def __str__(self):
        return "[{}]{}".format(self.type, self.content)
