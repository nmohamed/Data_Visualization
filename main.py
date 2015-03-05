"""
Data Visualization Project
Lucy Wilcox & Nora Mohamed
Software Design SP2015
"""

from Tkinter import *
from PIL import Image, ImageTk
from datafunctions import english_words, compare_to_english

class MakeWindow(Frame):
  
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.add_button()

######################################################elements of tkinter
    def add_button(self):
    	button_common = Button(text = 'Look at Common Data', 
    							command = self.add_percentscommonimage)
    	button_quit = Button(text = 'Quit', command = quit)
        button_yourpw = Button(text = 'Find Info About Your Password',
                                command = self.add_entry)
        button_quit.pack()
    	button_common.pack()
        button_yourpw.pack()

    def add_entry(self):
        def get_info():
            password = entry.get()
            english = english_words()
            Label(text = 'Your password: ' + password).pack()
            Label(text = compare_to_english(password, english)).pack()

        Label(text = "Input Password:").pack()
        entry = Entry()
        entry.pack()
        button_getinfo = Button(text = 'Get info', command = get_info)
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