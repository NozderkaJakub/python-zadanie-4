from tkinter import *

class Window():

    def napisz(self):
        print('dupa')

    def quit(self):
        self.quit()

    def __init__(self):
        window = Tk()
        window.title("Wilk i łowce")
        window.geometry('1000x800')
        menu = Menu(window)
        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label='Open')
        file_menu.add_separator()
        file_menu.add_command(label='Save')
        file_menu.add_separator()
        file_menu.add_command(label='Quit', command=quit)
        settings_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label='File', menu=file_menu)
        menu.add_cascade(label='Settings', menu=settings_menu)
        window.config(menu=menu)
        
        window.mainloop()