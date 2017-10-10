

import sys
import re

preposition = ['a', 'an', 'and', 'the']

def readfile(infile):
    word_dict = {}
    hashtag_dict = {}
    with open(infile, 'r') as f:
        for line in f:
            city, tweet = line.split(',', 1) # Separate city and tweet
            _, tweet = tweet.split(' ', 1) # Remove the state info
            word_list = get_words(tweet) # Get only the lowercase words
            hashtag_list = get_hashtags(tweet) # Get hashtags
            fill_dictionary(city, word_list, word_dict) # Fill in the word_dict
            fill_dictionary(city, hashtag_list, hashtag_dict) # Fill in the hashtag_dict
    return word_dict, hashtag_dict

def fill_dictionary(city, word_list, word_dict):
    for word in word_list:
        if word in word_dict:
            if city in word_dict[word]:
                word_dict[word][city] += 1
            else:
                word_dict[word][city] = 1
        else:
            word_dict[word] = {}
            word_dict[word][city] = 1

def get_hashtags(tweet):
    return [word[1:] for word in tweet.split() if word.startswith("#")]

def get_words(tweet):
    return [word.lower() for word in re.split(r"[\W_]", tweet) if word != '']

if __name__ == "__main__":
    training_file = sys.argv[1]
    testing_file = sys.argv[2]
    output_file = sys.argv[3]

    word, hashtag = readfile(training_file)

    print("Dictionaries created. check 'word' or 'hashtag'")
    
