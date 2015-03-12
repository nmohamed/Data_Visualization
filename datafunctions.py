# -*- coding: latin1 -*-
import string
import heapq
import operator
#import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from Levenshtein import distance
import re

class File(object):
    """ """
    def __init__(self, name, file_name, column):
        """Opens text file and creates a 
        column 0 = usernames, column 1 = passwords
        """
        self.name = name 
        self.text = open(file_name, 'r')
        self.column = column 
        lines =  self.text.readlines()
        the_list = []

        for line in lines:
            words_in_line = string.split(line)
            if len(words_in_line) == 1 or words_in_line == []:
                pass
            else:
                the_list.append(words_in_line[column])

        self.the_list = the_list


    def counts_dictionary(self):
        """ Creates a dictionary where the key is the words and the value 
        is the number of times they appear
        returns: dictionary
        """
        the_list = self.the_list
        column = self.column
        counts = dict()

        for word in the_list:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1  

        self.counts = counts   

    def length_of_file(self):
        """ returns lenth of file"""
        the_list = self.the_list
        self.length = len(the_list) #9997986


    def distance_from_list(self, your_word):
        """ 
        your_word: string that is your password
        Uses Levenshtein distance to find the number of characters off a password
        is from passwords and returns a dictionary where keys are passworeds and values = dist
        returns:dictionary"""
        dist = {}
        for word in self.the_list:
            if word in dist:
                pass
            else:
                dist[word] = distance(your_word, word)
        self.dist = dist


    def get_top_n_words(self, n = 25):
        """ Takes a list of words as input and returns a list of the n most frequently
            occurring words ordered from most to least frequently occurring.
            word_list: a list of words 
            n: the number of words to return
            returns: a list of n most frequently occurring words ordered from most
                     frequently to least frequently occurring
        """
        word_list = self.counts
        sort = sorted(word_list, key = word_list.get, reverse = True)
        self.top_words = sort[:n]   

    def get_top_n_values(self, n = 25):
        """
        Word list is a dictionary of words and the number of times  they appear
        """
        word_list = self.counts
        top_words = dict(sorted(word_list.iteritems(), key=operator.itemgetter(1), reverse=True)[:n])
        top_values = top_words.values()
        top_values = sorted(top_values, reverse = True)
        self.top_values = top_values

    def tenmill_year(self):
        """For making graph of password years thatre most common"""
        passes = self.the_list
        years = {}
        for password in passes:
            numbs = map(int, re.findall('\d+', password))
            for num in numbs:
                if num > 1965 and num < 2016:
                    years[num] = years.get(num, 0) + 1
        keys, values = years.keys(), years.values()
        newkeys = [str(x) for x in keys]
        self.years = newkeys
        self.yearvalues = values
        #print newkeys
        #print values

class English(object):
    """Deals with the English dictionary """

    def __init__(self):
        """Creates a list of all of the entries in a text file"""
        text = open('/usr/share/dict/american-english', 'r')
        words = text.readlines()
        english = []

        for line in words:
            english.append(line.translate(None, '\n'))

        self.english = english

    def compare_to_english_string(self, password):
        english = self.english
        matching = [word for word in english if word in password and len(word) > 2]
        if matching == []:
            self.contains = "Does not contain English"
        else:
            self.contains = 'Contains following English: ' + str(matching)

    def compare_to_english_list(self, password):
        english = self.english
        matching = [word for word in english if word in password and len(word) > 2]
        if matching == []:
            self.contains_list = matching
        else:
            self.contains_list = matching


def word_is_pass(words, passwords):
    """ Returns the number of times the strings in your password appear as passwords in the password data set
    words is the list of english words contained within the passwords: 
    english.contains_list("your password") where english = English()
    passwords is the dictonary of passwords as keys and values being the number of times they appear:
    password.counts where password = File('password', "10-million-combos.txt", 1)
    """
    counts = []
    for word in words:
        if word in passwords:
            counts.append(passwords[word])
        else:
            counts.append(0)
    return counts


#print word_is_pass(english.contains_list, passwords.counts)

if __name__ == '__main__':
    passwords = File('passwords', "10-million-combos.txt", 1)
    usernames = File('usernames',  "10-million-combos.txt", 0)
    passwords.counts_dictionary()
    passwords.distance_from_list("hello")
    passwords.get_top_n_words()
    passwords.get_top_n_values()
    passwords.tenmill_year()

    english = English()
    english.compare_to_english_string("hello")
    english.compare_to_english_list("hello")



""" The Grave Yard """

    # def get_top_n_words(self, n = 25):
    #     """ Takes a list of words as input and returns a list of the n most frequently
    #         occurring words ordered from most to least frequently occurring.
    #         word_list: a list of words 
    #         n: the number of words to return
    #         returns: a list of n most frequently occurring words ordered from most
    #                  frequently to least frequently occurring
    #     """
    #     word_list = self.the_list
    #     sort = sorted(word_list, key = word_list.get, reverse = True)
    #     return sort[:n]   

