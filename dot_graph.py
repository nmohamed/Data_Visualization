from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool, Range1d
from datafunctions import *


class DotGraph(object):
    """Used for making Bokeh dot graphs"""
    def __init__(self, typegraph, password, file_name, titles):

        self.p1 = figure(title= titles, tools="resize, wheel_zoom, reset, save",)
                         #y_range= y_value, x_range=[0, 1.1*x_length])
        output_file(file_name, title= titles)
        self.x0 = [0, 0, 0, 0, 0, 0, 0, 0]
        self.typegraph = typegraph
        self.password = password
        self.do_type()

    def do_type(self):

        if self.typegraph is 'english':

            password = self.password
            passwords = File('passwords', "10-million-combos.txt", 1)
            passwords.counts_dictionary()
            passwords.distance_from_list(password)
            passwords.get_top_n_values()
            passwords.get_top_n_words()

            english = English()

            english.compare_to_english_list(password)
            words = english.contains_list
            counts = word_is_pass(words, passwords.counts)

            self.makegraph(words, counts, max(counts), len(words))

        if self.typegraph is 'top25':
            pass
            self.makegraph()

    def makegraph(self, y_value, x_value, x_length, y_length):
        """y_value is a list of y values, x_value is list of x values"""
        self.p1.y_range = Range1d(start = 0, end = y_length)
        self.p1.x_range = Range1d(start = 0, end = 1.1*x_length)
        self.p1 = figure(title="Dot Plot", tools="resize, wheel_zoom, reset, save",
                         y_range= y_value, x_range=[0, 1.1*x_length])

        self.p1.segment(self.x0, y_value, x_value, y_value, line_width=2, line_color="green")
        self.p1.circle(x_value, y_value, size=15, fill_color="orange", line_color="green", 
                        line_width=3)

    def make_label(self, x, y):
        self.p1.xaxis.axis_label = x#'Number of appearances in all passwords'
        self.p1.yaxis.axis_label = y#'English words in your password'


g = DotGraph('english', 'friendly', 'englishinyourpw-to-10mill.html', 'How Common English Words In Your Password Are')
g.make_label('Number of appearances in all passwords', 'English words in your password')
show(g.p1)