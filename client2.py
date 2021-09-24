import socket

# making client socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((socket.gethostname(), 1234))

# receiving a message from server
msg = c.recv(1024)

# pprinting received message after decoding 
print(msg.decode())