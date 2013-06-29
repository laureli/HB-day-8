#!/usr/bin/env python
from sys import argv
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_chains = {}

    words = corpus.split()

    for idx in range(len(words)-2):
        key_pair = (words[idx], words[idx+1])
        pair_value = words[idx+2]
        if key_pair not in markov_chains:
            markov_chains.setdefault(key_pair, [pair_value])
        else:
            markov_chains[key_pair].append(pair_value)

    return markov_chains

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    """
    Step 1: Pick a key pair to start
    Step 2: Print key pair
    Step 3: Choose a value from potential next words
    Step 4: Print value
    Step 5: Make key[1] and value in to new key
    Step 6: Go to Step 3, repeat until done
    """
    init_key = random.choice(chains.keys())
    while not init_key[0].isupper():
        init_key = random.choice(chains.keys())

    markov_text = init_key[0] + " " + init_key[1]
    count = 0
    while init_key in chains and count < 500:
        choose_value = random.choice(chains[init_key])
        markov_text = markov_text + " " + choose_value
        init_key = (init_key[1], choose_value)
        count += 1
    
    return markov_text
    """
    Potential awesome things to do:
    1: Limit the length of the text
    2: Make the seed pair make sense as the start of a sentence
    2a. Make the print out structure more like the play.
    3: Utilize punctuation
    4: Mashup
    5: Tweet
    """

def make_format(body):
    """
    Takes the mass of text and formats it to appear more like a script.Capitalization will determine spacing:
        words in all caps are set off with new lines b/c are 
        character names or stage directions
    # """
    print type(body)

    words = body.split()
    # upper_words = []
    # lower_words = []

    for word in words:  # this prints out a list of capital words
        if word.isupper() and len(word)>2:
            # print word.index
            print word

    # print words

    """
    Step 1: Access word in all caps  -- okay
    Step 2: Print words in all caps  -- okay
    Step 3: Add 2 new lines above (1 empty line) and 1 below
        --> this means making a new string?
    Step 4: Combine capital words with un-capitalized

    ISSUES: What if multiple capitalized words follow each other?
            What about I, O, A, 
    """


def main():
    script, from_file = argv
    #args = sys.argv
    text = open(from_file)
    book = text.read()
    # Change this to read input_text from a file
    input_text = "Some text"
    text.close()

    chain_dict = make_chains(book)
    random_text = make_text(chain_dict)
    format_text = make_format(random_text)
    #print random_text

if __name__ == "__main__":
    main()
