from bokeh.plotting import *
from datafunctions import english_words, get_word_list

def compare_to_english(password, english):
    matching = [word for word in english if word in password and len(word) > 2]
    if matching == []:
        return matching
    else:
        return matching

def word_is_pass(words, passwords):
    counts = []
    for word in words:
        if word in passwords:
            counts.append(passwords[word])
        else:
            counts.append(0)
    return counts

english = english_words()
passwords_and_counts = get_word_list('10-million-combos.txt')
words = compare_to_english('hello', english)
counts =  word_is_pass(words, passwords_and_counts)
x0 = [0, 0, 0, 0, 0, 0, 0, 0]
x =  counts
x_range_end = max(counts) + max(counts)*.1

output_file("categorical.html", title="categorical.py example")

p1 = figure(title="Dot Plot", tools="resize,hover,save", y_range=words, x_range=[0,x_range_end])

p1.segment(x0, words, x, words, line_width=2, line_color="green", )
p1.circle(x, words, size=15, fill_color="orange", line_color="green", line_width=3, )

show(p1)


