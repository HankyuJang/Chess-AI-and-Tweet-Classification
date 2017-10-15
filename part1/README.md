# Pichu (Simplified version of chess) playing AI agent

## Method: Minimax algorithm with alpha-beta search

### Evaluation Function

<a href="https://www.codecogs.com/eqnedit.php?latex=e(s)&space;=&space;\sum_{i=1}^5{&space;w_i&space;f_i}(s)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e(s)&space;=&space;\sum_{i=1}^5{&space;w_i&space;f_i}(s)" title="e(s) = \sum_{i=1}^5{ w_i f_i}(s)" /></a>

where 

- <a href="https://www.codecogs.com/eqnedit.php?latex=f_1(s)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_1(s)" title="f_1(s)" /></a> = Number of possible moves of the pieces for White - Number of possible moves of the pieces for Black
- <a href="https://www.codecogs.com/eqnedit.php?latex=f_2(s)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_2(s)" title="f_2(s)" /></a> = Black checkmated - White checkmated (here 1 if checkmate, otherwise 0)
- <a href="https://www.codecogs.com/eqnedit.php?latex=f_3(s)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_3(s)" title="f_3(s)" /></a> = Number of open tiles for Kingfisher for White - Number of open tiles for Kingfisher for Black
- <a href="https://www.codecogs.com/eqnedit.php?latex=f_4(s)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_4(s)" title="f_4(s)" /></a> = Number of trapped pieces for Black - Number of trapped pieces for White
- <a href="https://www.codecogs.com/eqnedit.php?latex=f_5(s)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_5(s)" title="f_5(s)" /></a> = Sum of the values of pieces for White - Sum of the values of pieces for Black

and

<a href="https://www.codecogs.com/eqnedit.php?latex=w&space;=&space;(1,100,3,3,1)&space;\in&space;R^5" target="_blank"><img src="https://latex.codecogs.com/gif.latex?w&space;=&space;(1,100,3,3,1)&space;\in&space;R^5" title="w = (1,100,3,3,1) \in R^5" /></a>

- Trapped piece: A piece if moved, loses Kingfisher of Quetzal.

- Value of each pieces on chess board
    - Parakeet - 1 point
    - Nighthawk - 3 points
    - Blue jay - 3 points
    - Robin - 5 points
    - Quetzal - 9 points

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
