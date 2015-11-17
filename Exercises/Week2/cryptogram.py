The goal is to create a program that will take a string, create a random letter dictionary and
print the jumbled string under a series of blanks.  (Think newspaper jumble)

import random

def make_dash(string):
    '''input a string and return a string that is made up only of dashes.
    Be sure that spaces in the string are maintained. Each dash should
    represent a letter
    '''



def make_new_key():
    '''This function should take the alphabet list provided
    randomly append letters to new_alpha while removing those letters
    from alphabet (so there are no repeats - pop()) and then making a
    dictionary using alphabet_save as the keys and new_alpha as the values
    '''


def scramble(string, mapper):
    '''This function takes a string and the mapper dict created above
    use the dictionary to return a random string while preserving space
    '''


sentence = "the quick brown fox jumps over the lazy dog"
new_key = make_new_key()
print("\n\n" + make_dash(sentence))
print(scramble(sentence, new_key))
