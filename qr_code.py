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
Condition = input("Do you want me to install required module for you? Y/n: ")
if Condition == "Y":
    os.system("pip install qrcode")
    pass
elif Condition == "n":
    pass
else:
    print("Error: Invalid Input")
import qrcode
path = input("Enter The URL/TEXT to conver to QR: ")
output = input("Enter the Name of Output File: ")
def qr():
    image = qrcode.make(path)
    image.save(output+'.png')

qr()
print("QR Code has been successfully written to",output)
lola = input("do you want to close the program(Y/n): ")
if lola == "Y":
    sys.exit()
else:
    pass