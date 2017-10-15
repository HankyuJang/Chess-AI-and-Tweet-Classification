import sys

def p(r,c):
    return [(r,c) for r,c in [(r-1,c),(r-1,c-1),(r-1,c+1),(r-2,c)] if in_board(r,c)]
def P(r,c):
    return [(r,c) for r,c in [(r+1,c),(r+1,c-1),(r+1,c+1),(r+2,c)] if in_board(r,c)]
def N(r, c):
    return [(r,c) for r,c in [(r+2,c-1),(r+2,c+1),(r+1,c-2),(r+1,c+2),(r-1,c-2),(r-1,c+2),(r-2,c-1),(r-2,c+1)] if in_board(r,c)]
def B(r, c):
    diff, summ = r-c, r+c
    return [(r,c) for r,c in filter(lambda a: a != (r, c), [(i, i-diff) for i in range(8)] + [(i, summ-i) for i in range(8)]) if in_board(r,c)]
def R(r, c):
    return [(r,c) for r,c in filter(lambda a: a != (r, c), [(r,i) for i in range(8)] + [(i,c) for i in range(8)]) if in_board(r,c)]
def Q(r, c):
    diff, summ = r-c, r+c
    return [(r,c) for r,c in filter(lambda a: a != (r, c), [(r,i) for i in range(8)] + [(i,c) for i in range(8)] + [(i, i-diff) for i in range(8)] + [(i, summ-i) for i in range(8)]) if in_board(r,c)]
def K(r, c):
    return [(r,c) for r,c in [(r+1,c+1),(r+1,c),(r+1,c-1),(r,c-1),(r-1,c-1),(r-1,c),(r-1,c+1),(r,c+1)] if in_board(r,c)]

def in_board(r, c):
    return 0 <= r <= 7 and 0 <= c <= 7

# row_n: next row, col_n: next col, row: current row, col: current col
# current location in string: r*8 + c
# next location in string: r_n*8 + c_n
def next_board(s, piece, r, c, r_n, c_n):
    s_prime = s[:r*8+c] + '.' + s[r*8+c + 1:]
    return s_prime[:r_n*8 + c_n] + piece + s_prime[r_n*8 + c_n+1:]

def loc(s, r, c):
    return s[r*8 + c]

def successor(s, turn):
    board_list = []
    for i, piece in enumerate(s):
        if piece in player[turn]:
            r, c = i/8, i%8
            board_list.extend([next_board(s,piece,r,c,r_n,c_n) for r_n,c_n in possible_move[piece](r, c) if is_valid(s,turn,piece,r,c,r_n,c_n)])
    return board_list

def is_valid(s, turn, piece, r, c, r_n, c_n):
    if turn=='w':
        if piece=='P': # Check the 'P' in advance
            if r_n-r == 1 and c_n==c: # Check one-step move
                if loc(s, r_n, c_n) != '.':
                    return False
            elif r_n-r == 2: # Check the inital two-step move
                if r != 1:
                    return False
                elif loc(s,2,c) != '.':
                    return False
            elif c != c_n: # Check the attack move
                if loc(s,r_n,c_n) not in player['b']:
                    return False
        if loc(s, r_n, c_n) in player['w']:
            return False
    elif turn=='b':
        if piece=='p': # Check the 'P' in advance
            if r-r_n == 1 and c_n==c: # Check one-step move
                if loc(s, r_n, c_n) != '.':
                    return False
            elif r-r_n == 2: # Check the inital two-step move
                if r != 6: # If not in the initial position, you can't make 2 step move
                    return False
                elif loc(s,5,c) != '.':
                    return False
            elif c != c_n: # Check the attack move
                if loc(s,r_n,c_n) not in player['w']:
                    return False
        if loc(s, r_n, c_n) in player['b']:
            return False

    if piece=='R' or piece=='Q' or piece=='r' or piece=='q':
        if r==r_n: # Horizontal move
            for i in range(min(c,c_n)+1, max(c,c_n)):
                if loc(s,r,i) != '.':
                    return False
        elif c==c_n: # Vertical move
            for i in range(min(r,r_n)+1, max(r,r_n)):
                if loc(s,i,c) != '.':
                    return False

    if piece=='B' or piece=='Q' or piece=='b' or piece=='q':
        if r-r_n == c-c_n: # RightDown or LeftUp
            for i in range(1, abs(c-c_n)):
                if loc(s,min(r,r_n)+i,min(c,c_n)+i) != '.':
                    return False
        elif r-r_n == c_n-c: # RightUp, LeftDown
            for i in range(1, abs(c-c_n)):
                if loc(s, max(r,r_n)-i, min(c,c_n)+i) != '.':
                    return False
    return True

#######################################################################################
# These are just functions to print results. I won't need them to run the script.
def print_board(s):
    for i, piece in enumerate(s):
        if i % 8 == 0:
            print
        print piece, 

def print_successors(boards):
    for board in boards:
        print_board(board)
        print

def next(s, piece, r, c, r_n, c_n):
    s_prime = s[:r*8+c] + '.' + s[r*8+c + 1:]
    board = s_prime[:r_n*8 + c_n] + piece + s_prime[r_n*8 + c_n+1:]
    print_board(board)
    print
    return board
#######################################################################################

turn, S0, time = sys.argv[1], sys.argv[2], float(sys.argv[3])
possible_move = {'K':K,'Q':Q,'R':R,'B':B,'N':N,'P':P,'k':K,'q':Q,'r':R,'b':B,'n':N,'p':p}
player = {'w':['K','Q','R','B','N','P'], 'b':['k','q','r','b','n','p']}
# print_board(S0)
# print
# S1 = successor(S0, turn)
# for board in S1:
    # print_board(board)

# print_bs(S1)
