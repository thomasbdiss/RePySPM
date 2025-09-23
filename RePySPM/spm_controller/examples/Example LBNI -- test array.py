import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

import shutil

# Get the parent directory and add it to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# import aespm as ae
# Now you can import AFMController
from lbni_controller import AFMController

# Path to the project
project_path = r"D:\\Sakshi\\OpenSPM-source\\"
afm = AFMController(project_path)

# Set the scan parameters for the exploration
# Please skip this step if you prefer setting the initial parameters manually 
print("\n--- Ramp ---")
afm.scan_control.scan_stop()

# Define the number of points along X and Y
nx = 3  # Number of steps in x-direction
ny = 1  # Number of steps in y-direction
N = 3  # Number of repetitions for each point

# Define the scan area dimensions in meters
width = 0.1e-6   # Total width of the grid (meters)
height = 0.1e-6  # Total height of the grid (meters)

# Define the origin (you can change this)
x0 = 0.0
y0 = 0.0

# Calculate the step size
dx = width / (nx - 1) if nx > 1 else 0
dy = height / (ny - 1) if ny > 1 else 0

# Loop over the grid of (x, y) positions
for iy in range(ny):
    for ix in range(nx):
        # Calculate the absolute (x, y) position
        x_pos = x0 + ix * dx
        y_pos = y0 + iy * dy

        for repeat in range(N):  # Repeat N times for the same grid position
            # Set the AFM tip position
            afm.scan_control.set_xyposition(x_pos, y_pos, forced=False)
            print(f"Moving to position ({x_pos:.12e}, {y_pos:.12e}) - Repeat {repeat + 1}/{N}")

            time.sleep(2)



