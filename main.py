"""
Data Visualization Project
Lucy Wilcox & Nora Mohamed
Software Design SP2015
    main.py is the runnable file. Includes the class MakeWindow that creates the GUI
"""

from Tkinter import *
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool
from datafunctions import *
from dot_graph import *
import webbrowser

class MakeWindow(Frame):
    """ Creates GUI for user interactivity. The GUI includes options for viewing graphs
        on common password information, OR lets the user input a password and see how
        the password compares to the data set of 10 million (or less, depending on the
        graph) passwords."""

    def __init__(self, master):
        """ Initializes the GUI. Creates a frame and then adds button from 
            add_button method"""
        # Initialize GUI & frame
        self.master = master
        self.button_frame = Frame(self.master, width = 400, height = 400, colormap = 'new')
        self.add_button()
        self.button_frame.pack(fill = X)
        # For calling premade bokeh graphs
        self.current_directory = 'file://' + sys.argv[0]


    def add_button(self):
        """ Creates the buttons and entry form on the GUI. There are two portions to the
            GUI: buttons to look at common information of the data set, and buttons to
            compare your input to the data set."""
        # Quit Button
        Button(self.button_frame, text = 'Quit', command = quit).pack(fill = X)
        # Common Information Buttons
        Label(self.button_frame, text = "\n\nLook at Graphs on Common Data:").pack(fill = X)
        Button(self.button_frame, text = 'Most Common Passwords Graph', 
            command = lambda:webbrowser.open(self.current_directory[0:-7] + '/top25-common.html',
                                             new = 2)).pack(fill = X)
        Button(self.button_frame, text = 'Most Common Years Graph', 
            command = lambda:webbrowser.open(self.current_directory[0:-7] + '/years-common.html',
                                             new = 2)).pack(fill = X)
        Button(self.button_frame, text = 'Most Common Usernames Graph', 
            command = lambda:webbrowser.open(self.current_directory[0:-7] + '/usernames-common.html',
                                             new = 2)).pack(fill = X)
        # Password Entry
        Label(self.button_frame, text = '\n\nEnter a Password Below to Find Information:').pack(fill = X)
        global entry_pw 
        entry_pw = Entry(self.button_frame)
        entry_pw.pack(fill = X)
        # Input Password Buttons
        Button(self.button_frame, text = 'Get Levenshtein Distances of Your Password', 
            command = lambda:self.get_Levenshtein()).pack(fill = X)
        Button(self.button_frame, text = 'Get Appearances of Password & Words in Password Out of 10 Million', 
            command = lambda:self.get_english()).pack(fill = X)


    def get_english(self):
        """ Displays graph of number of times all the english words in your password
            appear as passwords in the data set, as well as how often the password
            you input itself appears"""
        your_pw = entry_pw.get()
        g = DotGraph('englishinyourpw-to-10mill.html',
                     'How Common Words in Your Password Are')
        g.do_type_english(your_pw)
        g.make_axis_label('Number of appearances in all passwords', 
                          'English words in your password')
        show(g.p1)


    def get_Levenshtein(self):
        """ Creates graph plotting many passwords in the dataset at the Levenshtein
            distance away from the center"""
        your_pw = entry_pw.get()
        g2 = DotGraph('lev_graph.html','Levenshtein Distance: ' + your_pw)
        g2.do_type_Lev(your_pw)
        show(g2.plot)


if __name__ == '__main__':
    root = Tk()
    ex = MakeWindow(root)
    root.mainloop() 