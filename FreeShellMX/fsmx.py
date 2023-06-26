import os
import socket
import platform
import webbrowser

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

clear = lambda: os.system('cls')


version = "v1.0.0"
pcname = socket.gethostname()
username = os.getlogin()

print("Welcome to FreeShellMX", version,"! \n")

while True:
    cmds = input(username + "@" +pcname+ " -& ")

    if cmds == "about":
        print("\n")
        print("'########:'########::'########:'########::'######::'##::::'##:'########:'##:::::::'##:::::::")
        print("##.....:: ##.... ##: ##.....:: ##.....::'##... ##: ##:::: ##: ##.....:: ##::::::: ##:::::::")
        print("##::::::: ##:::: ##: ##::::::: ##::::::: ##:::..:: ##:::: ##: ##::::::: ##::::::: ##:::::::")
        print("######::: ########:: ######::: ######:::. ######:: #########: ######::: ##::::::: ##:::::::")
        print("##...:::: ##.. ##::: ##...:::: ##...:::::..... ##: ##.... ##: ##...:::: ##::::::: ##:::::::")
        print("##::::::: ##::. ##:: ##::::::: ##:::::::'##::: ##: ##:::: ##: ##::::::: ##::::::: ##:::::::")
        print("##::::::: ##:::. ##: ########: ########:. ######:: ##:::: ##: ########: ########: ########:")
        print("..::::::::..:::::..::........::........:::......:::..:::::..::........::........::........::")
        print("FreeShellMX", version, "\n")
    elif cmds == "help":
        print(f"{bcolors.OKCYAN}BASIC FREESHELL COMMANDS:")
        print("help -> shows all commands")
        print("about -> freeshellMX about screen")
        print("exit -> exits freeshellMX")
        print("clear -> clears freeshellMX terminal")
        print(f"{bcolors.FAIL}ADVANCED FREESHELL COMMANDS:")
        print("fs seldir -> prints out selected directory")
        print("fs dir -> prints out items in directory")
        print("fs mkdir -> makes a file in target directory")
        print("fs pcinfo -> prints out pc information")
        print("fs rmdir -> removes file/folder in current directory")
        print("fs myip -> prints out current ip")
        print("fs search -> opens user-inputted url url in browser")
        print("fs gitpage -> opens github page of fsmx in browser")


    elif cmds == "exit":
        confirm = input(f"{bcolors.WARNING} WARNING : Are you sure? (Y/N) ").lower()
        if confirm == "y":
            exit()
        else:
            break
    elif cmds == "clear":
        clear()
    elif cmds == "fs seldir":
        print(os.getcwd())
    elif cmds == "fs dir":
        print(os.listdir(os.getcwd()))
    elif cmds == "fs mkdir":
        file = input("Insert file name. ")
        makedir = os.path.join(os.getcwd(), file)
        os.mkdir(makedir)
    elif cmds == "fs pcinfo":
        print(platform.uname())
    elif cmds == "fs rmdir":
        file = input("Insert file name to remove. ")
        confirm = input(f"{bcolors.WARNING} WARNING : Are you sure? (Y/N) ").lower()
        if confirm == "y":
            rmdir = os.path.join(os.getcwd(), file)
            os.rmdir(rmdir)
        else:
            break
    elif cmds == "fs myip":
        ip = socket.gethostbyname('www.google.com')
        print(ip)
    elif cmds == "fs search":
        website = input("What website do you want to open? (URL) : ")
        webbrowser.open(str(website))

    
