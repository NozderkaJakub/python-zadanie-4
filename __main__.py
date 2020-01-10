import configuration as cfg
import exceptions_handler as exc
import logger

from simulation import Simulation
from printer import Printer
from writer import Writer
from window import Window

def simulate():
    logger.log_debug(__name__, "simulate", "brak", "brak")

    simulation = Simulation(flock_size=cfg.config["sheep"], sheep_move_dist=cfg.config["sheep_move_dist"],
                            wolf_move_dist=cfg.config["wolf_move_dist"], init_pos_limit=cfg.config["init_pos_limit"],
                            turns=cfg.config["rounds"])
    simulation.simulate()

    Printer.print_simulation_results(
        simulation.results, wait=cfg.config["wait"])

    Writer.write_to_json(
        simulation_results=simulation.results, directory=cfg.config["dir_to_save"])
    Writer.write_to_csv(
        simulation_results=simulation.results, directory=cfg.config["dir_to_save"])

cfg.create_config()
logger.create_basic_config(cfg.config)
try:
    exc.raise_exceptions()
except ValueError as message:
    exc.handle_exceptions(message)
else:
    simulate()
    window = Window()
