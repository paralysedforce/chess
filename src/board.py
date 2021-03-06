from square import *
import pieces
import pdb

BOARDSIZE = 8

class Board(object):
    def __init__(self):
        self.squares = self._populate_board()

    def __repr__(self):
        board_string = "\033[4m" + "    " * 8 + "\n"
        filemap = "ABCDEFGH"
        for rank in range(7, -1, -1):
            for file in range(8):
                sq = Square(rank, file)
                if self.exists_piece(sq):
                    board_string += "| %s " % self.squares[sq].__repr__()
                else:
                    board_string += "|   "
            board_string += "|\033[0m  " + str(rank + 1) + "\033[4m\n"

        board_string += "\033[0m" 
        for i in range(8):
            board_string += "  %s " % filemap[i]
        return board_string

    def _populate_board(self):
        squares = {Square(i, j): None for i in range(BOARDSIZE) 
                                      for j in range(BOARDSIZE)}

        order = (pieces.Rook, pieces.Knight, pieces.Bishop, pieces.Queen,
                pieces.King, pieces.Bishop, pieces.Knight, pieces.Rook)

        for j in range(8):
            white_heavy = Square(0, j)
            squares[white_heavy] = order[j](self, white_heavy, True)

            white_pawn = Square(1, j)
            squares[white_pawn] = pieces.Pawn(self, white_pawn, True)

            black_pawn = Square(6, j)
            squares[black_pawn] = pieces.Pawn(self, black_pawn, False)
            
            black_heavy = Square(7, j)
            squares[black_heavy] = order[j](self, black_heavy, False)

        return squares

    def move(self, loc, other, special=None):
        if special is None:
            special = []
        p = self.squares[loc]
        possible_destinations = p.get_squares() + special
        if not p:
            raise ValueError("No piece found on square")
        else:
            if other in possible_destinations:
                self.squares[loc] = None
                self.squares[other] = p
                p.loc = other
            else:
                print(p.get_squares())

    def exists_piece(self, sq, color=None):
        if validate([sq]):
            piece = self.squares[sq]
            if piece:
                if color is not None:
                    return piece.white == color
                else:
                    return True
        return False

