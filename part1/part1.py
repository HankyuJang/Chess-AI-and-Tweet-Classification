#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 08 10:14:39 2017
@author: PulkitMaloo
"""
import sys

class Parakeet(object):
    def __init__(self,x=None,y=None,p=None):
        self.position_x = x
        self.position_y = y
        self.player = "w" if p.isupper() else "b"
    def __str__(self): return "P" if self.player == "w" else "p"

class Robin(object):
    def __init__(self,x=None,y=None,p=None):
        self.position_x = x
        self.position_y = y
        self.player = "w" if p.isupper() else "b"
    def __str__(self): return "R" if self.player == "w" else "r"

class Bluejay(object):
    def __init__(self,x=None,y=None,p=None):
        self.position_x = x
        self.position_y = y
        self.player = "w" if p.isupper() else "b"
    def __str__(self): return "B" if self.player == "w" else "b"

class Quetzal(object):
    def __init__(self,x=None,y=None,p=None):
        self.position_x = x
        self.position_y = y
        self.player = "w" if p.isupper() else "b"
    def __str__(self): return "Q" if self.player == "w" else "q"

class Nighthawk(object):
    def __init__(self,x=None,y=None,p=None):
        self.position_x = x
        self.position_y = y
        self.player = "w" if p.isupper() else "b"
    def __str__(self): return "N" if self.player == "w" else "n"

class Kingfisher(object):
    def __init__(self,x=None,y=None,p=None):
        self.position_x = x
        self.position_y = y
        self.player = "w" if p.isupper() else "b"
    def __str__(self): return "K" if self.player == "w" else "k"

class Board(object):
    def __init__(self, board):
        self.board = self.create_board(board)
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
    def succ(self): pass
#        for piece in self.board:
#            if piece:


class Player(object):
    def __init__(self):
        self.name = None

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
