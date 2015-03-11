"""
Data Visualization Project
Lucy Wilcox & Nora Mohamed
Software Design SP2015
"""

from Tkinter import *
from PIL import Image, ImageTk
from datafunctions import english_words, compare_to_english
from datafunctions import distance_from_passwords, graph_distances, total_password_list
from datafunctions import distance_from_passwords_dictionary
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool
from random import randint, uniform
from math import cos, sin
from dot_graph import *

class MakeWindow(Frame):
  
    def __init__(self, master):
        self.master = master
        self.button_frame = Frame(self.master, width = 400, height = 400, bg='', colormap = 'new')
        self.information_frame = Frame(self.master)
        self.add_button()

        self.button_frame.pack(fill = X)
        self.information_frame.pack()

    def add_button(self):
<<<<<<< HEAD
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



        Label(self.button_frame, text = "Input Password:").pack(fill = X)
        entry = Entry(self.button_frame)
        entry.pack(fill = X)
        button_getinfo = Button(self.button_frame, text = 'Get info', command = get_info)
        button_getinfo.pack(fill = X)


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

###################################################functions to do stuff
    def add_percentscommonimage(self):
        image = Image.open('percentsofcommon.png')
=======
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
        Button(self.button_frame, text = 'Get Appearances of English Words in Your Password Out of 10 Million', 
            command = lambda:self.get_english()).pack()

    def get_english(self):
        """ shows graph of number of times all the english words in your password appear in
            10 million list"""
        your_pw = entry_pw.get()
        g = DotGraph('english', your_pw, 
            'englishinyourpw-to-10mill.html', 'How Common English Words In Your Password Are')
        g.make_label('Number of appearances in all passwords', 'English words in your password')
        show(g.p1)

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
>>>>>>> a4534be39448d699582e8835af70fd23857617be
        photo = ImageTk.PhotoImage(image)
        label = Label(image = photo)
        label.image = photo #keep a reference!
        label.pack()

if __name__ == '__main__':
    root = Tk()
    ex = MakeWindow(root)
    root.mainloop()  
