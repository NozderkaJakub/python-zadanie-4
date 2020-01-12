import configuration as cfg
import exceptions_handler as exc

from simulation import Simulation
from window import Window

cfg.create_config()
try:
    exc.raise_exceptions()
except ValueError as message:
    exc.handle_exceptions(message)
else:
    # simulate()
    window = Window()
