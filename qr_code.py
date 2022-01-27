import sys
from colorama import Fore
print(Fore.GREEN + '''
░██████╗░██████╗░  ░█████╗░░█████╗░██████╗░███████╗  ███╗░░░███╗░█████╗░██╗░░██╗███████╗██████╗░
██╔═══██╗██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔════╝  ████╗░████║██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██║██╗██║██████╔╝  ██║░░╚═╝██║░░██║██║░░██║█████╗░░  ██╔████╔██║███████║█████═╝░█████╗░░██████╔╝
╚██████╔╝██╔══██╗  ██║░░██╗██║░░██║██║░░██║██╔══╝░░  ██║╚██╔╝██║██╔══██║██╔═██╗░██╔══╝░░██╔══██╗
░╚═██╔═╝░██║░░██║  ╚█████╔╝╚█████╔╝██████╔╝███████╗  ██║░╚═╝░██║██║░░██║██║░╚██╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝  ░╚════╝░░╚════╝░╚═════╝░╚══════╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝''')
print(Fore.GREEN + "                                                                    -Terminal1337")

import os
Condition = input(Fore.BLUE + "[+] Do you want me to install required module for you? Y/n: ")
if Condition == "Y":
    os.system("pip install qrcode")
    pass
elif Condition == "n":
    pass
else:
    print("Error: Invalid Input")
import qrcode
path = input(Fore.RED + "[+] Enter The URL/TEXT to conver to QR: ")
output = input(Fore.LIGHTCYAN_EX + "[+] Enter the Name of Output File: ")
def qr():
    image = qrcode.make(path)
    image.save(output+'.png')

qr()
print(Fore.RED + "[-] QR Code has been successfully written to",output)
lola = input(Fore.MAGENTA + "[+] do you want to close the program(Y/n): ")
if lola == "Y":
    sys.exit()
else:
    pass
