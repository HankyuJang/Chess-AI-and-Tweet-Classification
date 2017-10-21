import sys
import cPickle
import shelve

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
            global succ_count
            succ_count += 1
#            print "Successor accessed from dictionary"
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
        if turn == t:
            if piece in player[change_turn(t)]:
                f[4] -= value[piece]
                possible_moves = possible_move[piece](r, c)
                for r_n, c_n in possible_moves:
                    if is_valid(s, change_turn(t), piece, r, c, r_n, c_n):
                        f[0] -= 1
    succ_dict[s] = {}
    succ_dict[s][t] = (board_list, move_list)
    if t == turn:
        cost_dict[s] = {}
        cost_dict[s][t] = sum(f)
    return (board_list, move_list)

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
#    if s in cost_dict:
#        if turn in cost_dict[s]:
#            return cost_dict[s][turn]
    try:
        cost_count += 1
        return cost_dict[s][turn]
    except:
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
        return sum(f)
#==============================================================================

#==============================================================================
# Mini-Max with alpha beta pruning
def minimax_decision(s, turn, h=3):
    if s in move_dict:
        if turn in move_dict[s]:
            return move_dict[s][turn]
    s_p, m = successor(s, turn)
    return max([(x[0], x[1], min_value(x[0], change_turn(turn), h-1, -inf, inf)) for x in zip(s_p, m)], key = lambda item: item[2])[:2]
#    return max(map(lambda x: (x[0], x[1], min_value(x[0], turn, h, -inf, inf)), zip(s, m)), key = lambda k: k[2])[:2]

def max_value(s, t, h, alpha=-inf, beta=inf):
#    print_board(s)
    if h == 0:
        return calculate_cost(s)
    for s_prime in successor(s, t)[0]:
        alpha = max(alpha, min_value(s_prime, change_turn(t), h-1, alpha, beta))
        if alpha >= beta:
            return alpha
    return alpha
#    return max([min_value(s_prime, change_turn(t), h-1) for s_prime in successor(s, t)[0]])

def min_value(s, t, h, alpha=-inf, beta=inf):
#    print_board(s)
    if h == 0:
        return calculate_cost(s)
    for s_prime in successor(s, t)[0]:
        beta = min(beta, max_value(s_prime, change_turn(t), h-1, alpha, beta))
        if alpha >= beta:
            return beta
    return beta
#    return min([max_value(s_prime, change_turn(t), h-1) for s_prime in successor(s, t)[0]])

def change_turn(turn):
    return "b" if turn == "w" else "w"

#==============================================================================

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

#try:
#    with open("succ_dict.txt") as f:
#        succ_dict = cPickle.load(f)
#except:
succ_dict = {}
succ_count = 0
#try:
#    with open("cost_dict.txt") as f:
#        cost_dict = cPickle.load(f)
#except:
cost_dict = {}
cost_count = 0
try:
    with open("move_dict.txt") as f:
        move_dict = cPickle.load(f)
except:
    move_dict = {}

h = 4
for i in range(1, h+1):
#    if
    S_next, M_next = minimax_decision(S0, turn, i)
    piece, r, c, r_n, c_n = M_next
    print "Thinking! Please wait...\n"
    print "Hmm, I'd recommend moving the {} at row {} column {} to row {} column {}.".format(name[piece],r,c,r_n,c_n)
    print "New board:"
    print S_next
    print

move_dict[S0] = {}
move_dict[S0][turn] = (S_next, M_next)
#cPickle.dump(succ_dict, open('succ_dict.txt', 'w'))
#cPickle.dump(cost_dict, open('cost_dict.txt', 'w'))
cPickle.dump(move_dict, open('move_dict.txt', 'w'))

#######################################################################################
# Remove these lines later
print_board(S0)
print("")
print_board(S_next)

#succ_shelve = shelve.open('succ.db', writeback = True)
#cost_shelve = shelve.open('cost.db', writeback = True)
#move_shelve = shelve.open('move.db', writeback = True)
#move_shelve[S0] = (S_next, M_next)
#succ_shelve.close()
#cost_shelve.close()
#move_shelve.close()
#######################################################################################
