import sys
import os

# Get the parent directory and add it to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# import aespm as ae
# Now you can import AFMController
from lbni_controller import AFMController

def main():
    # Path to the project
    project_path = r"D:\\Sakshi\\OpenSPM-source\\"
    
    afm = AFMController(project_path)
    
    # Set the scan parameters for the exploration
    # Please skip this step if you prefer setting the initial parameters manually 
    print("\n--- Getting Scan Parameters ---")

    print(afm.scan_parameters.get_width())
    print(afm.scan_parameters.get_offset_x())
    print(afm.scan_parameters.get_offset_y())
    print(afm.scan_parameters.get_scan_speed())
    
    # Step N: Disconnect from the AFM system
    afm.disconnect()
    print("\n--- AFM disconnected ---")
    
if __name__ == "__main__":
    main()