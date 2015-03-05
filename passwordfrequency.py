
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
        if len(words_in_line) == 1 or words_in_line == []:
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
    counts = get_word_list('test_data.txt')
    top_pw = get_top_n_words(counts, 10)
    english = compare_to_english('qwrt')
    print english
    #most common words, is it english