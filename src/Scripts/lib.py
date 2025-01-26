import os
import sys
import psutil
import requests
import inquirer
import webbrowser
import subprocess
from colorama import Fore


# Define Variables, Constants, Paths, etc.
repo_path = "D:\\Codings\\"
github = "https://github.com/"
chatgpt = "https://chatgpt.com/"
youtube = "https://www.youtube.com/"

vscode_path = r"D:\Microsoft VS Code\Code.exe"
PyCharm = r"D:\PyCharm\PyCharm 2024.1.2\bin\pycharm64.exe"
web_storm = r"D:\WebStorm\WebStorm 2024.1.5\bin\webstorm64.exe"
gitkraken_path = r"C:\Users\deepe\AppData\Local\gitkraken\gitkraken.exe"
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

apps_to_close = ["Code", "msedge", "chrome", "GitKraken", "WhatsApp", "Calculator", "notepad", "Excel", "Word", "VirtualBox", "PowerPoint", "OneNote"]


def close_specific_applications():
    # Iterate over all running processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Check if the process name matches any app in the list
            for app in apps_to_close:
                if app.lower() in proc.info['name'].lower():
                    print(Fore.YELLOW + f"Attempting to close: {proc.info['name']}" + Fore.RESET)
                    proc.terminate()
                    proc.wait(timeout=5)
                    print(Fore.GREEN + f"{proc.info['name']} closed successfully." + Fore.RESET)
                    break                                                      
                
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, psutil.TimeoutExpired):
            continue


def close_ports_3000_to_3010():
    for conn in psutil.net_connections(kind='inet'):
        if 3000 <= conn.laddr.port <= 3010 and conn.status == psutil.CONN_LISTEN:
            try:
                proc = psutil.Process(conn.pid)
                print(Fore.YELLOW + f"Closing process {proc.name()} using port {conn.laddr.port}" + Fore.RESET)
                proc.terminate()
                proc.wait(timeout=5)
                print(Fore.YELLOW + "Process terminated successfully..." + Fore.RESET)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, psutil.TimeoutExpired):
                continue


def open_vscode(repo_path):
    try:
        if not os.path.exists(vscode_path):
            raise FileNotFoundError(Fore.RED + f"VS Code executable not found at {vscode_path}" + Fore.RESET) 
        subprocess.Popen([vscode_path, repo_path])
        print(Fore.GREEN + f"VS Code opened with repo: {repo_path}." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"Failed to open VS Code: {e}" + Fore.RESET)


def perform_git_pull(repo_path):
    try:
        result = subprocess.run(["git", "pull"], cwd=repo_path, capture_output=True, text=True)
        print(result.stdout)
        if result.returncode == 0:
            print(Fore.GREEN + "git pull completed successfully...\n" + Fore.RESET)
        else:
            print(Fore.RED + f"git pull failed: {result.stderr}" + Fore.RESET)
            
    except Exception as e:
        print(Fore.RED + f"Failed to perform git pull: {e}" + Fore.RESET)


def run_npm_dev(repo_path):
    try:        
        package_json_path = os.path.join(repo_path, "package.json")
        if not os.path.exists(package_json_path):
            raise FileNotFoundError(f"package.json not found at {repo_path}")
        
        with open(package_json_path, "r") as file:
            package_json = file.read()
            if '"dev"' not in package_json:
                raise ValueError(f"No 'dev' script found in package.json at {repo_path}")
        
        subprocess.Popen(f"cd {repo_path} && npm run dev", shell=True)
        print(Fore.GREEN + "npm run dev started." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"Failed to run npm run dev: {e}" + Fore.RESET)


def open_localhost_in_edge():
    try:
        if not os.path.exists(edge_path):
            raise FileNotFoundError(f"Microsoft Edge executable not found at {edge_path}")
        
        active_port = None
        for port in range(3000, 3011):
            try:
                response = requests.get(f"http://localhost:{port}")
                if response.status_code == 200:
                    active_port = port
                    break
            except requests.ConnectionError:
                continue

        if active_port is not None:
            url = f"http://localhost:{active_port}"
            subprocess.run([edge_path, url])
            print(Fore.GREEN + f"Opened {url} in Microsoft Edge." + Fore.RESET)
        else:
            print(Fore.RED + "No active server found on ports 3000 to 3010." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"/nFailed to open localhost in Edge: {e}" + Fore.RESET)
        

