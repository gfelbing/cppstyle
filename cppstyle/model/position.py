class Position:
    def __init__(self,row,col):
        self.row = row
        self.col = col

    def __str__(self):
        return "[Line {}, Col {}]".format(self.row, self.col)