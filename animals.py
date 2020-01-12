import math
import random


class Wolf:

    def __init__(self, move_dist=1.0, pos_x=0.0, pos_y=0.0):
        self.move_dist = move_dist
        self.pos_x = pos_x
        self.pos_y = pos_y

    def update_position(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def eat(self, nearest_sheep):
        nearest_sheep.is_alive = False

    def chase(self, nearest_sheep):
        # obliczam wektor miedzy wilkiem a owca
        vector_beetween_wolf_and_sheep = [
            nearest_sheep[0].pos_x - self.pos_x, nearest_sheep[0].pos_y - self.pos_y]
        # a nastepnie wektor jednostkowy
        unit_vector_beetween_wolf_and_sheep = [vector_beetween_wolf_and_sheep[0]/nearest_sheep[1],
                                               vector_beetween_wolf_and_sheep[1] /
                                               nearest_sheep[1]
                                               ]

        # i przesuwam wilka o wektor jednostkowy czyli jego krok równy 1
        self.pos_x += unit_vector_beetween_wolf_and_sheep[0] * self.move_dist
        self.pos_y += unit_vector_beetween_wolf_and_sheep[1] * self.move_dist


class Sheep:
    directions = ["north", "east", "south", "west"]

    def __init__(self, move_dist, id, pos_x, pos_y):
        self.move_dist = move_dist
        self.id = id
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_alive = True

    def move(self):
        if self.is_alive:
            direction = random.choice(Sheep.directions)
            if direction is "north":
                self.pos_y += self.move_dist
            elif direction is "east":
                self.pos_x += self.move_dist
            elif direction is "south":
                self.pos_y -= self.move_dist
            elif direction is "west":
                self.pos_x -= self.move_dist
