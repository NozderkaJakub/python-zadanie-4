import math
from animals import Wolf
from animals import Sheep
import json
import configuration as cfg


class Simulation:

    def __init__(self, sheep_move_dist=0.5, wolf_move_dist=1.0, step=54, scale=1.0):
        self.step = step
        self.scale = scale
        self.wolf = Wolf(wolf_move_dist * self.step)
        self.flock = []
        self.distances = []
        self.turn_result = {}
        self.results = []
        self.turn = 0

    def add_sheep(self, x, y):
        sheep = Sheep(
                cfg.config["sheep_move_dist"] * self.step,
                len(self.flock),
                x,
                y)
        self.flock.append(sheep)

    def update_scale(self, multiplier):
        self.wolf.move_dist *= multiplier
        self.wolf.pos_x *= multiplier
        self.wolf.pos_y *= multiplier
        for i in range(len(self.flock)):
            self.flock[i].move_dist *= multiplier
            self.flock[i].pos_x *= multiplier
            self.flock[i].pos_y *= multiplier
        self.scale *= multiplier
        self.step *= multiplier

    def go_step(self):
        if self.get_alive_sheep_amount() != 0:
            self.let_flock_flee()
            self.calculate_distances_between_wolf_and_flock()
            nearest_sheep = self.get_nearest_alive_sheep()
            distance_from_nearest_sheep = nearest_sheep[1]
            if (distance_from_nearest_sheep < self.wolf.move_dist):
                self.let_wolf_eat(nearest_sheep[0])
                self.alive_sheep_amount = self.get_alive_sheep_amount()
            else:
                self.let_wolf_chase(nearest_sheep)

            self.turn += 1
            self.write_turn_result()
            # print(self.turn_result)
            self.results.append(self.turn_result)
        else:
            print("Baco, nie ma łowiecek")


    def let_flock_flee(self):
        for id in range(0, len(self.flock)):
            self.flock[id].move()

    def let_wolf_eat(self, nearest_sheep):
        self.wolf.eat(nearest_sheep)

    def let_wolf_chase(self, nearest_sheep):
        self.wolf.chase(nearest_sheep)

    def calculate_distances_between_wolf_and_flock(self):
        self.distances = []
        for id in range(0, len(self.flock)):
            distance = 0.0
            distance = math.sqrt(
                math.pow(self.wolf.pos_x-self.flock[id].pos_x, 2) +
                math.pow(self.wolf.pos_y-self.flock[id].pos_y, 2)
            )
            self.distances.append([self.flock[id], distance])

    def get_nearest_alive_sheep(self):
        alive_sheep = [sheep for sheep in self.distances if sheep[0].is_alive]
        if self.get_alive_sheep_amount() != 0:
            return min(alive_sheep, key=lambda x: x[1])
        else:
            return None

    def is_any_alive_sheep(self):
        result = False if not self.get_alive_sheep_amount() else True
        return result

    def get_alive_sheep_amount(self):
        x = 0
        for i in range(len(self.flock)):
            if self.flock[i].is_alive:
                x += 1
        return x

    def get_eaten_sheep_amount(self):
        cnt = 0
        for sheep in self.flock:
            if not sheep.is_alive:
                cnt += 1
        return cnt

    def write_turn_result(self):
        self.turn_result = {
            "turn_no": self.turn,
            "wolf_pos": (self.wolf.pos_x, self.wolf.pos_y),
            "sheep_positions": [],
            "sheep_move_dist": self.flock[0].move_dist,
            "wolf_move_dist": self.wolf.move_dist,
            "sheeps": len(self.flock)
        }
        for i in range(len(self.flock)):
            self.turn_result["sheep_positions"].append(
                (self.flock[i].pos_x, self.flock[i].pos_y) if self.flock[i].is_alive else None)
