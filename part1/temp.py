#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 08 10:14:39 2017

@author: PulkitMaloo
"""

pieces = {"P":"parakeet", "Q":"quetzal", "B":"bluejay", "N":"nighthawk", "R":"robin", "K":"kingﬁsher"}
import sys
class Board(object):
    def __init__(self, board):
        self.board = board
    def __str__(self): return "\n".join([" ".join(self.board[i:i+8]) for i in range(0,64,8)])
    def succ(self, player="w"):
        succ_list = []
        player_check = {"w":"isupper", "b":"islower"}
        for i, piece in enumerate(self.board):
            if eval("piece."+player_check[player]+"()"):
                succ_list.append(eval("move_"+pieces[piece.lower()]+"("+i+")"))
#                print ("move_"+pieces[piece.upper()]+"("+str(i)+")")

    def move_parakeet(self, index, player="w"):
        piece = {"w":"P", "b":"p"}[player]
        succ = []

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