# def get_year(password):
#     """Sees if there's a year in your password, and tells you how common it is
#         to have that year in a password"""
#     numbs = map(int, re.findall('\d+', password))

#     for num in numbs:
#         if num > 1900 and num < 2020:
#             return "Year included is " + str(num)
#     return "No year present"

# def occurances_of_words_in_pass(words_in_pass, pass_dict):
#     """ Takes a list of words contained in the passwords and returns a list of tuples
#         words_in_pass: list of strings
#         returns: list of tuples
#      """
#     word_and_occurances = []
#     for word in words_in_pass:
#         if word in pass_dict:
#             word_and_occurances.append((word, pass_dict[word]))
#         else:
#             word_and_occurances.append((word, 0))
#     return word_and_occurances

# def get_percent(num_passwords, top_values):
#     percents = []
#     for value in top_values:
#         percents.append((float(value)/num_passwords)*100)
#     return percents


# def frequency(pass_dict, matching):
#     freq = []
#     for word in matching:
#         if word in pass_dict:
#             freq.append((float(pass_dict[word])/9997986)*100)
#         else:
#             freq.append(0)
#     freq = zip(matching, freq)
#     return freq

# def num_passwords(file_name):
#     """ returns number of passwords"""
#     f = open(file_name,'r')
#     words = []
#     lines = f.readlines()
#     for line in lines:
#         words_in_line = string.split(line)
#         if len(words_in_line) == 1:
#             pass
#         else:
#             words.append(words_in_line[1])
#     return len(words) #9997986


# def compare_to_english(password, english):
#     """ Compare input password to english words and see if password is english words
#         or if it contains one
#         Returns string stating "Not English" or "Contains English"
#         >>> compare_to_english('friend')
#         'Contains English'
#     """

#     matching = [word for word in english if word in password and len(word) > 2]
#     if matching == []:
#         return "Does not contain English"
#     else:
#         return 'Contains following English: ' + str(matching)


# def find_distance(s1, s2):
#     dis = distance(s1, s2)
#     return dis

# def passwords_as_list(pass_dict):
#     """ Turns dictionary of passwords keys to a list 
#     returns a list of passwords"""
#     pass_list = list(pass_dict.keys())
#     return pass_list

# def graph_percents(top_words, percents, top_values):
#     y_pos = np.arange(len(top_words))
#     performance = 3 + 10 * np.random.rand(len(top_words))

#     plt.barh(y_pos, percents)
#     plt.yticks(y_pos, top_words)
#     plt.xlabel('Percentage')
#     plt.title('Percent Apperance of Common Passwords')

#     #plt.show()
#     plt.savefig("percentsofcommon.gif")


# def english_words():
#     f = open('/usr/share/dict/american-english', 'r')
#     words = f.readlines()
#     english = []

#     for line in words:
#         english.append(line.translate(None, '\n'))

#     return english


# def get_word_list(file_name):
#     """ Creates a dictionary of passwords and their counts.
#     file_name: name of txt file
#     returns: dictionary
#     """
#     f = open(file_name,'r')
#     count = dict()
#     lines = f.readlines()

#     for line in lines:
#         words_in_line = string.split(line)
#         if len(words_in_line) == 1 or words_in_line == []:
#             pass
#         elif words_in_line[1] not in count:
#             count[words_in_line[1]] = 1
#         else:
#             count[words_in_line[1]] += 1        
#     return count


# def get_usernames(file_name):
#     """ Creates a dictionary of usernames and their passwords.
#     file_name: name of txt file
#     returns: dictionary
#     """
#     f = open(file_name, 'r')
#     d = dict()
#     lines = f.readlines()

#     for line in lines:
#         words_in_line = string.split(line)
#         if len(words_in_line) == 1 or words_in_line == []:
#             pass
#         elif words_in_line[0] not in d:
#             d[words_in_line[0]] = [words_in_line[1]]
#         else:
#             d[words_in_line[0]].append(words_in_line[1]) 
#     return d

# def distance_from_passwords(your_word, passwords):
#     """ 
#     your_word: string that is your password
#     passwordsr: list of passwords, all dublicates included 
#     Uses Levenshtein distance to find the number of characters off a password
#     is from passwords and returns a list where 0 is the number of words that are 0
#     off, distance[1] is words that are 1 of etc
#     returns list """ 
#     distance = [0]*10
#     for word in passwords:
#         dis = find_distance(your_word, word)
#         if dis < 10:
#             distance[dis] += 1
#     return distance

        # def total_password_list(file_name):
        # """ return the dictionary as a list where every password is its own entry"""
        # f = open(file_name, 'r')
        # total_pass_list = []
        # lines = f.readlines()
        # for line  in lines:
        #     words_in_line = string.split(line)
        #     if len(words_in_line) == 1 or words_in_line == []:
        #         pass
        #     else:
        #         total_pass_list.append(words_in_line[1])
        # return total_pass_list    

