from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool, Range1d
from datafunctions import *


class DotGraph(object):
    """Used for making Bokeh dot graphs. The y axis is strings, x axis is numbers"""
    def __init__(self, file_name, titles):
        self.titles = titles
        self.p1 = figure(title= titles, tools="resize, wheel_zoom, reset, save",)
                         #y_range= y_value, x_range=[0, 1.1*x_length])
        output_file(file_name, title= titles)
        self.x0 = [0] * 50
        
        self.passwords = File('passwords', "10-million-combos.txt", 1)
        #passwords.distance_from_list(password)

    def do_type_english(self, your_password):
        """ Makes a graph """
        self.passwords.counts_dictionary()
        english = English()

        english.compare_to_english_list(your_password)
        words = english.contains_list
        counts = word_is_pass(words, self.passwords.counts)

        self.makegraph(counts, words, max(counts), len(words))

    def do_type_top25(self):
        self.passwords.get_top_n_values()
        self.passwords.get_top_n_words()

        self.makegraph(self.passwords.top_values, self.passwords.top_words,
                       max(self.passwords.top_values), len(self.passwords.top_words))

    def do_type_years(self):
        self.passwords.tenmill_year()
        #password.year #years
        #password.yearvalues #number for year
        self.makegraph(self.passwords.yearvalues, self.passwords.years,
                       max(self.passwords.yearvalues), len(self.passwords.years))

    def makegraph(self, x_value, y_value, x_length, y_length):
        """y_value is a list of strings, x_value is list of integers"""
        self.p1.y_range = Range1d(start = 0, end = y_length)
        self.p1.x_range = Range1d(start = 0, end = 1.1*x_length)
        self.p1 = figure(title = self.titles, tools="resize, wheel_zoom, reset, save",
                         y_range= y_value, x_range=[0, 1.1*x_length])

        self.p1.segment(self.x0, y_value, x_value, y_value, line_width=2, line_color="#0085ff")
        self.p1.circle(x_value, y_value, size=15, fill_color="#fff400", line_color="#0085ff", 
                        line_width=3)

    def make_axis_label(self, x, y):
        self.p1.xaxis.axis_label = x#'Number of appearances in all passwords'
        self.p1.yaxis.axis_label = y#'English words in your password'


#g = DotGraph('englishinyourpw-to-10mill2.html', 'How Common English Words In Your Password Are')
#g.do_type_english('goldentable')
#g.make_axis_label('Number of appearances in all passwords', 'English words in your password')
#show(g.p1)

# g2 = DotGraph('top25-common.html', '25 Most Common Passwords')
# g2.do_type_top25()
# g2.make_axis_label('Appearances out of 10 million', 'Most common passwords')
# show(g2.p1)

g3 = DotGraph('years-common.html', 'Most Common Years in Passwords')
g3.do_type_years()
g3.make_axis_label('Appearances out of 10 million', 'Years')
show(g3.p1)