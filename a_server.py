from a_SERVERCLASS import Server

    

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 9000 
server = Server(SERVER_HOST, SERVER_PORT)
server.connection()
        
        
        
        
        
        
        # close client sockets
for cs in server.client_sockets:
    cs.close()
# close server socket
server.sock.close()    




