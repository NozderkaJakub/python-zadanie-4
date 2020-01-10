from tkinter import *
from simulation import Simulation
import configuration as cfg
from printer import Printer

class Window():

    def quit(self):
        self.window.destroy()

    def simulate(self):
        if self.turn <= self.simulation.turns:
            self.simulation.step()
            self.turn += 1
        else:
            print('Osiągnięto końcową liczbę rund')

    def reset(self):
        self.simulation = Simulation(flock_size=cfg.config['sheep'], sheep_move_dist=cfg.config['sheep_move_dist'],
                            wolf_move_dist=cfg.config['wolf_move_dist'], init_pos_limit=cfg.config['init_pos_limit'],
                            turns=cfg.config['rounds'])
        self.turn = 0

    def __init__(self):
        self.window = Tk()
        self.simulation = Simulation(flock_size=cfg.config['sheep'], sheep_move_dist=cfg.config['sheep_move_dist'],
                            wolf_move_dist=cfg.config['wolf_move_dist'], init_pos_limit=cfg.config['init_pos_limit'],
                            turns=cfg.config['rounds'])
        
        self.window.title('Wilk i łowce')
        self.window.geometry('1000x800')
        self.turn = 0
        menu = Menu(self.window)
        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label='Open')
        file_menu.add_separator()
        file_menu.add_command(label='Save')
        file_menu.add_separator()
        file_menu.add_command(label='Quit', command=self.quit)
        settings_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label='File', menu=file_menu)
        menu.add_cascade(label='Settings', menu=settings_menu)
        self.window.config(menu=menu)
        step_button = Button(self.window, text='Step', command=self.simulate)
        step_button.pack()
        reset_button = Button(self.window, text='Reset', command=self.reset)
        reset_button.pack()
        self.window.mainloop()