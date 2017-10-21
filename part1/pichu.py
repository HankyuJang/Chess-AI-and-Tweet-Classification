import sys
import json

def p(r,c):
    return [(r,c) for r,c in [(r-1,c),(r-1,c-1),(r-1,c+1),(r-2,c)] if in_board(r,c)] if r==6 else [(r,c) for r,c in [(r-1,c),(r-1,c-1),(r-1,c+1)] if in_board(r,c)]
def P(r,c):
    return [(r,c) for r,c in [(r+1,c),(r+1,c-1),(r+1,c+1),(r+2,c)] if in_board(r,c)] if r==1 else [(r,c) for r,c in [(r+1,c),(r+1,c-1),(r+1,c+1)] if in_board(r,c)]
def N(r, c):
    return [(r,c) for r,c in [(r+2,c-1),(r+2,c+1),(r+1,c-2),(r+1,c+2),(r-1,c-2),(r-1,c+2),(r-2,c-1),(r-2,c+1)] if in_board(r,c)]
def B(r, c):
    diff, summ = r-c, r+c
    return [(r,c) for r,c in filter(lambda a: a != (r, c), [(i, i-diff) for i in range(8)] + [(i, summ-i) for i in range(8)]) if in_board(r,c)]
def R(r, c):
    return [(r,c) for r,c in filter(lambda a: a != (r, c), [(r,i) for i in range(8)] + [(i,c) for i in range(8)]) if in_board(r,c)]
def Q(r, c):
    return R(r,c) + B(r,c)
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

def successor(s, t):
    if s in succ_dict:
        if t in succ_dict[s]:
#            print "Good! - succ"
            return succ_dict[s][t]
    board_list = []
    move_list = []
    f = [0, 0, 0, 0, 0]
    global turn
    for i, piece in enumerate(s):
        r, c = i/8, i%8
        if piece in player[t]:
            f[4] += value[piece]
            possible_moves = possible_move[piece](r, c)
            # board_list.extend([next_board(s,piece,r,c,r_n,c_n) for r_n,c_n in possible_moves if is_valid(s,turn,piece,r,c,r_n,c_n)])
            boards = []
            for r_n, c_n in possible_moves:
                if is_valid(s, t, piece, r, c, r_n, c_n):
                    boards.append(next_board(s, piece, r, c, r_n, c_n))
                    move_list.append((piece, r, c, r_n, c_n))
                    f[0] += 2
            board_list.extend(boards)
        if piece in player[change_turn(t)]:
            f[4] -= value[piece]
            possible_moves = possible_move[piece](r, c)
            for r_n, c_n in possible_moves:
                if is_valid(s, change_turn(t), piece, r, c, r_n, c_n):
                    f[0] -= 1
    succ_dict[s] = {}
    succ_dict[s][t] = (board_list, move_list)
    cost_dict[s] = {}
    cost_dict[s][t] = sum(f)
    return succ_dict[s][t]

def is_valid(s, turn, piece, r, c, r_n, c_n):
    if turn=='w':
        if piece=='P': # Check the 'P' in advance
            if r_n-r == 1 and c_n==c: # Check one-step move
                if loc(s, r_n, c_n) != '.':
                    return False
            elif r_n-r == 2: # Check the inital two-step move
                if loc(s,2,c) != '.':
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
                if loc(s,5,c) != '.':
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

#==============================================================================
# Calculate cost
def calculate_cost(s):
    # calculate f1, f5 of the evaluation function
#value = A.get("blah", None)
#if value is not None:
#    A["blah"] = value
    if s in cost_dict:
        if turn in cost_dict[s]:
            return cost_dict[s][turn]

    f = [0,0,0,0,0]
#    squares_controlled = []
    for i, piece in enumerate(s):
        r, c = i/8, i%8
        if piece in player[turn]:
            f[4] += value[piece]
            possible_moves = possible_move[piece](r, c)
            for r_n,c_n in possible_moves:
                if is_valid(s,turn,piece,r,c,r_n,c_n):
                    f[0] += 2
            continue
        if piece in player[change_turn(turn)]:
            f[4] -= value[piece]
            possible_moves = possible_move[piece](r, c)
            for r_n,c_n in possible_moves:
                if is_valid(s,change_turn(turn),piece,r,c,r_n,c_n):
                    f[0] -= 1
    cost_dict[s] = {}
    cost_dict[s][turn] = sum(f)      # <-if the turn changes then cost should be -ve
    return cost_dict[s][turn]
