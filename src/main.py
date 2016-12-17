#!usr/bin/python3

from pieces import Square
import game
import pdb

def main():
    g = game.Game()
    filemap = "abcdefgh"
    while True:
        print(g.board)
        from_input = input("From: ")
        to_input = input("To: ")
        if to_input[-5:] == "debug":
            pdb.set_trace()
        try:
            from_file = filemap.index(from_input[0]) 
            from_rank = int(from_input[1]) - 1
            from_sq = Square(from_rank, from_file)

            to_file = filemap.index(to_input[0])
            to_rank = int(to_input[1]) - 1
            to_sq = Square(to_rank, to_file)

        except ValueError:
            print("Improper input")
            continue
        g.move(from_sq, to_sq)

if __name__ == '__main__':
    main()
