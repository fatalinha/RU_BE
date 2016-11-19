#!/usr/bin/env python3
"""
Transliterates Italian to Spanish based on hand-written rules
Usage: ./translit_it_sp.py <italian_infile >transliterated_outfile
Note infile should be all lowercase, with punctuation separated

Created by Anna Currey for related languages project
Statistical Language Modeling
Summer Semester 2015

"""
# TO DO ignore accents in italian?
# TO DO did I add an extra space at end of line?
# TO DO maybe make à be a and not á (and so on)

import sys
from it_sp_dict import it_sp_dict

# initialize with most common translations of most common words
translit_word = it_sp_dict

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
    elif word[:2] == 'st':
        return 'est' + word[2:]
    elif word[:3] == 'esp':
        return 'exp' + word[3:]
    elif word[:3] == 'gia':
        return 'ya' + word[3:]
    elif word[:3] == 'esc':
        return 'exc' + word[3:]
    elif word[:3] == 'que':
        return 'cue' + word[3:]
    elif word[:3] == 'quo':
        return 'co' + word[3:]
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
    # also deal with plural
    elif word[-6:] == 'ssioni':
        new_word = word[:-6] + 'siones'
    # have to do this rule before one dealing with ne
    elif word[-5:] == 'sione':
        new_word = word[:-5] + 'sión'
    elif word[-5:] == 'sioni':
        new_word = word[:-5] + 'siones'
    # have to do this rule before one dealing with ne
    elif word[-5:] == 'zione':
        new_word = word[:-5] + 'ción'
    elif word[-5:] == 'zioni':
        new_word = word[:-5] + 'ciones'
    elif word[-3:] == 'are':
        new_word = word[:-3] + 'ar'
    elif word[-3:] == 'ere':
        new_word = word[:-3] + 'er'
    elif word[-2:] == 'ne':
        new_word = word[-2:] + 'n'
    # again deal with plurals
    elif word[-2:] == 'ni':
        new_word = word[-2:] + 'nes'
    elif word[-3:] == 'ire':
        new_word = word[:-3] + 'ir'
    # TODO what about accents in italian
    elif word[-2:] == 'le' and len(word) > 2 and word[-3] in ['a', 'e', 'i', 'o', 'u']:
        new_word = word[:-2] + 'l'
    elif word[-2:] == 'li' and len(word) > 2 and word[-3] in ['a', 'e', 'i', 'o', 'u']:
        new_word = word[:-2] + 'les'
    elif word[-3:] == 'ore':
        new_word = word[:-3] + 'or'
    elif word[-3:] == 'ori':
        new_word = word[:-3] + 'ores'
    elif word[-2:] == 'tà':
        new_word = word[:-2] + 'dad'
    # removed because of 'dice'
    #elif word[-2:] == 'ce' and len(word) > 2 and word[-3] != 'l':
    #    new_word = word[:-2] + 'z'
    elif word[-2:] == 'ci' and len(word) > 2 and word[-3] != 'l':
        new_word = word[:-2] + 'ces'
    # moved from word middle
    elif word[-3:] == 'ato':
        new_word = word[:-3] + 'ado'
    elif word[-3:] == 'ata':
        new_word = word[:-3] + 'ada'
    elif word[-3:] == 'ati':
        new_word = word[:-3] + 'ados'
    elif word[-3:] == 'ate':
        new_word = word[:-3] + 'adas'
    # removed because of 'dice'
    #elif word[-3:] == 'ice':
    #    new_word = word[:-3] + 'iz'
    #elif word[-3:] == 'ici':
    #    new_word = word[:-3] + 'ices'
    elif word[-4:] == 'bile':
        new_word = word[:-4] + 'ble'
    elif word[-4:] == 'bili':
        new_word = word[:-4] + 'bles'
    elif word[-8:] == 'bilmente':
        new_word = word[:-8] + 'blemente'
    return new_word


## elsewhere in the word
def word_middle(word):
    '''
    Replaces Italian clusters with Spanish clusters
    Input: original word (string)
    Returns: word with Italian clusters replaced if necessary (string)
    '''
    new_word = word
    # TODO what about accents in italian
    new_word = new_word.replace('cch', 'j')
    new_word = new_word.replace('cci', 'z')
    new_word = new_word.replace('cc', 'c')
    new_word = new_word.replace('che', 'que')
    new_word = new_word.replace('zz', 'z')
    # note need to have cci rule before this one
    new_word = new_word.replace('zi', 'ci')
    new_word = new_word.replace('ss', 's')
    new_word = new_word.replace('tt', 't')
    new_word = new_word.replace('gn', 'ñ')
    new_word = new_word.replace('gli', 'j')
    new_word = new_word.replace('ap', 'ab')
    new_word = new_word.replace('uo', 'o') # TODO Does this interact with aiu
    new_word = new_word.replace('mm', 'm')
    new_word = new_word.replace('nn', 'n')
    new_word = new_word.replace('bb', 'b')
    new_word = new_word.replace('aiu', 'ayu') # TODO does this interact with uo
    new_word = new_word.replace('pp', 'p')
    # TODO more ggV?
    new_word = new_word.replace('ggi', 'y')
    # change impossible accents -- put last so don't interfere with other
    new_word = new_word.replace('à', 'a')
    new_word = new_word.replace('è', 'e')
    new_word = new_word.replace('ì', 'i')
    new_word = new_word.replace('ò', 'o')
    new_word = new_word.replace('ù', 'u')
    # some impossible double consonants
    new_word = new_word.replace('vv', 'v')
    new_word = new_word.replace('ff', 'f')
    new_word = new_word.replace('dd', 'd') # TODO maybe need to fix
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