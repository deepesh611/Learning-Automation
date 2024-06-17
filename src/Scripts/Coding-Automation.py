'''
Script that helps to open the coding apps like VSCode and GitKraken for the coding purpose.
'''


import os
import sys
import importlib.util


# Specify the module file path
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib', 'lib.py'))

# Load the module
spec = importlib.util.spec_from_file_location("lib", lib_path)
lib = importlib.util.module_from_spec(spec)
sys.modules["lib"] = lib
spec.loader.exec_module(lib)


def main():
    
    # Define Folder Path
    path = r"D:\Codings\Learning-Automation"
    
    # Open Apps
    lib.open_vscode(path)
    lib.open_gitkraken()


if __name__ == "__main__":
    main()
    
    