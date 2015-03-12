"""
Data Visualization Project
Lucy Wilcox & Nora Mohamed
Software Design SP2015
    datafunctions.py includes the classes File and English, which are used for
    parsing your data. English is used for comparing your password to english,
    and File will deal with the dataset.
"""

import string
import heapq
import operator
import numpy as np
import matplotlib.pyplot as plt
from Levenshtein import distance
import re

class File(object):
    """Deals with our 10-million-combos dataset, and other datasets in a similar format
    (namely our test data set, which we sometimes use because it is still really big and
    faster to move through)."""

    def __init__(self, file_name, column):
        """ Opens text file and creates its text and a column which defines if it is a password
            or username data set
                file_name: txt file that you are reading the data from, probably 
                    10-million-combos.txt
                column: 0 refers to usernames, 1 refers to passwords"""
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
                sets a: dictionary"""
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
        """ Sets an int representing lenth of file"""
        the_list = self.the_list
        self.length = len(the_list) #9997986


    def distance_from_list(self, your_word):
        """ Uses Levenshtein distance to find the number of characters off a password
            is from passwords and returns a dictionary where keys are passworeds and 
            values = dist
                your_word: string that is your password
                sets a :dictionary"""
        dist = {}
        for word in self.the_list:
            if word in dist:
                pass
            else:
                dist[word] = distance(your_word, word)
        self.dist = dist


    def get_top_n_words(self, n = 25):
        """ Creates a list of n most frequently occurring words ordered from most
            frequently to least frequently occurring
                n: the number of words to return"""
        word_list = self.counts
        sort = sorted(word_list, key = word_list.get, reverse = True)
        self.top_words = sort[:n]   


    def get_top_n_values(self, n = 25):
        """ Creates a list of the number of times each word occures in the provided dictionary
                n: the top number to be returned"""
        word_list = self.counts
        top_words = dict(sorted(word_list.iteritems(), key=operator.itemgetter(1), reverse=True)[:n])
        top_values = top_words.values()
        top_values = sorted(top_values, reverse = True)
        self.top_values = top_values


    def tenmill_year(self):
        """ For making graph of password years that are most common
            Creates attributes of years which is the years and yearvalues which 
            is the number of times each year comes up, both of these are lists"""
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


class English(object):
    """ Deals with the English dictionary inside of Linux"""

    def __init__(self):
        """ Creates a list of all of the entries in a text file"""
        text = open('/usr/share/dict/american-english', 'r')
        words = text.readlines()
        english = []

        for line in words:
            english.append(line.translate(None, '\n'))

        self.english = english


    def compare_to_english_list(self, password):
        """ Takes a password (a string) and finds a list of english words that are within the password
            Sets attribute which is a list of strings"""
        english = self.english
        matching = [word for word in english if word in password and len(word) > 2]
        self.contains_list = matching


def word_is_pass(words, passwords):
    """ Returns the number of times the strings in your password appear as passwords in the password data set
        words is the list of english words contained within the passwords: 
        english.contains_list("your password") where english = English()
        passwords is the dictonary of passwords as keys and values being the number of times they appear:
        password.counts where password = File('password', "10-million-combos.txt", 1)"""
    counts = []
    for word in words:
        if word in passwords:
            counts.append(passwords[word])
        else:
            counts.append(0)
    return counts