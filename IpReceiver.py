import socket
import sys
from colorama import Fore, init, deinit

#Colorama on windows
init()

PORT = 5005

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(("", PORT))

Found = False

print("*********************************")
print("*     Looking for Raspberry     *")
print("*********************************")
while Found == False:
    data, addr = serverSocket.recvfrom(1024)

    data = data.decode('utf-8')

    if data.startswith("Pi Name:"):
        print("*       Found a Raspberry       *")
        print("*********************************")
        print(Fore.LIGHTGREEN_EX + data)
        print(Fore.RESET + "*********************************")
        print("")
        Found = True

#Stop using Colorama on Windows
deinit()

serverSocket.close()

sys.exit()