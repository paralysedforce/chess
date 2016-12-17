class Square(object):
    def __init__(self, rank, file):
        self.rank = rank
        self.file = file

    def __eq__(self, other):
        return self.rank == other.rank and self.file == other.file

    def __repr__(self):
        filemap = "ABCDEFGH"
        return filemap[self.file] + str(self.rank+1)

    def __hash__(self):
        return hash((self.rank, self.file))

def validate(squares):
    return [square for square in squares 
            if 0 <= square.rank < 8 and 0 <=square.file < 8]
