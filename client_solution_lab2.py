# from the socket module import all 
from socket import *

# Create a TCP/IP socket
sock = socket(AF_INET, SOCK_STREAM)

myHostname = gethostname()
myHostIP = gethostbyname(myHostname)

# the machine address and port number have to be the same as the server is using.
server_address = (myHostname, 10000)
print('connecting to server at %s port %s' % server_address)
# Connect the socket to the host and port
sock.connect(server_address)

try:
    while True:
        message = input("Enter something: ")
        sock.sendall(message.encode())
        print('Client: "%s"' % message)
        if message == "end":
            break
        # Data is read from the connection with recv()
        while True:
            data = sock.recv(16).decode()
            print('Server: "%s"' % data)
            if len(data) < 16:
                break
        if data == "end":
            break

finally:
    print('closing socket')
    sock.close()