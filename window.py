from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkcolorpicker import askcolor
import json
from simulation import Simulation
import configuration as cfg
import numpy as np
from animals import Wolf


class Window():
    def choose_sheep_color(self):
        try:
            _, colorStr = askcolor(title="Choose color")
        except TclError:
            colorStr = None
        if colorStr is not None:
            cfg.config['sheep_color'] = colorStr
        self.update_animals()

    def choose_grass_color(self):
        try:
            _, colorStr = askcolor(title="Choose color")
        except TclError:
            colorStr = None
        if colorStr is not None:
            cfg.config['grass_color'] = colorStr
        self.update_animals()

    def choose_wolf_color(self):
        try:
            _, colorStr = askcolor(title="Choose color")
        except TclError:
            colorStr = None
        if colorStr is not None:
            cfg.config['wolf_color'] = colorStr
        self.update_animals()        

    def settings(self):
        win = Toplevel()
        win.wm_title("Settings")
        sheep_color = Button(win, text='Sheep color', command=self.choose_sheep_color)
        sheep_color.pack()
        sheep_color = Button(win, text='Grass color', command=self.choose_grass_color)
        sheep_color.pack()
        sheep_color = Button(win, text='Wolf color', command=self.choose_wolf_color)
        sheep_color.pack()

    def sheep_color(self):
        win = Toplevel()
        win.wm_title("Sheep color")

    def grass_color(self):
        win = Toplevel()
        win.wm_title("Grass color")

    def wolf_color(self):
        win = Toplevel()
        win.wm_title("Wolf color")

    def quit(self):
        self.window.destroy()

    def update_sheep_amount(self):
        self.sheep_amount_label.config(text='Liczba żywych owiec: ' + str(self.simulation.get_alive_sheep_amount()))

    def simulate(self):
        if self.turn <= cfg.config['rounds']-1 and len(self.simulation.flock) > 0:
            self.simulation.go_step()
            self.turn += 1
            self.update_sheep_amount()
            self.update_animals()
        elif len(self.simulation.flock) < 1:
            messagebox.showinfo('Brak owiec', 'Dodaj najpierw owce')  
        else:
            print('Osiągnięto końcową liczbę rund')

    def reset(self):
        self.simulation = Simulation(sheep_move_dist=cfg.config['sheep_move_dist'], wolf_move_dist=cfg.config['wolf_move_dist'])
        self.clear_canvas()
        self.add_wolf()
        self.turn = 0
        self.update_sheep_amount()

    def restore_game(self, result):
        self.simulation = Simulation(sheep_move_dist=result['sheep_move_dist'], wolf_move_dist=result['wolf_move_dist'])
        self.simulation.turn = result['turn_no']
        self.simulation.wolf.pos_x = result['wolf_pos'][0]
        self.simulation.wolf.pos_y = result['wolf_pos'][1]
        i = 0
        for sheep_pos in result['sheep_positions']:
            if sheep_pos is not None:
                self.simulation.flock[i].pos_x = sheep_pos[0]
                self.simulation.flock[i].pos_y = sheep_pos[1]
                self.simulation.flock[i].is_alive = True
            else:
                self.simulation.flock[i].is_alive = False
            i += 1
        self.update_sheep_amount()
            

    def file_save(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension='.txt', title='Wybierz, gdzie chcesz zapisać plik ze stanem rozgrywki')
        if f is None:
            return
        text2save = json.dumps(self.simulation.turn_result, indent=4)
        f.write(text2save)
        f.close()

    def file_open(self):
        f = filedialog.askopenfile(initialdir = './',title = 'Wybierz plik z zapisanym stanem rozgrywki')
        result = json.loads(f.read())
        self.restore_game(result)

    def clear_canvas(self):
        self.canvas.create_rectangle(0, 0, cfg.config['canvas_side'], cfg.config['canvas_side'], fill=cfg.config['grass_color'])

    def update_animals(self):
        self.clear_canvas()
        for i in range(len(self.simulation.flock)):
            if self.simulation.flock[i].is_alive:
                self.paint_animal(self.simulation.flock[i].pos_x, self.simulation.flock[i].pos_y, cfg.config['sheep_color'])
        self.paint_animal(self.simulation.wolf.pos_x, self.simulation.wolf.pos_y, cfg.config['wolf_color'])
        
    def update_wolf(self, event):
        self.clear_canvas()
        self.simulation.wolf.update_position(event.x, event.y)
        self.update_animals()
        self.paint_animal(event.x, event.y, 'red')        
    
    def canvas_setup(self):
        self.canvas.pack()
        self.clear_canvas()
        self.canvas.bind('<Button-1>', self.add_sheep)
        self.canvas.bind('<Button-3>', self.update_wolf)

    def paint_animal(self, x, y, color):
        self.canvas.create_oval(x-self.dot_size/2, y-self.dot_size/2, x+self.dot_size/2, y+self.dot_size/2, width=0, fill=color)

    def add_sheep(self, event):
        self.simulation.add_sheep(event.x, event.y)
        self.paint_animal(event.x, event.y, cfg.config['sheep_color'])
        self.update_sheep_amount()

    def add_wolf(self):
        self.simulation.wolf = Wolf(cfg.config['wolf_move_dist']*self.step, cfg.config['canvas_side']/2, cfg.config['canvas_side']/2)
        self.paint_animal(cfg.config['canvas_side']/2, cfg.config['canvas_side']/2, cfg.config['wolf_color'])


    def config(self):
        self.turn = 0
        self.dot_size = 10
        self.window.title(cfg.config['title'])
        self.window.geometry(cfg.config['resolution'])
        self.step = cfg.config['canvas_side'] / (1.5 * cfg.config['init_pos_limit'])
        self.simulation = Simulation(sheep_move_dist=cfg.config['sheep_move_dist'],
                            wolf_move_dist=cfg.config['wolf_move_dist'], step=self.step)
        menu = Menu(self.window)
        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label='Open', command=self.file_open)
        file_menu.add_separator()
        file_menu.add_command(label='Save', command=self.file_save)
        file_menu.add_separator()
        file_menu.add_command(label='Quit', command=self.quit)
        settings_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label='File', menu=file_menu)
        menu.add_cascade(label='Settings', menu=settings_menu)
        self.window.config(menu=menu)
        self.sheep_amount_label = Label(self.window)
        self.update_sheep_amount()
        self.sheep_amount_label.pack()
        self.canvas = Canvas(self.window, width=cfg.config['canvas_side'], height=cfg.config['canvas_side'])
        self.canvas_setup()
        self.add_wolf()
        step_button = Button(self.window, text='Step', command=self.simulate)
        step_button.pack()
        reset_button = Button(self.window, text='Reset', command=self.reset)
        reset_button.pack()
        button = Button(self.window, text='Settings', command=self.settings)
        button.pack()

    def __init__(self):
        self.window = Tk()
        self.config()
        self.window.mainloop()