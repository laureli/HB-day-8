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
    markov_text = init_key[0] + " " + init_key[1]
    count = 0
    while init_key in chains and count < 100:
        choose_value = random.choice(chains[init_key])
        markov_text = markov_text + " " + choose_value
        init_key = (init_key[1], choose_value)
        count += 1
    print markov_text
    """
    Potential awesome things to do:
    1: Limit the length of the text
    2: Make the seed pair make sense as the start of a sentence
    2a. Make the print out structure more like the play.
    3: Utilize punctuation
    4: Mashup
    5: Tweet
    """
    return "Here's some random text."

def main():
    # script, from_file = argv
    # args = sys.argv
    text = open("sophocles.txt")
    book = text.read()
    # Change this to read input_text from a file
    input_text = "Some text"
    text.close()

    chain_dict = make_chains(book)
    random_text = make_text(chain_dict)
    #print random_text

if __name__ == "__main__":
    main()