#==============================================================================

#==============================================================================
# Mini-Max
def minimax_decision(s, turn, h=4):
    s, m = successor(s, turn)
    return max([(x[0], x[1], min_value(x[0], change_turn(turn), h-1, -inf, inf)) for x in zip(s, m)], key = lambda item: item[2])[:2]
#    return max(map(lambda x: (x[0], x[1], min_value(x[0], turn, h)), zip(s, m)), key = lambda k: k[2])[:2]

def max_value(s, t, h, alpha=0, beta=0):
#    print_board(s)
    if h == 0:
        return calculate_cost(s)
    return max([min_value(s_prime, change_turn(t), h-1) for s_prime in successor(s, t)[0]])

def min_value(s, t, h, alpha=0, beta=0):
#    print_board(s)
    if h == 0:
        return calculate_cost(s)
    return min([max_value(s_prime, change_turn(t), h-1) for s_prime in successor(s, t)[0]])

def change_turn(turn):
    return "b" if turn == "w" else "w"

#==============================================================================

# Returns the best successor
#
# Current version: 1 depth BFS.
#
def solve(s, turn):
    successors, moves = successor(s, turn)
    cost_list = [calculate_cost(s_prime) for s_prime in successors]
    if turn == 'w':
        idx = cost_list.index(max(cost_list))
        succ_next = successors[idx]
        move_next = moves[idx]
    else: # if black's turn, take the min cost
        idx = cost_list.index(min(cost_list))
        succ_next = successors[idx]
        move_next = moves[idx]
    return succ_next, move_next

#######################################################################################
# These are just functions to print results. I won't need them to run the script.
def print_board(s):
    print "\n".join([" ".join(s[i:i+8]) for i in range(0,64,8)])

def print_successors(s):
    for board in successor(s, turn)[0]:
        print_board(board)
        print

def next(s, piece, r, c, r_n, c_n):
    s_prime = s[:r*8+c] + '.' + s[r*8+c + 1:]
    board = s_prime[:r_n*8 + c_n] + piece + s_prime[r_n*8 + c_n+1:]
    print_board(board)
    print
    return board
#
#######################################################################################
turn, S0, time = sys.argv[1], sys.argv[2], float(sys.argv[3])
possible_move = {'K':K,'Q':Q,'R':R,'B':B,'N':N,'P':P,'k':K,'q':Q,'r':R,'b':B,'n':N,'p':p}
player = {'w':['K','Q','R','B','N','P'], 'b':['k','q','r','b','n','p']}
value = {'K':200,'Q':9,'R':5,'B':3,'N':3,'P':1,'k':200,'q':9,'r':5,'b':3,'n':3,'p':1}
name = {'K':"Kingfisher",'Q':"Quetzal",'R':"Robin",'B':"Blue jay",'N':"Nighthawk",'P':"Parakeet",
        'k':"kingfisher",'q':"quetzal",'r':"robin",'b':"blue jay",'n':"nighthawk",'p':"parakeet"}
try:
    with open("succ_dict.txt") as f:
        succ_dict = json.load(f)
except:
    succ_dict = {}
try:
    with open("cost_dict.txt") as f:
        cost_dict = json.load(f)
except:
    cost_dict = {}

print("Thinking! Please wait...\n")
#S_next, M_next = solve(S0, turn)
S_next, M_next = minimax_decision(S0, turn)
piece, r, c, r_n, c_n = M_next
print("Hmm, I'd recommend moving the {} at row {} column {} to row {} column {}.".format(name[piece],r,c,r_n,c_n))
#######################################################################################
# Remove these lines later
print_board(S0)
print("")
print_board(S_next)
# Saving the files

json.dump(succ_dict, open('succ_dict.txt', 'w'))
json.dump(cost_dict, open('cost_dict.txt', 'w'))
#
#######################################################################################
print("\n\nNew board:")
print(S_next)
