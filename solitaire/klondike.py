"""This module contains several methods, the most important of which
is set_up_klondike, which will set up a game of Klondike to be played
via the remaining methods.
"""

import cards.cards as c

__all__ = ["set_up_klondike", "get_waste", "draw", "move", "show_board"]

def set_up_klondike():
"""This method initializes the board state.
"""
    global layout, foundations, stock, waste
    layout = [[[], []], [[], []], [[], []], [[], []], [[], []],
                [[], [] ], [[], []]]
    foundations = [0, 0, 0, 0]
    stock = c.create_playing_card_deck()
    stock.shuffle()
    for i in range(7):
        layout[i][1] = [stock.draw_card()]
        for j in range(i + 1, 7):
            layout[j][0].append(stock.draw_card())
    waste = []

def get_layout():
    return layout

def get_waste():
    return waste

def draw():
    global stock, waste
    if len(stock) < 1:
        stock = c.Deck(waste)
        waste = []
    for i in range(3):
        if (len(stock) > 0):
            waste.append(stock.draw_card())

def can_move(card, target):
    if target is None:
        return card.rank is 13
    if target.get_color() is None or target.get_color() is card.get_color():
        return False
    return card.rank == target.rank - 1

def m(*args):
"""
"""
    if len(args) == 0:
        move_waste_to_foundation()
        show_board()
        return
    if len(args) == 2:
        if args[0] == 'w':
            move_from_waste(args[1])
            show_board()
            return
        if args[1] == 'f':
            move_to_foundation(args[0])
            show_board()
            return
        move([args[0], 0], args[1])
        show_board()
        return
    if len(args) == 3:
        move([args[0], args[1]], args[2])
        show_board()
        return
    show_board()
    return

"""old_location should have at index 0 an int indicating which column of the
layout the card to move is in and at index 1 an int indicating how far from the
bottom of the stack of face up cards that card is. location should be an int
indicating the column to which old_location should be moved.
Returns False if the indicated card could not be moved to the specified column.
Otherwise returns True.
"""
def move(old_location, location):
    build = layout[old_location[0]][1]
    for i in range(len(build) - 1, old_location[1], -1):
        if not can_move(build[i], build[i - 1]):
            return False
    if len(layout[location][1]) >= 1:
        if not can_move(build[old_location[1]], layout[location][1][-1]):
            return False
    elif not build[old_location[1]].rank is 13:
        return False
    for i in range(old_location[1], len(build)):
        layout[location][1].append(build[i])
    if old_location[1] == 0 and len(layout[old_location[0]][0]) > 0:
        fd = layout[old_location[0]][0]
        layout[old_location[0]][1] = fd[-1:]
        layout[old_location[0]][0] = fd[:-1]
    else:
        layout[old_location[0]][1] = build[:old_location[1]]
    return True

def move_to_foundation(old_col):
    suit = layout[old_col][1][-1].suit
    rank = layout[old_col][1][-1].get_rank()
    findex = -1
    if suit == "Clubs":
        findex = 0
    elif suit == "Hearts":
        findex = 1
    elif suit == "Spades":
        findex = 2
    elif suit == "Diamonds":
        findex = 3
    if rank == "King":
        if foundations[findex] != 12:
            return False
        foundations[findex] = 13
    elif rank == "Queen":
        if foundations[findex] != 11:
            return False
        foundations[findex] = 12
    elif rank == "Jack":
        if foundations[findex] != 10:
            return False
        foundations[findex] = 11
    elif rank == "Ace":
        if foundations[findex] != 0:
            return False
        foundations[findex] = 1
    else:
        rank = int(rank)
        if foundations[findex] != rank-1:
            return False
        foundations[findex] = rank
    layout[old_col][1] = layout[old_col][1][:-1]
    if len(layout[old_col][1]) <= 0 and len(layout[old_col][0]) > 0:
        layout[old_col][1].append(layout[old_col][0][-1])
        layout[old_col][0] = layout[old_col][0][:-1]
    for f in foundations:
        if not f is 13:
            return True
    print "You Win!"
    return True

def move_waste_to_foundation():
    layout.append([[], [waste[-1]]])
    if move_to_foundation(len(layout) - 1):
        del waste[-1]
        return True
    del layout[-1]
    return False

def move_from_waste(col):
    if len(waste) < 1:
        return False
    if len(layout[col][1]) < 1:
        layout[col][1].append(None)
    if can_move(waste[-1], layout[col][1][-1]):
        layout[col][1].append(waste[-1])
        del waste[-1]
        return True
    del layout[col][1][-1]
    return False

def display_layout():
    print "Facedown cards:",
    print repr(len(layout[0][0])).rjust(8), repr(len(layout[1][0])).rjust(8),
    print repr(len(layout[2][0])).rjust(8), repr(len(layout[3][0])).rjust(8),
    print repr(len(layout[4][0])).rjust(8), repr(len(layout[5][0])).rjust(8),
    print repr(len(layout[6][0])).rjust(8)
    c1 = len(layout[0][1])
    c2 = len(layout[1][1])
    c3 = len(layout[2][1])
    c4 = len(layout[3][1])
    c5 = len(layout[4][1])
    c6 = len(layout[5][1])
    c7 = len(layout[6][1])
    for i in range(max(c1, c2, c3, c4, c5, c6, c7)):
        c1 = get_card([0, i])
        c2 = get_card([1, i])
        c3 = get_card([2, i])
        c4 = get_card([3, i])
        c5 = get_card([4, i])
        c6 = get_card([5, i])
        c7 = get_card([6, i])
        print "".rjust(15),
        print repr(c1).rjust(8), repr(c2).rjust(8), repr(c3).rjust(8),
        print repr(c4).rjust(8), repr(c5).rjust(8), repr(c6).rjust(8),
        print repr(c7).rjust(8)

def show_board():
    print "Stock: ", (repr(len(stock)) + " ").rjust(16),
    waste_str = ""
    if len(waste) >= 3:
        waste_str += repr(waste[-3])[-2:] + " "
    if len(waste) >= 2:
        waste_str += repr(waste[-2])[-2:] + " "
    if len(waste) >= 1:
        waste_str += repr(waste[-1])[-2:]
    print waste_str.rjust(8),
    print "".rjust(8),
    if foundations[0] > 0:
        print repr(c.PlayingCard(foundations[0], "Clubs")).rjust(8),
    else:
        print "".rjust(8),
    if foundations[1] > 0:
        print repr(c.PlayingCard(foundations[1], "Hearts")).rjust(8),
    else:
        print "".rjust(8),
    if foundations[2] > 0:
        print repr(c.PlayingCard(foundations[2], "Spades")).rjust(8),
    else:
        print "".rjust(8),
    if foundations[3] > 0:
        print repr(c.PlayingCard(foundations[3], "Diamonds")).rjust(8),
    else:
        print "".rjust(8),
    print
    display_layout()

def get_card(location):
    if location[0] >= len(layout):
        return ""
    if location[1] >= len(layout[location[0]][1]):
        return "";
    return layout[location[0]][1][location[1]]
