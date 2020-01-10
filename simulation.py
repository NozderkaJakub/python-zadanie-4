import math
from meadow import Meadow
import json
from writer import Writer
from printer import Printer
import logger


class Simulation:

    def __init__(self, flock_size=15, sheep_move_dist=0.5, wolf_move_dist=1.0, init_pos_limit=10.0, turns=50):
        self.meadow = Meadow()
        self.wolf = self.meadow.create_wolf(wolf_move_dist)
        self.flock = self.meadow.create_flock(
            flock_size, sheep_move_dist, init_pos_limit)
        self.alive_sheep_amount = flock_size
        self.turns = turns
        self.distances = []
        self.turn_result = {}
        self.results = []

    def simulate(self):
        logger.log_debug(__name__, "simulate", "brak", "brak")

        self.turn = 0
        while (self.turn < self.turns and self.is_any_alive_sheep()):
            self.let_flock_flee()
            self.calculate_distances_between_wolf_and_flock()
            nearest_sheep = self.get_nearest_alive_sheep()
            distance_from_nearest_sheep = nearest_sheep[1]
            if (distance_from_nearest_sheep < self.wolf.move_dist):
                self.let_wolf_eat(nearest_sheep[0])
                self.alive_sheep_amount = self.get_alive_sheep_amount()
            else:
                self.let_wolf_chase(nearest_sheep)

            self.write_turn_result()
            self.results.append(self.turn_result)

            self.turn += 1

    def let_flock_flee(self):
        logger.log_debug(__name__, "let_flock_flee", "brak", "brak")
        for id in range(0, len(self.flock)):
            self.flock[id].move()

    def let_wolf_eat(self, nearest_sheep):
        logger.log_debug(__name__, "let_wolf_eat", str(nearest_sheep), "brak")
        self.wolf.eat(nearest_sheep)

    def let_wolf_chase(self, nearest_sheep):
        logger.log_debug(__name__, "let_wolf_chase",
                         str(nearest_sheep), "brak")
        self.wolf.chase(nearest_sheep)

    def calculate_distances_between_wolf_and_flock(self):
        logger.log_debug(
            __name__, "calculate_distances_between_wolf_and_flock", "brak", "brak")
        self.distances = []
        for id in range(0, len(self.flock)):
            distance = 0.0
            distance = math.sqrt(
                math.pow(self.wolf.pos_x-self.flock[id].pos_x, 2) +
                math.pow(self.wolf.pos_y-self.flock[id].pos_y, 2)
            )
            self.distances.append([self.flock[id], distance])

    def get_nearest_alive_sheep(self):
        logger.log_debug(__name__, "get_nearest_alive_sheep", "brak", "brak")
        alive_sheep = [sheep for sheep in self.distances if sheep[0].is_alive]
        return min(alive_sheep, key=lambda x: x[1])

    def is_any_alive_sheep(self):
        result = False if not self.get_alive_sheep_amount() else True
        logger.log_debug(__name__, "is_any_alive_sheep", "brak", str(result))
        return result

    def get_alive_sheep_amount(self):
        alive_sheep_amount = len(self.flock) - self.get_eaten_sheep_amount()
        logger.log_debug(__name__, "get_alive_sheep_amount",
                         "brak", str(alive_sheep_amount))
        return alive_sheep_amount

    def get_eaten_sheep_amount(self):
        cnt = 0
        for sheep in self.flock:
            if not sheep.is_alive:
                cnt += 1
        logger.log_debug(__name__, "get_eaten_sheep_amount", "brak", str(cnt))
        return cnt

    def write_turn_result(self):
        logger.log_debug(__name__, "write_turn_result", "brak", "brak")
        self.turn_result = {
            "turn_no": self.turn,
            "wolf_pos": (self.wolf.pos_x, self.wolf.pos_y),
            "alive_sheep_amount": self.get_alive_sheep_amount(),
            "sheep_positions": []
        }
        for i in range(len(self.flock)):
            self.turn_result["sheep_positions"].append(
                (self.flock[i].pos_x, self.flock[i].pos_y) if self.flock[i].is_alive else None)
