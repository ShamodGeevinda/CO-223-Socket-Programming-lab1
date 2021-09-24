import socket

# making client socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((socket.gethostname(), 1234))

# Getting input from user
cmsg = input ("Enter message to server: ")

# sendding decodede message
c.send(cmsg.encode())

# receiving a reply from server
msg = c.recv(1024)

# printing the server reply after decoding
print(msg.decode())