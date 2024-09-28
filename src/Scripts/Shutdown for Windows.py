'''
Script for all the lazy developers who don't want to shutdown their system manually.
This script will close all the applications (that are mentioned in the list) and ports from 3000 to 3010 and then shutdown the system.
'''

import lib
import time
import subprocess


# Close applications and all active ports from 3000 to 3010
lib.close_specific_applications()
lib.close_ports_3000_to_3010()


# Give a delay to ensure applications close properly
time.sleep(1)


# Initate Shutdown process
subprocess.run(["shutdown", "/s","/t","01"])