def open_gitkraken():
    try:
        if not os.path.exists(gitkraken_path):
            raise FileNotFoundError(f"GitKraken executable not found at {gitkraken_path}")
        subprocess.Popen([gitkraken_path])
        print(Fore.GREEN + f"GitKraken opened." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"Failed to open GitKraken: {e}" + Fore.RESET)


def open_chrome():
    webbrowser.open(github)
    webbrowser.open_new_tab(youtube)
    webbrowser.open_new_tab(chatgpt)


def open_whatsapp():
    try:
        subprocess.run(["explorer.exe", "shell:appsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App"])
        print(Fore.GREEN + "\nWhatsApp opened." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"Failed to open WhatsApp: {e}" + Fore.RESET)
        

def open_outlook():
    try:
        subprocess.run(["explorer.exe", "shell:appsFolder\\Microsoft.Office.Desktop.Outlook"])
        print(Fore.GREEN + "Outlook opened." + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"Failed to open Outlook: {e}" + Fore.RESET)
        
        
def open_ms_to_do():
    try:
        subprocess.run(["explorer.exe", "shell:appsFolder\\Microsoft.Todos_8wekyb3d8bbwe!App"])
        print(Fore.GREEN + "\nMicrosoft To Do opened.\n" + Fore.RESET, end='')
    except Exception as e:
        print(Fore.RED + f"Failed to open Microsoft To Do: {e}\n" + Fore.RESET, end='')  


def open_instagram():
    try:
        subprocess.run(["explorer.exe", "shell:appsFolder\\Facebook.InstagramBeta_42.0.23.0_neutral__8xx8rvfyw5nnt!Instagram"])
        print(Fore.GREEN + "\nInstagram opened.\n" + Fore.RESET, end='')
    except Exception as e:
        print(Fore.RED + f"Failed to open Instagram: {e}\n" + Fore.RESET, end='')
        
        
def run_command(cmd):
    
    """
    Run a command in Command Prompt.

    Parameters:
    - cmd (str): The command to be executed.

    Returns:
    - return_code (int): The return code of the command execution.
    - output (str): The standard output of the command.
    """
    
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.returncode, result.stdout
    except subprocess.CalledProcessError as e:
        return e.returncode, e.stderr


def clear_screen():
    sys.stdout.write("\033[H\033[J")  
    
    
def use_checkboxs(dict, msg):
    
    # Define the checkbox prompt
    questions = [
        inquirer.Checkbox(
            'selected',
            message=msg,
            choices=list(dict.keys())
        )
    ]

    # Prompt the user and get the selected repositories
    selected = inquirer.prompt(questions)['selected']
    return selected


def open_webstorm(project_path):
    try:
        # For Windows (ensure the correct path to webstorm.exe):
        subprocess.run([web_storm, project_path], check=True)
        
        # For Linux/macOS
        # subprocess.run(["webstorm", project_path])
        
        # Example for Linux with full path:
        # subprocess.run(["/path/to/webstorm/bin/webstorm.sh", project_path], check=True)
        
        # Example for macOS with full path:
        # subprocess.run(["/Applications/WebStorm.app/Contents/MacOS/webstorm", project_path], check=True)
        
    except FileNotFoundError:
        print(Fore.RED + "WebStorm not found. Make sure it's installed and the path is correct." + Fore.RESET)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"An error occurred while trying to open WebStorm: {e}" + Fore.RESET)


def open_pycharm(project_path):
    try:
        # For Windows (ensure the correct path to pycharm64.exe):
        subprocess.run([PyCharm, project_path], check=True)
        
        # For Linux/macOS
        # subprocess.run(["pycharm", project_path])
        
        # Example for Linux with full path:
        # subprocess.run(["/path/to/pycharm/bin/pycharm.sh", project_path], check=True)
        
        # Example for macOS with full path:
        # subprocess.run(["/Applications/PyCharm.app/Contents/MacOS/pycharm", project_path], check=True)
        
    except FileNotFoundError:
        print(Fore.RED + "PyCharm not found. Make sure it's installed and the path is correct." + Fore.RESET)
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"An error occurred while trying to open PyCharm: {e}" + Fore.RESET)
        
        
def check_url_status(url):
    try:
        response = requests.get(url)
        # Check if the status code is 404 or other errors
        if response.status_code == 404:
            return False, "404 Not Found"
        # You can check for other status codes if needed, e.g. 403 for Forbidden, 500 for Server errors
        elif response.status_code != 200:
            return False, f"Error: {response.status_code}"
        return True, None
    except requests.exceptions.RequestException as e:
        return False, str(e)




        