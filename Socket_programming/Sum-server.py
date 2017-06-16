 # This is server.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
server_port = 12345         # Reserve a port in server for your service.
s.bind((host, server_port)) # Bind the server to the socket address (host+server_port)

s.listen(5)                 # Server specifies atmost 5 client request it receives before any ignoring any service request
while True:   # Waiting for client connection 
   client_port, addr = s.accept()     # Establish connection with client. Here, client_port is port used by client and addr is his IP addr.
   print 'Got connection from', addr
   #print client_port.recv(1024)       # recv(1024) receives max. 1024 bytes from client
   num_string = client_port.recv(1024)
   num_list = num_string.split(',')
   print num_list
   sum_result = 0
   for element in num_list:
	   sum_result += int(element) 
   result = "sum of given nos. is :"+str(sum_result)
   client_port.send(result) # Send the data to client via. client_port
   client_port.close()                # Close the connection
