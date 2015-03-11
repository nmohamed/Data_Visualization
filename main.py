"""
Data Visualization Project
Lucy Wilcox & Nora Mohamed
Software Design SP2015
"""

from Tkinter import *
from PIL import Image, ImageTk
from datafunctions import english_words, compare_to_english, get_year
from datafunctions import distance_from_passwords, graph_distances, total_password_list
from datafunctions import distance_from_passwords_dictionary
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool
from random import randint, uniform
from math import cos, sin

class MakeWindow(Frame):
  
    def __init__(self, master):
        self.master = master
        self.button_frame = Frame(self.master, width = 400, height = 400, bg='', colormap = 'new')
        self.information_frame = Frame(self.master)
        self.add_button()

        self.button_frame.pack(fill = X)
        self.information_frame.pack()

######################################################elements of tkinter
    def add_button(self):
        Button(self.button_frame, text = 'Quit', command = quit).pack()

        Label(self.button_frame, text = "Look at Graphs on Common Data:").pack()
    	Button(self.button_frame, text = 'Common Passwords Graph', 
    		command = lambda:self.add_image('percentsofcommon.png')).pack()

        Label(self.button_frame, text = 'Enter a Password Below to Find Information:').pack()
        global entry_pw 
        entry_pw = Entry(self.button_frame)
        entry_pw.pack()
        Button(self.button_frame, text = 'Get Levenshtein distances', 
            command = lambda:self.get_Levenshtein()).pack()
        ##################

    def get_Levenshtein(self):
        """ your_pw: your password that you input
            passwords: dict of passwords with values as Levenschtein dist
            Graphs words with smaller lev dist in center and bigger ones further"""

        your_pw = entry_pw.get()
        total_passwords = total_password_list('twenty_pw.txt')
        passwords = distance_from_passwords_dictionary(your_pw, total_passwords)
        
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
        image = Image.open(image_name) #percentsofcommon.png
        photo = ImageTk.PhotoImage(image)
        label = Label(image = photo)
        label.image = photo #keep a reference!
        label.pack()

if __name__ == '__main__':
    root = Tk()
    ex = MakeWindow(root)
    root.mainloop()  
    infolabel = None