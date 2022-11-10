# Socket Programming Task

import socket
from random import sample

# Creating a local echo server

boojoke = {
        "lead": "Knock Knock!",
        "clue": "Boo",
        "punchline": "Don't cry, I just wanted to chat"
        }

weekendjoke = {
        "lead": "Knock Knock!",
        "clue": "Weekend.",
        "punchline": "Weekend do anything we want!"
        }

goatjoke = {
        "lead": "Knock Knock!",
        "clue": "Goat.",
        "punchline": "Goat to the door and find out!"
        }

owljoke = {
        "lead": "Knock Knock!",
        "clue": "Who.",
        "punchline": "What are you, an owl?"
        }

# Available jokes
jokes = [boojoke, weekendjoke, goatjoke, owljoke]
# Sample a random joke
joke = sample(jokes, 1)[0]

# HOST = localhost IP, PORT = arbitray number over 1023
HOST = socket.gethostbyname('localhost')
PORT = 12345
print(f"Our localhost ip is {HOST} and port is {PORT}")

# create a socket "instance" (object)
s = socket.socket()
print("Socket created successfully")

# Bind to a port
s.bind((HOST, PORT))
print(f"Socket is binded to {PORT}")

# once "bound" we must "listen"
s.listen(5)


while True:
    # Establish connection for server
    conn, addr = s.accept()
    print(f"Connection accepted from {addr}")

    # Send message confirming connection
    conn.send("You were successfully connected".encode())

    # Set initial state for joke
    state = "lead"
    print(joke[state])
    conn.send(joke[state].encode())

    while True:
        # Receive data from client
        data = conn.recv(1024)
        if not data:
            break
        # Transition state of joke
        if state == "lead":
            state = "clue"
        elif state == "clue":
            state = "punchline"

        # Send client the joke
        print(joke[state])
        conn.send(joke[state].encode())

    # Disconnect from server
    conn.close()
    break
