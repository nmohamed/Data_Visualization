"""
Data Visualization Project
Lucy Wilcox & Nora Mohamed
Software Design SP2015
"""

from Tkinter import *
from PIL import Image, ImageTk

class MakeWindow(Frame):
  
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.add_button()
    	
    def add_percentscommonimage(self):
    	image = Image.open('percentsofcommon.png')
    	photo = ImageTk.PhotoImage(image)
    	label = Label(image = photo)
    	label.image = photo #keep a reference!
    	label.pack()

    def yourpasswordinfo(self):
        label = Label(text = 'Getting info about your stuff')
        label.pack()

    def add_button(self):
    	button_common = Button(text = 'Look at Common Data', 
    							command = self.add_percentscommonimage)
        button_yourpw = Button(text = 'Find Info About Your Password',
                                command = self.yourpasswordinfo)
    	button_quit = Button(text = 'Quit', command = quit)
        button_quit.pack()
    	button_common.pack()
        button_yourpw.pack()


def main():
    root = Tk()
    ex = MakeWindow(root)
    root.mainloop()  

if __name__ == '__main__':
    main()  
