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
    Step 1: Pick a key pair to start | Step 2: Print key pair
    Step 3: Choose a value from potential next words
    Step 4: Print value | Step 5: Make key[1] and value in to new key
    Step 6: Go to Step 3, repeat until done
    """
    init_key = random.choice(chains.keys())
    while not init_key[0].isupper():
        init_key = random.choice(chains.keys())

    markov_text = init_key[0] + " " + init_key[1]
    count = 0
    while init_key in chains and count < 800:
        choose_value = random.choice(chains[init_key])
        markov_text = markov_text + " " + choose_value
        init_key = (init_key[1], choose_value)
        count += 1
    
    return markov_text
    """ 
    Potential awesome things to do:
    1: Make the seed pair make sense as the start of a sentence
    2: Make the print out structure more like the play.
    3: Utilize punctuation
    4: Mashup
    5: Tweet
    """

def make_format(body):
    words = body.split()

    formatted_list = []
    formatted_words = ""

    idx = 0

    for word in range(len(words)-2):  # this prints out a list of capital words
        current_word = words[idx]
        next_word = words[idx+1]

        current_upper = current_word.isupper() and len(current_word)>1
            # return boolean values
        next_upper = next_word.isupper() and len(next_word)>1

        # different_case = (current_upper and not next_upper) or (next_upper and not current_upper)

        # if (current_upper and next_upper) or (current_upper not and next_upper):

        formatted_list.append(current_word)
        if current_upper and not next_upper:
            formatted_list.append(":\n\n")
        elif next_upper and not current_upper:
            # # check last character of current word --
            # if next_upper[-1] == ord()
            # # if last character is not punctuation, insert some punctuation
            formatted_list.append(".\n\n")
        formatted_list.append(" ")            # print "first option"

        idx +=1
        

#this takes the list and makes it a string.
    for word in formatted_list:
        # print "formatted list print out"
        formatted_words += word.format(formatted_words)

            # print word.index
    print "the string is ", formatted_words
    # print "the list is ", formatted_list




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
