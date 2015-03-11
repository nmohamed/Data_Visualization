from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool, Range1d
from datafunctions import return_objects

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
        def compare_to_english(password, english):
            matching = [word for word in english if word in password and len(word) > 2]
            if matching == []:
                return matching
            else:
                return matching

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
            ####################################################
        if self.typegraph is 'english':

            #english = english_words()
            #passwords_and_counts = get_word_list('10-million-combos.txt')
            #words = compare_to_english(self.password, english)
            passwords = return_objects("hello")
            print type(passwords)
            english = English()
            words = english.compare_to_english(self.password)
            print words
            counts =  word_is_pass(words, passwords_and_counts)

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