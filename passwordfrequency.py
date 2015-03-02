
import string

def get_word_list(file_name):
    """ Creates a dictionary of passwords and their counts.
    file_name: name of txt file
    returns: dictionary
    """
    f = open(file_name,'r')
    count = dict()
    all_words = []
    lines = f.readlines()

    for line in lines:
        words_in_line = string.split(line)
        if len(words_in_line) == 1:
            pass
        elif words_in_line[1] not in count:
            count[words_in_line[1]] = 1
        else:
            count[words_in_line[1]] += 1        
    return count


def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
        occurring words ordered from most to least frequently occurring.

        word_list: a list of words 
        n: the number of words to return
        returns: a list of n most frequently occurring words ordered from most
                 frequently to least frequently occurring
    """
    sort = sorted(word_list, key = word_list.get, reverse = True)
    return sort[:n]


counts = get_word_list("10-million-combos.txt")
print get_top_n_words(counts, 25)