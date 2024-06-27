import os
import psutil
import requests
import subprocess
from colorama import Fore


repo_path = "D:\\Codings\\"
vscode_path = r"D:\Microsoft VS Code\Code.exe"
gitkraken_path = r"<path to GitKraken executable>"
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"


def close_specific_applications():
    apps_to_close = [
        "Code", 
        "Word", 
        "Excel", 
        "chrome", 
        "msedge", 
        "OneNote",
        "notepad", 
        "WhatsApp", 
        "GitKraken", 
        "VirtualBox",
        "PowerPoint", 
        "Calculator", 
    ]

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
                    
                    break           # Exit loop after terminating the process
                
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
            print(Fore.GREEN + "git pull completed successfully." + Fore.RESET)
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
            print(Fore.GREEN + f"/nOpened {url} in Microsoft Edge." + Fore.RESET)
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


def open_whatsapp():
    try:
        subprocess.run(["explorer.exe", "shell:appsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App"])
        print(Fore.GREEN + "WhatsApp opened." + Fore.RESET)
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
        print(Fore.GREEN + "Microsoft To Do opened." + Fore.RESET, end='')
        
    except Exception as e:
        print(Fore.RED + f"Failed to open Microsoft To Do: {e}" + Fore.RESET, end='')
        
        
        
        