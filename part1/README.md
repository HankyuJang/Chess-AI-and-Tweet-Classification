# Pichu (Simplified version of chess) playing AI agent

## Method: Minimax algorithm with alpha-beta search

### Evaluation Function

<a href="https://www.codecogs.com/eqnedit.php?latex=e(s)&space;=&space;\sum_{i=0}^2{&space;w_i&space;f_i}(s)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e(s)&space;=&space;\sum_{i=0}^2{&space;w_i&space;f_i}(s)" title="e(s) = \sum_{i=0}^2{ w_i f_i}(s)" /></a>

where 

- <a href="https://www.codecogs.com/eqnedit.php?latex=f_0(s)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_0(s)" title="f_0(s)" /></a> = sum of value of pieces of MAX - sum of value of pieces of MIN
- <a href="https://www.codecogs.com/eqnedit.php?latex=f_1(s)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_1(s)" title="f_1(s)" /></a> = number of moves possible for MAX - number of moves possible for MIN
- <a href="https://www.codecogs.com/eqnedit.php?latex=f_2(s)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_2(s)" title="f_2(s)" /></a> = number of unique places in the board on which only MAX can attack in the next move

and

<a href="https://www.codecogs.com/eqnedit.php?latex=w&space;=&space;(10,1,1)&space;\in&space;R^3" target="_blank"><img src="https://latex.codecogs.com/gif.latex?w&space;=&space;(10,1,1)&space;\in&space;R^3" title="w = (10,1,1) \in R^3" /></a>

One interesting thing about `f[2]` is that, if say MAX's bishop can attack on (1,1) and MIN's bishop can also attack on (1,1) then it will be "0".
But if there's another MAX's piece that can attack on (1,1) then we will count that as "1"

- Value of each pieces on chess board
    - Parakeet - 1 point
    - Nighthawk - 3 points
    - Blue jay - 3 points
    - Robin - 5 points
    - Quetzal - 9 points
    - Kingfisher - 1,000 points

The fourth evaluation function that we wanted to implement was the Pawn Structure
    - For each pawn of MAX, +1 for each of MAX piece in the pawn's diagonal places

- The Algorithm 

We are using Mini-Max Algorithm with alpha beta pruning along with some additional features
    - Our algorithm works in a Iterative Deepening Depth First Search fashion
    - To make it work faster, we stored the successors of each state in a dictionary, so when we increase the max_depth of our algorithm        we can avoid finding successors again and again
    - We also calculated the evaluation of a state while finding its successors and stored it in a dictionary. This way we were avoiding        looping through the board since we were already doing that while finding it's successors.
    - We started our algorithm from height 3 which could be evaluated within a couple of seconds. So at first, we run minimax normally          and record for each state which is its 'max' successor or 'min' successor, we're storing this in a dictionary. 
    - Now, for the second time we increment the height by 3, ie, now run to a depth 6. However, this time for the first max node we             evaluate all it's successor and for each successor onwards we just access its best child, ie, max node or min node. However,            after height 3, we haven't explored anything yet, so we explore again normally for all its successors using minimax with alpha          beta pruning to height and again store each node's best successor, ie, max or min node.  
    - The algorithm keeps incrementing the height by 3 until the time ends.
    - For each iteration of height, we also save our dictionary to a file which can used in the next time run of the program


### Usage

Here's some plausible moves that occur in the beginning of a chess game. I printed two boards: above is the input board, below is the best successor.
Now, the evaluation only calculates the <a href="https://www.codecogs.com/eqnedit.php?latex=f_5(s)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_5(s)" title="f_5(s)" /></a> Sum of the values of pieces f    or White - Sum of the values of pieces for Black. 

```
[hankjang@silo part1]$ python -i pichu.py w RNBQKBNRPPPP.PPP............P......p............ppp.pppprnbqkbnr 10
Thinking! Please wait...

Hmm, I'd recommend moving the Parakeet at row 3 column 4 to row 4 column 3.

R N B Q K B N R
P P P P . P P P
. . . . . . . .
. . . . P . . .
. . . p . . . .
. . . . . . . .
p p p . p p p p
r n b q k b n r

R N B Q K B N R
P P P P . P P P
. . . . . . . .
. . . . . . . .
. . . P . . . .
. . . . . . . .
p p p . p p p p
r n b q k b n r

New board:
RNBQKBNRPPPP.PPP...................P............ppp.pppprnbqkbnr
```

Now it's black's turn. I fed in the New board as the input.

```
[hankjang@silo part1]$ python -i pichu.py b RNBQKBNRPPPP.PPP...................P............ppp.pppprnbqkbnr 10
Thinking! Please wait...

Hmm, I'd recommend moving the quetzal at row 7 column 3 to row 4 column 3.

R N B Q K B N R
P P P P . P P P
. . . . . . . .
. . . . . . . .
. . . P . . . .
. . . . . . . .
p p p . p p p p
r n b q k b n r

R N B Q K B N R
P P P P . P P P
. . . . . . . .
. . . . . . . .
. . . q . . . .
. . . . . . . .
p p p . p p p p
r n b . k b n r

New board:
RNBQKBNRPPPP.PPP...................q............ppp.pppprnb.kbnr
```



Here's are come more commands that shows how the program works. `next` function is just used for this example (not used in `solve`).

Each of functions, Q, K, R, ... returns the possible moves of each piece in a board assumign the board is empty (row, col) 

```
$ python -i pichu.py w RNBQKBNRPPPPPPPP................................pppppppprnbqkbnr 10
Q(0,0)
K(0,5)
R(1,1)
B(3,1)
N(5,5)
P(1,1)
p(6,1)
print_board(S0)
S1 = next(S0, 'p', 6, 4, 4, 4)
S2 = next(S1, 'P', 1, 4, 3, 4)
S3 = next(S2, 'p', 6, 3, 4, 3)
print_successors(successor(S3, 'w')[0])
print_board(S3)
S4 = next(S3, 'P', 3, 4, 4, 3)
S5 = next(S4, 'q', 7, 3, 4, 3)
```

