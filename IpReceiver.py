import socket

PORT = 5005

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(("", PORT))

Found = False

print("Looking for Raspberry's")
while Found == False:
    data, addr = serverSocket.recvfrom(1024)

    data = data.decode('utf-8')

    if data.startswith("Pi name:"):
        print("")
        print("Found a Raspberry!")
        print("")
        print(data)
        Found = True

serverSocket.close()
