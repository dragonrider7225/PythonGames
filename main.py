#!py -3
from solitaire import *
import sys

def main():
    opt = int(input("Which game would you like to play?\n\t0: Quit program\n" +
            "\t1: Klondike\n"))
    if not opt:
        sys.exit(0)
    if opt == 1:
        game = klondike
        args = []
    game.set_up(*args)
    game.show_board()
    while True:
        if game.get_result() == game.VICTORY:
            print("YOU WIN!")
            return
        if game.get_result() == game.LOSE:
            print("YOU LOSE!")
            return
        m = input("Move: ").split()
        if game == klondike:
            if m[0][0] == "s":
                game.draw()
                game.show_board()
            elif m[0][0] == "m":
                if m[1][0] == "w":
                    if m[2][0] == "f":
                        game.m()
                    elif m[2][0] == "l":
                        game.m(m[1], int(m[2][1:]))
                    else:
                        print_valid_moves(game)
                        continue
                elif m[1][0] == "l":
                    if m[2][0] == "f":
                        game.m(int(m[1][1:]), "f")
                    elif m[2][0] == "l":
                        if len(m) == 3:
                            game.m(int(m[1][1:]), int(m[2][1:]))
                        else:
                            game.m(int(m[1][1:]), int(m[3]), int(m[2][1:]))
                    else:
                        print_valid_moves(game)
                elif m[1][0] == "f":
                    if m[2][0] == "l":
                        game.m("f", int(m[1][1:]), int(m[2][1:]))
                    else:
                        print_valid_moves(game)
                else:
                    print_valid_moves(game)
            else:
                print_valid_moves(game)

def print_valid_moves(game):
    game.show_board()
    print("Please enter a valid move:")
    if game == klondike:
        print("s[tock]")
        print("m[ove] w[aste] f[oundation]")
        print("m[ove] w[aste] lN")
        print("m[ove] lN f[oundation]")
        print("m[ove] lN1 lN2 C")
        print("m[ove] fM lN")
        print("0 <= N* <= 6, 0 <= M <= 3, C is the number of cards", end=" ")
        print("that are below the card to move from one layout", end=" ")
        print("pile to another.")

if __name__ == "__main__":
    main()
