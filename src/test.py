import pieces
import board

def parse_square(string):
    filemap = "ABCDEFGH"
    rank = int(string[1]) - 1
    file = filemap.index(string[0])
    return board.Square(rank, file)

def test():
    b = board.Board()
    print(b)
    with open("../tests/game1") as f:
        for line in f.readlines():
            sq1, sq2= line.split()
            from_sq = parse_square(sq1)
            to_sq = parse_square(sq2)
            b.move(from_sq, to_sq)
            print(b)

if __name__ == "__main__":
    test()
