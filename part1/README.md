# Pichu (Simplified version of chess) playing AI agent

## Method: Minimax algorithm with alpha-beta search

### Evaluation Function

<a href="https://www.codecogs.com/eqnedit.php?latex=e(s)&space;=&space;\sum_{i=1}^5{&space;w_i&space;f_i}(s)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?e(s)&space;=&space;\sum_{i=1}^5{&space;w_i&space;f_i}(s)" title="e(s) = \sum_{i=1}^5{ w_i f_i}(s)" /></a>

where 

- <a href="https://www.codecogs.com/eqnedit.php?latex=f_1(s)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_1(s)" title="f_1(s)" /></a> = Number of possible moves of the pieces for Max - Number of possible moves of the pieces for Min
- <a href="https://www.codecogs.com/eqnedit.php?latex=f_2(s)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_2(s)" title="f_2(s)" /></a> = Min checkmated - Max checkmated (here 1 if checkmate, otherwise 0)
- <a href="https://www.codecogs.com/eqnedit.php?latex=f_3(s)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_3(s)" title="f_3(s)" /></a> = Number of open tiles for Kingfisher for Max - Number of open tiles for Kingfisher for Min
- <a href="https://www.codecogs.com/eqnedit.php?latex=f_4(s)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_4(s)" title="f_4(s)" /></a> = Number of trapped pieces for Min - Number of trapped pieces for Max
- <a href="https://www.codecogs.com/eqnedit.php?latex=f_5(s)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f_5(s)" title="f_5(s)" /></a> = Sum of the values of pieces for Max - Sum of the values of pieces for Min

and

<a href="https://www.codecogs.com/eqnedit.php?latex=w&space;=&space;(1,100,3,3,1)&space;\in&space;R^5" target="_blank"><img src="https://latex.codecogs.com/gif.latex?w&space;=&space;(1,100,3,3,1)&space;\in&space;R^5" title="w = (1,100,3,3,1) \in R^5" /></a>

- Trapped piece: A piece if moved, loses Kingfisher of Quetzal.

- Value of each pieces on chess board
    - Parakeet - 1 point
    - Nighthawk - 3 points
    - Blue jay - 3 points
    - Robin - 5 points
    - Quetzal - 9 points



To embed the formula to this markdown file, I used the following ![https://www.codecogs.com/latex/eqneditor.php](link) to convert the latex syntex into the html.

```
e(s) = \sum_{i=1}^5{ w_i f_i}(s)
w = (1,100,3,3,1) \in R^5

```
