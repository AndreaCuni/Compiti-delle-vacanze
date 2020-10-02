"""
Cuniberti Andrea
Class: 5 A ROB
Server ECHO UDP 
"""
import socket
import threading

#setting the tupla
server_adress = '127.0.0.1'
sever_port = 5000

#setting the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#binding the server
server.bind((server_adress, sever_port))   

def solver(data_connection,client_adress):

    while(True):

        data = data_connection.recv(4096)  

        #check for a closing message
        if(data.decode() == "close()"):
            break

        print(str(client_adress) + ": \t" + data.decode())    

        #sendin' results
        data_connection.sendall(data)

    #closing the socket
    server.close()

def main():

    users = []

    while (True):

        #waiting for a connection
        server.listen()

        #connection established
        data_connection, client_adress = server.accept()
        users.append(threading.Thread(target = solver, args=(data_connection,client_adress)))

        users[-1].start()

    for k in users:
        k.join()

if __name__ == "__main__":
    main()
