from email import message
import socket

import psutil;




def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    print('socket client started at:    host: ' + str(host) + '    port: ' + str(port))

    size = 0
    
    while True:
        
        message = str([i.info for i in psutil.process_iter(['name', 'status']) if i.info['status'] == 'running'])
        print(size)
        
        if len(message) != size:
            
            client_socket.send(message.encode())
            size = len(message)
            
        
        size = len(message)

    # message = 'qwe'
    
    # for i in psutil.process_iter(['name', 'status']):
    
    #     if i.info['name'] == 'chrome':
            
    #         message = str(i.info)
    

    # while message.lower().strip() != 'bye':
    #     client_socket.send(message.encode())  # send message
    #     data = client_socket.recv(1024).decode()  # receive response

    #     print('Received from server: ' + data)  # show in terminal

    #     message = input(" -> ")  # again take input

    # client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()