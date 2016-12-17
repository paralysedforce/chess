import pdb
from square import Square
import board
import pieces

class Game(object):
    def __init__(self):
        self.board = board.Board()
        self.whites_turn = True
        self.stalemate_count = 0
        self.en_passant = None
        self.white_castling = [True, True]
        self.black_castling = [True, True]

    def change_turns(self):
        self.whites_turn = not self.whites_turn

    def move(self, from_sq, to_sq):
        piece = self.board.squares[from_sq]

        try:
            if self.board.exists_piece(from_sq, not self.whites_turn):
                raise ValueError

            if isinstance(piece, pieces.Pawn):
                white_ep = piece.white and from_sq.rank == 1 and to_sq.rank == 3
                black_ep = not piece.white and from_sq.rank == 6 and to_sq.rank == 4
                direction = 1 if piece.white else -1

                # Promotion
                if (piece.white and to_sq.rank == 7) or \
                   (not piece.white and to_sq.rank == 0):

                    self.board.move(from_sq, to_sq, special=self.en_passant)
                    queen = pieces.Queen(self.board, piece.loc, piece.white)
                    self.board.squares[to_sq] = queen
                    self.en_passant = None
                    self.change_turns()
                    self.stalemate_count = 0
                    return

                # Track En Passant
                elif white_ep or black_ep:
                    self.board.move(from_sq, to_sq)
                    self.en_passant = pieces.Square(to_sq.rank - direction,
                            to_sq.file)
                    self.change_turns()
                    self.stalemate_count = 0
                    return

                elif self.en_passant and to_sq == self.en_passant:
                    self.board.move(from_sq, to_sq, special=[self.en_passant])
                    former_ep_square = pieces.Square(to_sq.rank - direction, to_sq.file)
                    self.board.squares[former_ep_square] = None
                    self.en_passant = None
                    self.change_turns()
                    self.stalemate_count = 0
                    return

                else:
                    self.board.move(from_sq, to_sq)
                    self.change_turns()
                    self.en_passant = None
                    self.stalemate_count = 0


#            elif isinstance(piece, pieces.King):
#                pass

            else:
                self.board.move(from_sq, to_sq)
                self.en_passant = None
                self.stalemate_count += 1
                self.change_turns()
            
        except ValueError:
            return

