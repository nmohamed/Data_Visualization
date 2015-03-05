
import string
import heapq
import operator
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


def get_word_list(file_name):
    """ Creates a dictionary of passwords and their counts.
    file_name: name of txt file
    returns: dictionary
    """
    f = open(file_name,'r')
    count = dict()
    lines = f.readlines()

    for line in lines:
        words_in_line = string.split(line)
        if len(words_in_line) == 1 or words_in_line == []:
            pass
        elif words_in_line[1] not in count:
            count[words_in_line[1]] = 1
        else:
            count[words_in_line[1]] += 1        
    return count


def num_passwords(file_name):
    f = open(file_name,'r')
    words = []
    lines = f.readlines()
    for line in lines:
        words_in_line = string.split(line)
        if len(words_in_line) == 1:
            pass
        else:
            words.append(words_in_line[1])
    print len(words)
    return len(words)


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

def get_top_n_values(word_list, n):
    top_words = dict(sorted(word_list.iteritems(), key=operator.itemgetter(1), reverse=True)[:n])
    top_values = top_words.values()
    top_values = sorted(top_values, reverse = True)
    return top_values


def get_percent(num_passwords, top_values):
    percents = []
    for value in top_values:
        percents.append((float(value)/num_passwords)*100)
    return percents

def graph_percents(top_words, percents, top_values):
    y_pos = np.arange(len(top_words))
    performance = 3 + 10 * np.random.rand(len(top_words))

    plt.barh(y_pos, percents)
    plt.yticks(y_pos, top_words)
    plt.xlabel('Percentage')
    plt.title('Percent Apperance of Common Passwords')

    #plt.show()
    plt.savefig("percentsofcommon.gif")


counts = get_word_list("10-million-combos.txt")
top_values =  get_top_n_values(counts, 25)
num_passwords = num_passwords("10-million-combos.txt")
top_words = get_top_n_words(counts, 25)
#print top_values
#print top_words
percents = get_percent(num_passwords, top_values)
graph_percents(top_words, percents, top_values)

def compare_to_english(password):
    """ Compare input password to english words and see if password is english words
        or if it contains one
        Returns string stating "Not English" or "Contains English"
        >>> compare_to_english('friend')
        'Contains English'
    """
    f = open('/usr/share/dict/american-english', 'r')
    words = f.readlines()
    english = []
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'j', 'k', 'l', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'es', 'as', 'so']
    for line in words:
        if line.translate(None, '\n') in letters:
            pass
        else:
            english.append(line.translate(None, '\n'))

    matching = [word for word in english if word in password]
    if matching == []:
        return "Does not contain English"
    else:
        return "Contains English"



if __name__ == '__main__':
    counts = get_word_list('10-million-combos.txt')
    top_pw = get_top_n_words(counts, 10)
    #english = compare_to_english('qwrt')
    #print english
    #most common words, is it english

