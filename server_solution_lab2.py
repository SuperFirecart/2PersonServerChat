# from the socket module import all 
from socket import *
import os.path
import time

# Create a TCP/IP socket
sock = socket(AF_INET, SOCK_STREAM)
# if we did not import everything from socket, then we would have to write the previous line as:
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

myHostname = gethostname()
myHostIP = gethostbyname(myHostname)

# set values for host 'localhost' - meaning this machine and port number 10000
server_address = (myHostname, 10000)
# output to terminal some info on the address details
print('*** Server is starting up on %s port %s ***' % server_address)
# Bind the socket to the host and port
sock.bind(server_address)

# Listen for one incoming connections to the server
sock.listen(1)

# we want the server to run all the time, so set up a forever true while loop
while True:
    # Now the server waits for a connection
    print('*** Waiting for a connection ***')
    # accept() returns an open connection between the server and client, along with the address of the client
    connection, client_address = sock.accept()
    
    try:
        print('connection from', client_address)
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16).decode()
            print('Client: "%s"' % data)
            if data == "end":
                break
            if len(data) < 16:
                message = input("Enter something: ")
                print('sending "%s"' % message)
                connection.sendall(message.encode())
                if message == "end":
                    break
            
    finally:
        # Clean up the connection
        connection.close()
        break
        
sock.close();
