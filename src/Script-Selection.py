import re
import os
import sys
import msvcrt
import subprocess
import importlib.util


# Import Lib module
lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Scripts', 'lib.py'))
spec = importlib.util.spec_from_file_location("lib", lib_path)
lib = importlib.util.module_from_spec(spec)
sys.modules["lib"] = lib
spec.loader.exec_module(lib)


# Define ANSI escape codes for colors
COLORS = lib.COLORS


# Function to get colored script names
def get_colored_scripts():
    directory = "./Scripts"
    try:
        files = os.listdir(directory)
    except FileNotFoundError:
        print(f"Directory '{directory}' not found.")
        sys.exit(1)

    colors = [COLORS['magenta'], COLORS['yellow'], COLORS['green'], COLORS['red'], COLORS['cyan'], COLORS['blue']]
    script_mapping = {}
    scripts = []

    for i, file in enumerate(files):
        if file != "lib.py":
            if file.endswith(".py"):
                script_name = file[:-3]                                                     # Remove .py extension from file names
                colored_script = colors[i % len(colors)] + script_name + COLORS['reset']
                scripts.append(colored_script)
                script_mapping[script_name] = file

    return scripts, script_mapping


# Function to strip ANSI escape codes from text
def strip_ansi_codes(text):
    ansi_escape = re.compile(r'\x1b\[([0-9]+)(;[0-9]+)*m')
    return ansi_escape.sub('', text)


# Dynamically populate the SCRIPTS list and mapping
SCRIPTS, SCRIPT_MAPPING = get_colored_scripts()


# Function to print the menu with arrow key selection
def print_menu(selected_index):
    sys.stdout.write("\033[H\033[J")                        # Clear the screen

    print("\033[1mSelect Your Preferred Startup:\033[0m\n")
    
    for index, script in enumerate(SCRIPTS):
        if index == selected_index:
            print(f"  {COLORS['white']}>> {COLORS['reset']}{script}")
        else:
            print(f"    {script}")
    
    print("\nUse arrow keys (↑ ↓) to navigate, and press Enter to select.\n")


# Main function to select script
def select():
    selected_index = 0
    while True:
        print_menu(selected_index)
       
        # Capture arrow key input
        key = msvcrt.getch()
        if key == b'\xe0':                                              # Arrow key prefix
            key = msvcrt.getch()
            if key == b'H':                                             # Up arrow key
                selected_index = (selected_index - 1) % len(SCRIPTS)
            elif key == b'P':                                           # Down arrow key
                selected_index = (selected_index + 1) % len(SCRIPTS)
        elif key == b'\r':                                              # Enter key
            break

    # Print the selected script
    sys.stdout.write("\033[H\033[J")                            # Clear the screen
    
    selected_script = strip_ansi_codes(SCRIPTS[selected_index])
    actual_script = SCRIPT_MAPPING[selected_script]
    script_path = os.path.join("./Scripts", actual_script)
    command = f'python "{script_path}"'
    subprocess.Popen(command, shell=True)


# Run the function
if __name__ == "__main__":
    select()
