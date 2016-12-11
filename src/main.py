#!usr/bin/python3

import pieces
import board

def main():
    b = board.Board()
    filemap = "ABCDEFGH"
    while True:
        print(b)
        from_input = input("From: ")
        to_input = input("To: ")
        try:
            from_file = filemap.index(from_input[0])
            from_rank = int(from_input[1])
            from_sq = board.Square(from_rank, from_file)

            to_file = filemap.index(to_input[0])
            to_rank = int(to_input[1])
            to_sq = board.Square(to_rank, to_file)

        except ValueError:
            print("Improper input")
            continue
        b.move(from_sq, to_sq)

if __name__ == '__main__':
    main()
