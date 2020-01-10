import random
from animals import Wolf
from animals import Sheep
import logger

class Meadow:

    def create_flock(self, flock_size, sheep_move_dist, init_pos_limit):
        flock = []
        for sheep_id in range(0, flock_size):
            sheep = Sheep(
                sheep_move_dist,
                sheep_id,
                random.uniform(-init_pos_limit, init_pos_limit),
                random.uniform(-init_pos_limit, init_pos_limit)
            )
            logger.log_info(__name__, "Owca nr {} pojawila sie na pozycji [{:.3f}, {:.3f}]".format(
                sheep.id, sheep.pos_x, sheep.pos_y))
            flock.append(sheep)

        params = "flock_size: {}, sheep_move_dist: {}, init_pos_limit: {}".format(
            flock_size, sheep_move_dist, init_pos_limit)
        logger.log_debug(__name__, "create_flock", params, str(flock))

        return flock

    def create_wolf(self, wolf_move_dist):
        wolf = Wolf(wolf_move_dist)

        logger.log_debug(__name__,
                         "create_wolf", str(wolf_move_dist), str(wolf))
        logger.log_info(__name__,
                        "Wilk pojawil sie na pozycji [{:.3f}, {:.3f}]".format(wolf.pos_x, wolf.pos_y))

        return wolf
