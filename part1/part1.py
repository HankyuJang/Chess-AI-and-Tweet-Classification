#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 08 10:14:39 2017
@author: PulkitMaloo
"""
import sys
from copy import deepcopy

class Piece(object):
    def __init__(self, x=None, y=None, p=None):
        self.position_x = x
        self.position_y = y
        self.player = "w" if p.isupper() else "b"
    def __str__(self): return "."

class Parakeet(Piece):
    def __init__(self, x=None, y=None, p=None):
        Piece.__init__(self, x, y, p)
    def __str__(self): return "P" if self.player == "w" else "p"

class Robin(Piece):
    def __init__(self, x=None, y=None, p=None):
        Piece.__init__(self, x, y, p)
    def __str__(self): return "R" if self.player == "w" else "r"

class Bluejay(Piece):
    def __init__(self, x=None, y=None, p=None):
        Piece.__init__(self, x, y, p)
    def __str__(self): return "B" if self.player == "w" else "b"

class Quetzal(Piece):
    def __init__(self, x=None, y=None, p=None):
        Piece.__init__(self, x, y, p)
    def __str__(self): return "Q" if self.player == "w" else "q"

class Nighthawk(Piece):
    def __init__(self, x=None, y=None, p=None):
        Piece.__init__(self, x, y, p)
    def __str__(self): return "N" if self.player == "w" else "n"

class Kingfisher(Piece):
    def __init__(self,x=None,y=None,p=None):
        Piece.__init__(self, x, y, p)
    def __str__(self): return "K" if self.player == "w" else "k"

class Board(object):
    def __init__(self, board):
        self.board = board if isinstance(board, list) else self.create_board(board)
    def __repr__(self):
        return "\n".join([" ".join([str(self.board[i][j]) if self.board[i][j] is not None else "." for j in range(8)]) for i in range(8)])
#    def __str__(self):
#        return "".join(self.__repr__.split())
    def create_board(self, init_board):
        pieces_dict = {"P":"Parakeet", "Q":"Quetzal", "B":"Bluejay", "N":"Nighthawk", "R":"Robin", "K":"Kingfisher", "p":"Parakeet", "q":"Quetzal", "b":"Bluejay", "n":"Nighthawk", "r":"Robin", "k":"Kingfisher"}
        board = [[None]*8 for i in range(8)]
        for i, piece in enumerate(init_board):
            x, y = i/8, i%8
            board[x][y] = None if piece == "." else eval(pieces_dict[piece]+"("+str(x)+","+str(y)+","+"'"+str(piece)+"'"+")")
        return board

def succ(board, player="w"):
    succ = []
    for row in board:
        for piece in row:
            if piece and piece.player == player:
                succ.append(move_piece(board, piece))
    return succ

def move_piece(board, piece): pass
    # We can easily check the type of piece and its position here
    # and move it in the board accordingly

def move_quetzel(board, piece):
    pass

def move_parakeet(board, piece):
    pass

def move_nighthawk(board, piece):
    pass

def move_robin(board, piece):
    pass

def move_bluejay(board, piece):
    pass

def move_down(board, piece):
    x = piece.position_x
    y = piece.position_y
    if board[x+1][y] is None:
        board[x][y], board[x+1][y] = board[x+1][y], board[x][y]
        piece.position_x += 1
    elif board[x+1][y].player != piece.player:
        board[x][y] = None
        board[x+1][y] = piece
        piece.position_x += 1
    else:
        pass
    return board

def move_up(board, piece):
    x = piece.position_x
    y = piece.position_y
    if board[x-1][y] is None:
        board[x][y], board[x-1][y] = board[x-1][y], board[x][y]
        piece.position_x -= 1
    elif board[x-1][y].player != piece.player:
        board[x][y] = None
        board[x-1][y] = piece
        piece.position_x -= 1
    else:
        pass
    return board

def move_right(board, piece):
    x = piece.position_x
    y = piece.position_y
    if board[x][y+1] is None:
        board[x][y], board[x][y+1] = board[x][y+1], board[x][y]
        piece.position_y += 1
    elif board[x][y+1].player != piece.player:
        board[x][y] = None
        board[x][y+1] = piece
        piece.position_y += 1
    else:
        pass
    return board

def move_left(board, piece):
    x = piece.position_x
    y = piece.position_y
    if board[x][y-1] is None:
        board[x][y], board[x][y-1] = board[x][y-1], board[x][y]
        piece.position_y -= 1
    elif board[x][y-1].player != piece.player:
        board[x][y] = None
        board[x][y-1] = piece
        piece.position_y -= 1
    else:
        pass
    return board

def move_up_right(board, piece):
    x = piece.position_x
    y = piece.position_y
    if board[x-1][y+1] is None:
        board[x][y], board[x-1][y+1] = board[x-1][y+1], board[x][y]
        piece.position_x -= 1
        piece.position_y += 1
    elif board[x-1][y+1].player != piece.player:
        board[x][y] = None
        board[x-1][y+1] = piece
        piece.position_x -= 1
        piece.position_y += 1
    else:
        pass
    return board

def move_up_left(board, piece):
    x = piece.position_x
    y = piece.position_y
    if board[x-1][y-1] is None:
        board[x][y], board[x-1][y-1] = board[x-1][y-1], board[x][y]
        piece.position_x -= 1
        piece.position_y -= 1
    elif board[x-1][y-1].player != piece.player:
        board[x][y] = None
        board[x-1][y-1] = piece
        piece.position_x -= 1
        piece.position_y -= 1
    else:
        pass
    return board

def move_down_right(board, piece):
    x = piece.position_x
    y = piece.position_y
    if board[x+1][y+1] is None:
        board[x][y], board[x+1][y+1] = board[x+1][y+1], board[x][y]
        piece.position_x += 1
        piece.position_y += 1
    elif board[x+1][y+1].player != piece.player:
        board[x][y] = None
        board[x+1][y+1] = piece
        piece.position_x += 1
        piece.position_y += 1
    else:
        pass
    return board

def move_down_left(board, piece):
    x = piece.position_x
    y = piece.position_y
    if board[x+1][y-1] is None:
        board[x][y], board[x+1][y-1] = board[x+1][y-1], board[x][y]
        piece.position_x += 1
        piece.position_y -= 1
    elif board[x+1][y-1].player != piece.player:
        board[x][y] = None
        board[x+1][y-1] = piece
        piece.position_x += 1
        piece.position_y -= 1
    else:
        pass
    return board

class Player(object):
    def __init__(self):
        self.name = None
        self.turn = False

class Game(object):
    def __init__(self): pass

if __name__ == "__main__":
    try:
        curr_player = sys.argv[1]
        initial_board = sys.argv[2]
        time = sys.argv[3]
    except:
        curr_player = "w"
        initial_board = "RNBQKBNRPPPPPPPP................................pppppppprnbqkbnr"
        time = 10

    b = Board(initial_board)
    print b
