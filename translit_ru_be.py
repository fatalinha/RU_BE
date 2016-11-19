#!/usr/bin/env python3
"""
Transliterates Russian to Belorussian based on hand-written rules
Usage: ./translit_ru_be.py <russian_infile >transliterated_outfile
Note infile should be all lowercase, with punctuation separated

Based on code by Anna Currey for related languages project
Statistical Language Modeling
Summer Semester 2015

"""

# Instructions: In the case of impossible character combinations at the 
# beginning or end of the word, please add the rules under the appropriate 
# function. 

import sys
from ru_be_dict import ru_be_dict

# initialize with most common translations of most common words
translit_word = ru_be_dict

## beginning of words
def word_begin(word):
    '''
    Transliterates beginnings of words
    Input: original word (string)
    Returns: word with beginning modified if necessary (string)
    '''
    if word[:2] == 'sp':
        return 'esp' + word[2:]
    elif word[:3] == 'qua':
        return 'cua' + word[3:]
    return word


## end of words
def word_end(word):
    '''
    Transliterates ends of words
    Input: original word (string)
    Returns: word with ending modified if necessary (string)
    '''
    new_word = word
    # note have to do this rule before the ones dealing with sione, ne
    if word[-6:] == 'ssione':
        new_word = word[:-6] + 'sión'
    return new_word


## elsewhere in the word
def word_middle(word):
    '''
    Replaces Russian clusters with Belorussian clusters
    Input: original word (string)
    Returns: word with Russian clusters replaced if necessary (string)
    '''
    new_word = word
    new_word = new_word.replace('che', 'que')
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
