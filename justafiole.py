#import os
from tkinter import *
import time


def gifoeffnen(name,gifnr) :

    giffenster = Tk()

    label = Label()
    label.pack()

    counter = 0

    while counter < gifnr :

        photo = PhotoImage(file=name, format="gif -index " + str(counter))
        label.config(image = photo)
        time.sleep(0.01)
        giffenster.update()
        counter += 1

        if counter > gifnr:
            # giffenster.destroy()
            print(gifnr)
    giffenster.mainloop()

gifoeffnen("bas0.gif", 25)
