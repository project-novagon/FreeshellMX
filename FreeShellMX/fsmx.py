import os
import socket
import platform
import webbrowser
import colorama
from colorama import Fore


clear = lambda: os.system('cls')


version = "v1.1.0"
pcname = socket.gethostname()
username = os.getlogin()
color = Fore.WHITE

print("Welcome to FreeShellMX", version,"! \n")

while True:
    cmds = input(color + username + "@" +pcname+ " -$ ")

    if cmds == "about":
        print("")
        print("'########:'########::'########:'########::'######::'##::::'##:'########:'##:::::::'##:::::::")
        print("##.....:: ##.... ##: ##.....:: ##.....::'##... ##: ##:::: ##: ##.....:: ##::::::: ##:::::::")
        print("##::::::: ##:::: ##: ##::::::: ##::::::: ##:::..:: ##:::: ##: ##::::::: ##::::::: ##:::::::")
        print("######::: ########:: ######::: ######:::. ######:: #########: ######::: ##::::::: ##:::::::")
        print("##...:::: ##.. ##::: ##...:::: ##...:::::..... ##: ##.... ##: ##...:::: ##::::::: ##:::::::")
        print("##::::::: ##::. ##:: ##::::::: ##:::::::'##::: ##: ##:::: ##: ##::::::: ##::::::: ##:::::::")
        print("##::::::: ##:::. ##: ########: ########:. ######:: ##:::: ##: ########: ########: ########:")
        print("..::::::::..:::::..::........::........:::......:::..:::::..::........::........::........::")
        print(Fore.CYAN + "FreeShellMX", version, "\n")
    elif cmds == "help":
        print(Fore.CYAN + "BASIC FREESHELL COMMANDS:")
        print(Fore.CYAN + "help -> shows all commands")
        print(Fore.CYAN + "about -> freeshellMX about screen")
        print(Fore.CYAN + "exit -> exits freeshellMX")
        print(Fore.CYAN + "clear -> clears freeshellMX terminal")
        print(Fore.MAGENTA + "ADVANCED FREESHELL COMMANDS:")
        print(Fore.MAGENTA + "fs seldir -> prints out selected directory")
        print(Fore.MAGENTA + "fs dir -> prints out items in directory")
        print(Fore.MAGENTA + "fs mkdir -> makes a file in target directory")
        print(Fore.MAGENTA + "fs pcinfo -> prints out pc information")
        print(Fore.MAGENTA + "fs rmdir -> removes file/folder in current directory")
        print(Fore.MAGENTA + "fs myip -> prints out current ip")
        print(Fore.MAGENTA + "fs search -> opens user-inputted url in browser")
        print(Fore.MAGENTA + "fs gitpage -> opens github page of fsmx in browser")
        print(Fore.MAGENTA + "fs color -> change shell color")
    elif cmds == "exit":
        confirm = input( Fore.LIGHTYELLOW_EX + "WARNING : Are you sure? (Y/N) ").lower()
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
        confirm = input(Fore.LIGHTYELLOW_EX + "WARNING : Are you sure? (Y/N) ").lower()
        if confirm == "y":
            try:
                rmdir = os.path.join(os.getcwd(), file)
                os.rmdir(rmdir)
            except FileNotFoundError:
                print(Fore.RED + "File ", file ," not found.")
        else:
            break
    elif cmds == "fs myip":
        ip = socket.gethostbyname('www.google.com')
        print(ip)
    elif cmds == "fs search":
        website = input("What website do you want to open? (URL) : ")
        webbrowser.open(str(website))
    elif cmds == "fs gitpage":
        webbrowser.open("https://github.com/project-novagon/FreeshellMX")
    elif cmds == "fs color":
        colorsel = input("What color do you want to choose? ( fs color -h / fs color help for available colors): ")
        if colorsel == "PURPLE" or colorsel == "purple":
            color = Fore.MAGENTA
        if colorsel == "GREEN" or colorsel == "green":
            color = Fore.GREEN
        if colorsel == "WHITE" or colorsel == "white":
            color = Fore.WHITE
        if colorsel == "BLUE" or colorsel == "blue":
            color = Fore.BLUE
        if colorsel == "RED" or colorsel =="red":
            color = Fore.LIGHTRED_EX
    elif cmds == "fs color -h" or cmds == "fs color help":
        print("Availble colors:")
        print(Fore.MAGENTA + "Purple")
        print(Fore.GREEN + "Green")
        print(Fore.WHITE + "White")
        print(Fore.BLUE + "Blue")
        print(Fore.RED + "Red")
    else:
        print(Fore.RED + "ERROR : Command not found!")

    
