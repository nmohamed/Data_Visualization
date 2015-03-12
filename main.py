"""
Data Visualization Project
Lucy Wilcox & Nora Mohamed
Software Design SP2015
"""

from Tkinter import *
from PIL import Image, ImageTk
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool
from random import randint, uniform
from math import cos, sin
from datafunctions import *
from dot_graph import *

class MakeWindow(Frame):
    """ Creates GUI for user interactivity. The GUI includes options for viewing graphs
        on common password information, OR lets the user input a password and see how
        the password compares to the data set of 10 million (or less, depending on the
        graph) passwords."""

    def __init__(self, master):
        """ Initializes the GUI. Creates a frame and adds the information """
        self.master = master
        self.button_frame = Frame(self.master, width = 400, height = 400, bg='', colormap = 'new')
        self.add_button()
        self.button_frame.pack(fill = X)
        self.information_frame.pack()

    def add_button(self):
        """ Creates the buttons and entry form on the GUI. There are two portions to the
            GUI: buttons to look at common information of the data set, and buttons to
            compare your input to the data set."""

        Button(self.button_frame, text = 'Quit', command = quit).pack()

        # Common information
        Label(self.button_frame, text = "Look at Graphs on Common Data:").pack()
        Button(self.button_frame, text = 'Common Passwords Graph', 
            command = lambda:self.add_image('percentsofcommon.png')).pack()

        # Information based on your input
        Label(self.button_frame, text = 'Enter a Password Below to Find Information:').pack()
        global entry_pw 
        entry_pw = Entry(self.button_frame)
        entry_pw.pack()

        Button(self.button_frame, text = 'Get Levenshtein distances', 
            command = lambda:self.get_Levenshtein()).pack()
        Button(self.button_frame, text = 'Get Appearances of English Words in Your Password Out of 10 Million', 
            command = lambda:self.get_english()).pack()

    def get_english(self):
        """ Displays graph of number of times all the english words in your password
            appear as passwords in the data set"""
        your_pw = entry_pw.get()
        g = DotGraph('english', your_pw, 'englishinyourpw-to-10mill.html',
                     'How Common English Words In Your Password Are')
        g.make_axis_label('Number of appearances in all passwords', 
                          'English words in your password')
        show(g.p1)

    def get_Levenshtein(self):
        """ Displays interactive graph plotting passwords from the data set at a 
            Levenshtein distance away from the input"""
        passwords = File('passwords', 'test_data.txt', 1) #running test data for speed, still pretty large and good
        total_passwords = passwords.the_list
        your_pw = entry_pw.get()

        #total_passwords = total_password_list('twenty_pw.txt')
        passwords = distance_from_passwords_dictionary(your_pw, passwords.dist)
        
        output_file("lev_graph.html")
        plot = figure(width = 700, height = 700, title = 'Levenshtein distance: ' + your_pw,
                      tools = "resize, hover, wheel_zoom, box_zoom, reset, save")
        hover_pass = []
        hover_lev = []
        colors = []
        x = []
        y = []
        for pw in passwords:
            #  for hovering
            hover_pass.append(pw)
            hover_lev.append(passwords[pw])
            # convert to polar
            r = passwords[pw]
            theta = randint(0, 360)
            x.append(r * cos(theta))
            y.append(r * sin(theta))
            colors.append(('#ff3366'))
        #colors = ['blue', 'purple', 'blue'][-50, 50]
        source = ColumnDataSource(data= dict(
            hover_pass = hover_pass,
            hover_lev = hover_lev,
            color = colors))
        plot.circle(x, y, alpha = .5, source = source, color = colors)
        plot.select(dict(type = HoverTool)).tooltips = {"Levenshtein Distance":"@hover_lev",
                                                        "Password":"@hover_pass"}
        show(plot)

    def add_image(self, image_name):
        """ A function for buttons to do. Takes in a string of an image name and will
            display that image in the GUI"""
        image = Image.open(image_name) #percentsofcommon.png
        photo = ImageTk.PhotoImage(image)
        label = Label(image = photo)
        label.image = photo #keep a reference!
        label.pack()

if __name__ == '__main__':
    root = Tk()
    ex = MakeWindow(root)
    root.mainloop()  