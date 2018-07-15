from tkinter import *

def context_menu(event, menu, listBox): #2345
    widget = event.widget
    index = widget.nearest(event.y)
    listBox.activate(index)
    _, yoffset, _, height = widget.bbox(index)
    if event.y > height + yoffset + 5: # XXX 5 is a niceness factor :)
        # Outside of widget.
        return
    item = widget.get(index)
    print("Do something with", index, item)
    menu.post(event.x_root, event.y_root)

def removeClient(): #2345
    pass
    print('CLICKED')
root = Tk()
menu = Menu(self.root, tearoff=0) #5432
menu.add_command(label='remove bot', command=removeClient)
listbox = Listbox()
listbox.insert(0, *range(1, 10, 2))
listbox.bind('<3>', lambda e: context_menu(e, menu))       #4352
listbox.pack()
listbox.activate(1)
root.mainloop()