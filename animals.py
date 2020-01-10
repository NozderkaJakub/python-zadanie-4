import math
import random
import logger


class Wolf:

    def __init__(self, move_dist=1.0, pos_x=0.0, pos_y=0.0):
        self.move_dist = move_dist
        self.pos_x = 0.0
        self.pos_y = 0.0

    def eat(self, nearest_sheep):
        logger.log_debug(__name__, "eat", str(nearest_sheep), "brak")
        nearest_sheep.is_alive = False
        logger.log_info(__name__, "Wilk pozarl owce nr {}".format(nearest_sheep.id))

    def chase(self, nearest_sheep):
        logger.log_debug(__name__, "chase", str(nearest_sheep), "brak")

        # obliczam wektor miedzy wilkiem a owca
        vector_beetween_wolf_and_sheep = [
            nearest_sheep[0].pos_x - self.pos_x, nearest_sheep[0].pos_y - self.pos_y]
        # a nastepnie wektor jednostkowy
        unit_vector_beetween_wolf_and_sheep = [vector_beetween_wolf_and_sheep[0]/nearest_sheep[1],
                                               vector_beetween_wolf_and_sheep[1] /
                                               nearest_sheep[1]
                                               ]

        previous_pos = [self.pos_x, self.pos_y]
        # i przesuwam wilka o wektor jednostkowy czyli jego krok równy 1
        self.pos_x += unit_vector_beetween_wolf_and_sheep[0] * self.move_dist
        self.pos_y += unit_vector_beetween_wolf_and_sheep[1] * self.move_dist
        current_pos = [self.pos_x, self.pos_y]

        logger.log_info(__name__,"Wilk zmienil pozycje z [{:.3f},{:.3f}] na [{:.3f},{:.3f}]".format(
            previous_pos[0], previous_pos[1], current_pos[0], current_pos[1]))


class Sheep:
    directions = ["north", "east", "south", "west"]

    def __init__(self, move_dist, id, pos_x, pos_y):
        self.move_dist = move_dist
        self.id = id
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_alive = True

    def move(self):
        logger.log_debug(__name__, "move", "brak", "brak")

        previous_pos = [self.pos_x, self.pos_y]
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

        current_pos = [self.pos_x, self.pos_y]
        if self.is_alive:
            logger.log_info(__name__, "Owca nr {} zmienila pozycje z [{:.3f},{:.3f}] na [{:.3f},{:.3f}]".format(
                self.id, previous_pos[0], previous_pos[1], current_pos[0], current_pos[1]))