These are the results.

```
[hankjang@silo part1]$ python -i pichu.py w RNBQKBNRPPPPPPPP................................pppppppprnbqkbnr 10
Thinking! Please wait...

Hmm, I'd recommend moving the Nighthawk at row 0 column 1 to row 2 column 0.

R N B Q K B N R
P P P P P P P P
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
p p p p p p p p
r n b q k b n r

R . B Q K B N R
P P P P P P P P
N . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
p p p p p p p p
r n b q k b n r

New board:
R.BQKBNRPPPPPPPPN...............................pppppppprnbqkbnr
>>> Q(0,0)
[(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]
>>> K(0,5)
[(1, 6), (1, 5), (1, 4), (0, 4), (0, 6)]
>>> R(1,1)
[(1, 0), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (0, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
>>> B(3,1)
[(2, 0), (4, 2), (5, 3), (6, 4), (7, 5), (0, 4), (1, 3), (2, 2), (4, 0)]
>>> N(5,5)
[(7, 4), (7, 6), (6, 3), (6, 7), (4, 3), (4, 7), (3, 4), (3, 6)]
>>> P(1,1)
[(2, 1), (2, 0), (2, 2), (3, 1)]
>>> p(6,1)
[(5, 1), (5, 0), (5, 2), (4, 1)]
>>> print_board(S0)

R N B Q K B N R
P P P P P P P P
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
p p p p p p p p
r n b q k b n r
>>> S1 = next(S0, 'p', 6, 4, 4, 4)

R N B Q K B N R
P P P P P P P P
. . . . . . . .
. . . . . . . .
. . . . p . . .
. . . . . . . .
p p p p . p p p
r n b q k b n r
>>> S2 = next(S1, 'P', 1, 4, 3, 4)

R N B Q K B N R
P P P P . P P P
. . . . . . . .
. . . . P . . .
. . . . p . . .
. . . . . . . .
p p p p . p p p
r n b q k b n r
>>> S3 = next(S2, 'p', 6, 3, 4, 3)

R N B Q K B N R
P P P P . P P P
. . . . . . . .
. . . . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r
>>> print_successors(successor(S3, 'w')[0])

R . B Q K B N R
P P P P . P P P
N . . . . . . .
. . . . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R . B Q K B N R
P P P P . P P P
. . N . . . . .
. . . . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B . K B N R
P P P P Q P P P
. . . . . . . .
. . . . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B . K B N R
P P P P . P P P
. . . . . Q . .
. . . . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B . K B N R
P P P P . P P P
. . . . . . . .
. . . . P . Q .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B . K B N R
P P P P . P P P
. . . . . . . .
. . . . P . . .
. . . p p . . Q
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q . B N R
P P P P K P P P
. . . . . . . .
. . . . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K . N R
P P P P B P P P
. . . . . . . .
. . . . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K . N R
P P P P . P P P
. . . B . . . .
. . . . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K . N R
P P P P . P P P
. . . . . . . .
. . B . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K . N R
P P P P . P P P
. . . . . . . .
. . . . P . . .
. B . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K . N R
P P P P . P P P
. . . . . . . .
. . . . P . . .
. . . p p . . .
B . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K B . R
P P P P . P P P
. . . . . N . .
. . . . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K B . R
P P P P . P P P
. . . . . . . N
. . . . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K B . R
P P P P N P P P
. . . . . . . .
. . . . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K B N R
. P P P . P P P
P . . . . . . .
. . . . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K B N R
. P P P . P P P
. . . . . . . .
P . . . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K B N R
P . P P . P P P
. P . . . . . .
. . . . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K B N R
P . P P . P P P
. . . . . . . .
. P . . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K B N R
P P . P . P P P
. . P . . . . .
. . . . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K B N R
P P . P . P P P
. . . . . . . .
. . P . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K B N R
P P P . . P P P
. . . P . . . .
. . . . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K B N R
P P P . . P P P
. . . . . . . .
. . . P P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K B N R
P P P P . . P P
. . . . . P . .
. . . . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K B N R
P P P P . . P P
. . . . . . . .
. . . . P P . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K B N R
P P P P . P . P
. . . . . . P .
. . . . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K B N R
P P P P . P . P
. . . . . . . .
. . . . P . P .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K B N R
P P P P . P P .
. . . . . . . P
. . . . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K B N R
P P P P . P P .
. . . . . . . .
. . . . P . . P
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r

R N B Q K B N R
P P P P . P P P
. . . . . . . .
. . . . . . . .
. . . P p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r
>>> print_board(S3)

R N B Q K B N R
P P P P . P P P
. . . . . . . .
. . . . P . . .
. . . p p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r
>>> S4 = next(S3, 'P', 3, 4, 4, 3)

R N B Q K B N R
P P P P . P P P
. . . . . . . .
. . . . . . . .
. . . P p . . .
. . . . . . . .
p p p . . p p p
r n b q k b n r
>>> S5 = next(S4, 'q', 7, 3, 4, 3)

R N B Q K B N R
P P P P . P P P
. . . . . . . .
. . . . . . . .
. . . q p . . .
. . . . . . . .
p p p . . p p p
r n b . k b n r
```

To embed the formula to this markdown file, I used the following ![https://www.codecogs.com/latex/eqneditor.php](link) to convert the latex syntex into the html.

```
e(s) = \sum_{i=1}^5{ w_i f_i}(s)
w = (1,100,3,3,1) \in R^5

```
