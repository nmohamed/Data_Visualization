"""
Data Visualization Project
Lucy Wilcox & Nora Mohamed
Software Design SP2015
    dot_graph.py includes the class DotGraph that creates the different types of
    dot graphs in the GUI. Commented lines at the bottom are used to create the .html
    files that main.py opens
"""
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool, Range1d
from datafunctions import *

class DotGraph(object):
    """Used for making Bokeh dot graphs. The y axis is of strings, x axis is numbers"""

    def __init__(self, file_name, titles):
        """ Initializes the class.
                file_name: String, name of the file to save graph to
                titles: String, title of graph"""
        self.titles = titles
        self.p1 = figure(title= titles, tools="resize, wheel_zoom, reset, save",)
                         #y_range= y_value, x_range=[0, 1.1*x_length])
        output_file(file_name, title= titles)
        self.x0 = [0] * 50
        
        self.passwords = File("10-million-combos.txt", 1)
        self.passwords.counts_dictionary()
        #passwords.distance_from_list(password)


    def do_type_english(self, your_password):
        """ Makes a graph of number of occurences of your password and english words
            in your password in the dataset"""
        english = English()

        english.compare_to_english_list(your_password)
        words = english.contains_list
        counts = word_is_pass(words, self.passwords.counts)

        self.makegraph(counts, words, max(counts), len(words))


    def do_type_top25(self):
        """ Makes graph of number of occurences of the 25 most common passwords"""
        self.passwords.get_top_n_values()
        self.passwords.get_top_n_words()

        self.makegraph(self.passwords.top_values, self.passwords.top_words,
                       max(self.passwords.top_values), len(self.passwords.top_words))


    def do_type_years(self):
        """ Makes graph of number of occurences of the last 49 years in passwords"""
        self.passwords.tenmill_year()
        #password.year #years
        #password.yearvalues #number for year
        self.makegraph(self.passwords.yearvalues, self.passwords.years,
                       max(self.passwords.yearvalues), len(self.passwords.years))


    def do_type_usernames(self):
        """ Makes graph of number of occurences of the 25 most common usernames"""
        self.usernames = File('10-million-combos.txt', 0)
        self.usernames.counts_dictionary()
        self.usernames.get_top_n_values()
        self.usernames.get_top_n_words()

        self.makegraph(self.usernames.top_values, self.usernames.top_words,
                       max(self.usernames.top_values), len(self.usernames.top_words))


    def makegraph(self, x_value, y_value, x_length, y_length):
        """ Main function for creating dot graphs. Graph will be equivalent of a bar
            graph on its side.
                x_value: List of integers corresponding to number of occurences of y_values
                y_value: List of strings (e.g., list of words or y)
                x_length: Int, largest int in x_value list
                y_value: Int, length of y_value list"""
        self.p1.y_range = Range1d(start = 0, end = y_length)
        self.p1.x_range = Range1d(start = 0, end = 1.1*x_length)
        self.p1 = figure(title = self.titles, tools="resize, wheel_zoom, reset, save",
                         y_range= y_value, x_range=[0, 1.1*x_length])

        self.p1.segment(self.x0, y_value, x_value, y_value, line_width=2, line_color="#ff0033")
        self.p1.circle(x_value, y_value, size=15, fill_color="#00ffb8", line_color="#ff0033", 
                        line_width=3)


    def make_axis_label(self, x, y):
        """ Creates a label for the x and y axises.
                x: String for x axis title
                y: String for y axis title"""
        self.p1.xaxis.axis_label = x
        self.p1.yaxis.axis_label = y

if __name__ == '__main__':
    pass
        #Generates 25 Most Common Passwords graph
    # g2 = DotGraph('top25-common.html', '25 Most Common Passwords')
    # g2.do_type_top25()
    # g2.make_axis_label('Appearances out of 10 million', 'Most common passwords')
    # show(g2.p1)
        #Generates Mosts Common Years graph
    # g3 = DotGraph('years-common.html', 'Most Common Years in Passwords')
    # g3.do_type_years()
    # g3.make_axis_label('Appearances out of 10 million', 'Years')
    # show(g3.p1)
        #Generates 25 Most Common Usernames graph
    # g4 = DotGraph('usernames-common.html', '25 Most Common Usernames')
    # g4.do_type_usernames()
    # g4.make_axis_label('Appearances out of 10 million', 'Most common usernames')
    # show(g4.p1)