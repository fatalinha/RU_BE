#!/usr/bin/env python3
"""
Transliterates Russian to Belorussian based on hand-written rules
Usage: ./translit_ru_be.py <russian_infile >transliterated_outfile
Note infile should be all lowercase, with punctuation separated

Based on code by Anna Currey for related languages project
Statistical Language Modeling
Summer Semester 2015

"""

# Instructions: The model we are training is a character-based one. 
# Therefore, it is important that we eliminate impossible Russian characters 
# into Belorussian. Please add the equivalent BE character in the place of ??? (lines 31-32)

import sys
from ru_be_dict import ru_be_dict

# initialize with most common translations of most common words
translit_word = ru_be_dict

## elsewhere in the word
def word_middle(word):
    '''
    Replaces Russian clusters with Belorussian clusters
    Input: original word (string)
    Returns: word with Russian clusters replaced if necessary (string)
    '''
    new_word = word
    new_word = new_word.replace('и', '???')
    new_word = new_word.replace('ъ', '???')
    return new_word


if __name__ == '__main__':
    # read in the input line by line (one sentence per line)
    for line in sys.stdin.readlines():
        # look at each word
        words = line.split()
        for word in words:
            # process word
            # check if it's in the dictionary first
            if word in translit_word:
                sys.stdout.write(translit_word[word] + ' ')
            else:
                # word middle needs to go last because of interactions
                word_new = word_end(word)
                word_new = word_begin(word_new)
                word_new = word_middle(word_new)
                # add it to the dictionary
                translit_word[word] = word_new
                # then print it to the outfile
                sys.stdout.write(word_new + ' ')
        # print a new line
        sys.stdout.write('\n')
