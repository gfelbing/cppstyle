class Access(object):
    def __init__(self, value):
        self.value = value

Access.PRIVATE = Access("private")
Access.PROTECTED = Access("protected")
Access.PUBLIC = Access("public")
Access.NONE = Access("none")
