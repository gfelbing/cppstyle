class Issue(object):
    def __init__(self, row, col, message):
        self.row = row
        self.col = col
        self.message = message

    def __str__(self):
        return "[Line {row}, Col {col}]: {msg}".format(row = self.row, col = self.col, msg = self.message)