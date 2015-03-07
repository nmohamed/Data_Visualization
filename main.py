"""
Data Visualization Project
Lucy Wilcox & Nora Mohamed
Software Design SP2015
"""

from Tkinter import *
from PIL import Image, ImageTk
from datafunctions import english_words, compare_to_english, get_year

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
        button_yourpw.pack()

    def add_entry(self):
        #s
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

        Label(self.button_frame, text = "Input Password:").pack()
        entry = Entry(self.button_frame)
        entry.pack()
        button_getinfo = Button(self.button_frame, text = 'Get info', command = get_info)
        button_getinfo.pack()

###################################################functions to do stuff
    def add_percentscommonimage(self):
        image = Image.open('percentsofcommon.png')
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