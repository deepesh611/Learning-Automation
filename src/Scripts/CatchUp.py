'''
Catch Up to the latest updates, may it be emails, messages, or any other form of communication.
1. Opens OutLook, WhatsApp 
2. Performs Git Pull on selected Repositories (Make Sure that you have already cloned the repositories and have the actual path add to the script)
'''


# Import Modules
import os
import sys
import importlib.util


# Define Constants
repo_path_to_perform_git_pull = [
    r"Actual (Full) Path to the Repository 1",
    r"Acutal (Full) Path to the Repository 2"
]


# Specify the module file path
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib', 'lib.py'))

# Load the module
spec = importlib.util.spec_from_file_location("lib", lib_path)
lib = importlib.util.module_from_spec(spec)
sys.modules["lib"] = lib
spec.loader.exec_module(lib)


def main():
    print()
    lib.open_whatsapp()
    lib.open_outlook()
    
    for repos in repo_path_to_perform_git_pull:
        print(f"\nPerforming git pull in folder: {os.path.basename(os.path.normpath(repos))}")
        lib.perform_git_pull(repos)
    

if __name__ == "__main__":
    main()