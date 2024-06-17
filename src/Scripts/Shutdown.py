'''
Script for all the lazy people who don't want to shutdown their system manually.
This script will close all the applications (that are mentioned in the list) and ports from 3000 to 3010 and then shutdown the system.
'''

import os
import sys
import time
import subprocess
import importlib.util


# Specify the module file path
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib', 'lib.py'))


# Load the module
spec = importlib.util.spec_from_file_location("lib", lib_path)
lib = importlib.util.module_from_spec(spec)
sys.modules["lib"] = lib
spec.loader.exec_module(lib)


# Close applications and all active ports from 3000 to 3010
lib.close_specific_applications()
lib.close_ports_3000_to_3010()


# Give a delay to ensure applications close properly
time.sleep(1)


# Initate Shutdown process
subprocess.run(["shutdown", "/s","/t","01"])
