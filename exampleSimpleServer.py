import socket

## File to show cross-platform.
## Create a local "echo" server

## HOST = localhost IP, PORT = arbitray number over 1023
HOST = socket.gethostbyname('localhost')
PORT = 12345
print(f"Our localhost ip is {HOST} and port is {PORT}")

## create a socket "instance" (object)
simple = socket.socket()
print("Socket created successfully")

## Bind to a port
simple.bind((HOST, PORT))
print(f"Socket is binded to {PORT}")

## once "bound" we must "listen"
simple.listen(5)

## infinte loop - until interrupt or error
while True:
    # Establish connection for our simple server
    conn, addr = simple.accept()
    print(f"Connection accepted from {addr}")

    # Send message confirming connection
    conn.send("You were successfully connected".encode())

    ## We're closing after a single send event and then disconnecting (no infinte loop)
    conn.close()
    break

