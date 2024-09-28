'''
Script that helps to open the coding apps like VSCode and GitKraken for the coding purpose.
'''


import lib


def main():
    
    # Define Folder Path
    path = r"D:\Codings\Learning-Automation"
    
    # Open Apps
    lib.open_vscode(path)
    lib.open_gitkraken()


if __name__ == "__main__":
    main()
    
    