import time
import logging
from .commands import OHCcommands

class Bias:
    def __init__(self, controller):
        self.controller = controller  # Store reference to AFMController

    def get_bias(self) -> float:
        control = "Bias (AO4/AN2LV)"
        command = f"{OHCcommands.r_bias}{control}"
        return self.controller.read_control(command, control)
    
    def set_bias(self, value : float):
        control = "Bias (AO4/AN2LV)"
        command = f"{OHCcommands.w_bias}{control}:{value}"
        logging.info(f"Setting bias to {value}")
        self.controller.write_control(command)