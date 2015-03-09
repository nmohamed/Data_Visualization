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
    	button_common = Button(self.button_frame, text = 'Look at Common Data', 
    							command = self.add_percentscommonimage)
    	button_quit = Button(self.button_frame, text = 'Quit', command = quit)
        button_yourpw = Button(self.button_frame, text = 'Find Info About Your Password',
                                command = self.add_entry)
        button_quit.pack(fill = X)
    	button_common.pack(fill = X)
        button_yourpw.pack(fill = X)


    def add_entry(self):
        ############################
        def get_info():
            """Get password info for password you Input
                """
            #self.information_frame.pack_forget()
            #self.information_frame = Frame(self.master)
            password = entry.get()
            english = english_words()
            Label(self.information_frame, text = 'Your password: ' + password).pack()
            Label(self.information_frame, text = compare_to_english(password, english)).pack()
            Label(self.information_frame, text = get_year(password)).pack()
            password_list = total_password_list('10-million-combos.txt')
            distances = distance_from_passwords(password, password_list)
            graph_distances(distances)
            MakeWindow.add_distancesimage(self)
<<<<<<< HEAD


        Label(self.button_frame, text = "Input Password:").pack(fill = X)
        entry = Entry(self.button_frame)
        entry.pack(fill = X)
        button_getinfo = Button(self.button_frame, text = 'Get info', command = get_info)
        button_getinfo.pack(fill = X)


=======
>>>>>>> bea5b2f1f171b3aff9469c1298ab8a2c3277b2f2
        def get_Levenshtein():
            """ your_pw: your password that you input
                passwords: dict of passwords with values as Levenschtein dist
                Graphs words with smaller lev dist in center and bigger ones further"""
            from bokeh.plotting import figure, output_file, show, ColumnDataSource
            from bokeh.models import HoverTool
            from random import randint, uniform
            from math import cos, sin

            your_pw = entry.get()
            total_passwords = total_password_list('test_data.txt')
            passwords = distance_from_passwords_dictionary(your_pw, total_passwords)
            
            output_file("lev_graph.html")
            #hover.tooltips = []
            plot = figure(width = 700, height = 700, title = 'Levenshtein distance: ' + your_pw,
                          tools = "resize, hover")
            hover_pass = []
            hover_lev = []
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
                
            source = ColumnDataSource(data= dict(hover_pass = hover_pass, hover_lev = hover_lev))
            plot.circle(x, y, alpha = .5, source = source)
            plot.select(dict(type = HoverTool)).tooltips = {"Levenshtein Distance":"@hover_lev",
                                                            "Password":"@hover_pass"}
            show(plot)   
        ##################
        Label(self.button_frame, text = "Input Password:").pack()
        entry = Entry(self.button_frame)
        entry.pack()
        button_getLevenshtein = Button(self.button_frame, text = 'Get Levenshtein distances', command = get_Levenshtein).pack()
        button_getinfo = Button(self.button_frame, text = 'Get info', command = get_info).pack()
<<<<<<< HEAD
        #############################
=======
>>>>>>> bea5b2f1f171b3aff9469c1298ab8a2c3277b2f2

###################################################functions to do stuff
    def add_percentscommonimage(self):
        image = Image.open('percentsofcommon.png')
        photo = ImageTk.PhotoImage(image)
        label = Label(image = photo)
        label.image = photo #keep a reference!
        label.pack()


    def add_distancesimage(self):
        image = Image.open('distancefrompass.png')
        photo = ImageTk.PhotoImage(image)
        label = Label(image = photo)
        label.image = photo #keep a reference!
        label.pack()


def main():
    root = Tk()
    ex = MakeWindow(root)
    root.mainloop()  



if __name__ == '__main__':
    main()  
    #pw = 'abc123'
    #total_passwords = total_password_list('test_data.txt')
    #graphing_circles(pw, distance_from_passwords_dictionary(pw, total_passwords))
