from swampy.Gui import *
from Tkinter import *
import PIL
from PIL import Image, ImageTK
import string




g = Gui()
g.title('Gui')

class Canvas():
    """ """
    def __init__(self):
        canvas = g.ca(width = 500, height = 200)

class MakeWindow():
    """ """
    def __init__(self):
        self.canvas = g.ca(width = 500, height = 200, bg = 'white')


    def add_button(self, text, the_command = None):
        b = g.bu(text, command = the_command)
        b.pack()

    def makeentry(self, caption, width=None, **options):
        v = StringVar()
        Label(g, text=caption).pack(side=LEFT)
        entry = Entry(g, textvariable = v)
        if width:
            entry.config(width=width)
        entry.pack(side=LEFT)
        v.set("")
        text = entry.get()
        s = v.get()
        v.set(text)
        print s
        return entry

    def text_entry(self):
        text = g.te(width = 100, height = 5)
        password = MakeWindow.makeentry(MakeWindow(), "Password:", 10)
        s = password.get()
        print s

def show_photo():

        #image = Image.open("percentsofcommon.png")
        #photo = ImageTk.PhotoImage(image)
        root = Tkinter.Tk()
        #w = Tkinter.Lable(master)
        photo = PhotoImage( file= "earth.gif")
        lable = Label(image = photo).pack()

        #w.photo = photo
        #w.pack()
        #w = Label(master, image=photo)
        #w.photo = photo
        #w.pack()

def common_passwords_percents():
    print get_top_n_words(counts, 25)


    # def set_option(self, color):
    #   mb.config(text = option)
    #   print color
window = MakeWindow()
#window.setup()
#window.add_button("Test", show_photo)
window.add_button("Test", MakeWindow.text_entry(window))



# c = Canvas()
# g.la('Select a option:')
# options = ['LOOK AT COMMON DATA','COMPARE YOUR DATA']
# mb = g.mb(text = options[0])
# for option in options:
#   g.mi(mb, text = option, command = Callable(set_option, option))

# text = g.te(width = 100, height = 5)
# button = g.bu(text = "LOOK AT COMMON DATA", command = sel)
# button2 = g.bu(text = "Common Numbers")
# label = g.la(text = "press the button")

g.mainloop()