from board import validate, Square
import pdb

class Piece(object):
    def __init__(self, game_board, start, isWhite):
        self.loc = start
        self.white = isWhite
        self.other = not isWhite
        self.board = game_board
        self.available = []

    def move(self, newloc):
        self.board.move(self.loc, newloc)
        self.available = self.get_squares()
        self.loc = newloc

class Pawn(Piece):
    def get_squares(self):
        squares = []

        direction = 1 if self.white else -1
        forward = Square(self.loc.rank + direction, self.loc.file)
        capture = [Square(self.loc.rank + direction, self.loc.file + 1),
                Square(self.loc.rank + direction, self.loc.file - 1)]
        capture = validate(capture)

        if not self.board.exists_piece(forward):
            squares.append(forward)

        for c in capture:
            if self.board.exists_piece(c, color=self.other):
                squares.append(c)

        if (self.white and self.loc.rank == 1) or \
            (not self.white and self.loc.rank == 6):
                pdb.set_trace()
                double_forward = Square(self.loc.rank + 2 * direction,
                        self.loc.file)
                if not self.board.exists_piece(double_forward):
                    squares.append(double_forward)
        return validate(squares)

    def __repr__(self):
        if self.white:
            return chr(0x2659)
        else:
            return chr(0x265f)

class Knight(Piece):
    def get_squares(self):
        reach = [-2, -1, 1, 2]
        displacement = [(i, j) for i in reach for j in reach 
                if abs(i) + abs(j) == 3]
        squares = [Square(self.loc.rank + i, self.loc.file + j) 
                for i, j in displacement]
        return validate(squares)

    def __repr__(self):
        if self.white:
            return chr(0x2658)
        else:
            return chr(0x265e)

class Bishop(Piece):
    def get_squares(self):
        flags = [True] * 4
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        squares = []

        for i in range(1, 8):
            for j in range(len(flags)):
                flag, direction = flags[j], directions[j]
                right, up = direction
                if flag:
                    next_square = Square(self.loc.rank + i*up, 
                                         self.loc.file + i*right)

                    if self.board.exists_piece(next_square, color=self.white):
                        flags[j] = False
                    elif self.board.exists_piece(next_square, color=self.other):
                        squares.append(next_square)
                        flags[j] = False
                    else:
                        squares.append(next_square)

        return validate(squares)

    def __repr__(self):
        if self.white:
            return chr(0x2657)
        else:
            return chr(0x265d)

class Rook(Piece):
    def get_squares(self):
        flags = [True] * 4
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        squares = []

        for i in range(1, 8):
            for j in range(len(flags)):
                flag, direction = flags[j], directions[j]
                right, up = direction
                if flag:
                    next_square = Square(self.loc.rank + i*up, 
                                         self.loc.file + i*right)

                    #pdb.set_trace()
                    if self.board.exists_piece(next_square, color=self.white):
                        flags[j] = False
                    elif self.board.exists_piece(next_square, color=self.other):
                        squares.append(next_square)
                        flags[j] = False
                    else:
                        squares.append(next_square)

        return validate(squares)
    
    def __repr__(self):
        if self.white:
            return chr(0x2656)
        else:
            return chr(0x265c)

class Queen(Piece):
    def get_squares(self):
        flags = [True] * 8
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), 
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]
        squares = []

        for i in range(1, 8):
            for j in range(len(flags)):
                flag, direction = flags[j], directions[j]
                right, up = direction
                if flag:
                    next_square = Square(self.loc.rank + i*up, 
                                         self.loc.file + i*right)
                    if self.board.exists_piece(next_square, color=self.white):
                        flags[j] = False
                    elif self.board.exists_piece(next_square, color=self.other):
                        squares.append(next_square)
                        flags[j] = False
                    else:
                        squares.append(next_square)
        return validate(squares)

    def __repr__(self):
        if self.white:
            return chr(0x2655)
        else:
            return chr(0x265b)

class King(Piece):
    def get_squares(self):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), 
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]
        squares = []
        for i,j in directions:
            next_square = Square(self.loc.rank + i, self.loc.file + j)
            if not self.board.exists_piece(next_square, self.white):
                squares.append(next_square)
        return validate(squares)
    
    def __repr__(self):
        if self.white:
            return chr(0x2654)
        else:
            return chr(0x265a)
