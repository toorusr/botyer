from tkinter import *
from tkinter.ttk import *

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title('TEST COMPILE')
        self.root.geometry('700x500')
        self.root.resizable(0, 0)
        self.frame = Frame(self.root).place(x=0, y=0, height=500, width=700)
        image = PhotoImage(file=' base.gif')
        label = Label(self.frame, image=image).place(x='-1', y='-1', width=700, height=500)

        self.root.mainloop()
App().__init__()
