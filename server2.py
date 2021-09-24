import socket

# making a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Getin IP addrs of server
Host = socket.gethostname()

# port number
Port = 1234

# binding socket with port number
s.bind((Host, Port))

# no of clients to connect
s.listen(5)


while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")

    # sendding message to the client socket
    clientsocket.send('This is a message from server'.encode())

    # closing the client socket
    clientsocket.close()