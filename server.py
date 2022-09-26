import socket;




def server_program():
    print('starting socket server...')
     # get the hostname
    host = socket.gethostname();
    port = 5000; # initiate port no above 1024

    server_socket = socket.socket();  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port));  # bind host address and port together
    
    #configure how many clientes the server can listen simultaneously
    server_socket.listen(2);
    
    print('socket server started at:    host: ' + str(host) + '    port: ' + str(port))
    
    conn, adress = server_socket.accept(); #accept new connection
    print('connection from : '+ str(adress))
    
    while True:
        #receive data stream
        data = conn.recv(10240).decode();
        
        if not data: 
            break
        
        print('message from connected user: ' + str(data))
        
        # data = input(' -> ')
        # conn.send(data.encode())
        
    conn.close()
    
    
if __name__ == '__main__':
    server_program()

