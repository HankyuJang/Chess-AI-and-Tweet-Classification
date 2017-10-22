#Tweet Classification (Naive Bayes Multinomial Implementation):
Reference: http://sebastianraschka.com/Articles/2014_naive_bayes_1.html

Given:
A training set and a test set, each containing tweets and their corresponding locations (12 Locations in total for the training set).

Task:
Based on Training set, create a Naive Bayes model which, just based on the content of the tweet, predicts the corresponding location

Approach:
Naive Bayes Multinomial Implementation:

Every tweet in the test set contains specific words (w1, w2, w3 ... wN)

Probability(Location | w1,w2,w3...wn) = Probability(location) * Probability(w1,w2,w3...wN | Location) / Probability(w1,w2,w3...wN)

By Naive Bayes Assumption, given a class (Location in this case), all other factors / variables are independent of each other.
So,

P(Location | w1,w2,w3...wn) = P(location) * P(w1| Location)* P(w2| Location)...* P(wN| Location) / P(w1,w2,w3...wN) 

P(wN | Location) 
= Number of times 'wN' word has appeared in training set for all tweets in that Location / Total words in all tweets of that location

For all the locations, denominator is constant.
So, for every location, we compute the numerator, and assign location to the tweet for which numerator is maximum.

Additional Smoothing and Operations in the Equation:
A) Laplace Smoothing: (For every P(wN | Location), Numerator has been added by 1, and denominator by count of unique words.
It has been done to prevent any probability from becoming 0 

B) Log of Probabilities - Since the probability can become infinitesimal, log has been taken. log(A*B*C) = logA + logB + logC

C) Skipping New word - If a new word comes, which has never been encountered in Training data set, it has been skipped. 
If all words are new, then the city with the maximum count in training data will be assigned (since P(Location) will be highest)


Data Cleaning:
From the training and test inputs, following cleaning operations have been done:
1) Punctuations and symbols have been removed.
2) Stop words have been ignored.
3) All words converted to Lower case
4) Words have been trimmed till the length of 5
5) If total count of any word is only 1, it has been ignored
