import os
import sys
import time
import importlib.util
from colorama import Fore


repos = {
    "repo1" : r"path/to/repo1",
    "repo2" : r"path/to/repo2",
}

# Specify the module file path
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib', 'lib.py'))


# Load the module
spec = importlib.util.spec_from_file_location("lib", lib_path)
lib = importlib.util.module_from_spec(spec)
sys.modules["lib"] = lib
spec.loader.exec_module(lib)


def main():
    lib.clear_screen()
    selected = lib.use_checkboxs(repos, "Select the repositories to update:")
    
    # Perform an operation on the selected repositories
    try:
        for repo in selected:
            repo_path = repos[repo]
            lib.perform_git_pull(repo_path)
            time.sleep(1)
        print(Fore.GREEN + "All Repositories Updated Successfully..." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"Failed to perform the operation: {e}" + Fore.RESET)
        

if __name__ == "__main__":
    main()
    input(Fore.MAGENTA + "\nPress Enter to exit..." + Fore.RESET) 