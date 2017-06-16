# This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
server_port = 12345        # A port used by server for your service.

s.connect((host, server_port))
# Send data
message = '1,2,3,4,5,6'
s.send(message)
print s.recv(1024)
s.close 
