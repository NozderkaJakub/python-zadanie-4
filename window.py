from tkinter import *
from tkinter import filedialog
import json
from simulation import Simulation
import configuration as cfg
from printer import Printer

class Window():

    def quit(self):
        self.window.destroy()

    def update_sheep_amount(self):
        self.sheep_amount_label.config(text='Liczba żywych owiec: ' + str(self.simulation.get_alive_sheep_amount()))

    def simulate(self):
        if self.turn <= self.simulation.turns-1:
            self.simulation.step()
            self.turn += 1
            self.update_sheep_amount()
        else:
            print('Osiągnięto końcową liczbę rund')

    def reset(self):
        self.simulation = Simulation(flock_size=cfg.config['sheep'], sheep_move_dist=cfg.config['sheep_move_dist'],
                            wolf_move_dist=cfg.config['wolf_move_dist'], init_pos_limit=cfg.config['init_pos_limit'],
                            turns=cfg.config['rounds'])
        self.turn = 0
        self.update_sheep_amount()

    def restore_game(self, result):
        self.simulation = Simulation(flock_size=result['sheeps'], sheep_move_dist=result['sheep_move_dist'],
                            wolf_move_dist=result['wolf_move_dist'], init_pos_limit=result['init_pos_limit'],
                            turns=result['turns'])
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
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt", title='Wybierz, gdzie chcesz zapisać plik ze stanem rozgrywki')
        if f is None:
            return
        text2save = json.dumps(self.simulation.turn_result, indent=4)
        f.write(text2save)
        f.close()

    def file_open(self):
        f = filedialog.askopenfile(initialdir = "./",title = "Wybierz plik z zapisanym stanem rozgrywki")
        result = json.loads(f.read())
        self.restore_game(result)

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
        step_button = Button(self.window, text='Step', command=self.simulate)
        step_button.pack()
        reset_button = Button(self.window, text='Reset', command=self.reset)
        reset_button.pack()

        
        self.window.mainloop()