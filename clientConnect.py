# Socket Programming Task

import socket
 
# Create a socket object
sclient = socket.socket()        
 
## cross-platform, telnet-ish connection

PORT = 12345
HOST = socket.gethostbyname("localhost")

# in order to "connect" to a server - I must "connect" to its socket
sclient.connect((HOST, PORT))

# recieve some data from our connected client (decode that string)
while True:
    data = sclient.recv(1024).decode()
    print(f"{data}")
    response = input("Enter response: ")
    if response is None or response == "":
        break
    else:
        sclient.send(f"{response}".encode())

#close connection
sclient.close()