"""
Cuniberti Andrea
Class: 5 A ROB
Client ECHO TCP
"""
import socket

#setting the tupla
server_adress = '127.0.0.1'
server_port = 5000

#setting the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#establish a connection...
client.connect((server_adress,server_port))

while(True):
    #sending a message
    mex = input("message: ")
    client.sendall(mex.encode())
    
    #check for a closing message
    if(mex == "close()"):
        break

    echo = client.recv(4096) 

    print("this is the result: " + echo.decode())

#closing the socket
client.close()