import socket
from threading import Thread





#import person into server 
#So it knows what a Person() object is, so it can reconstruct it when listening for ':' in msg
from a_person import Person

#Network will store all persons that joined and their information
from a_network import Network










class Server():
    
    
    def __init__(self, SERVER_HOST, SERVER_PORT):
        
        ## Setting up tcp socket connection and client connection list
    
        #Create a lsit of TCP connections
        self.client_sockets = []      
        # create a TCP socket
        self.sock = socket.socket()    
        # make the port as reusable port
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   
        # bind the socket to the address we specified
        self.sock.bind((SERVER_HOST, SERVER_PORT))
        # listen for upcoming connections
        self.sock.listen(5)
        print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
        
        
        ## Setting up network class that will be connected to servers
        
        self.network = Network(self.sock)

      
      
      
      
      
    def connection(self):
        
       
        while True:
            
            # we keep listening for new connections all the time
            client_socket, client_address = self.sock.accept()
            print(f"[+] {client_address} connected.")
            
            
            # add the new connected client to connected sockets
            self.client_sockets.append(client_socket)
            
            
            
            
            ##Start a thread that listens for messages when person connects, person information
            
            t = Thread(target=self.listening, args=(client_socket, client_address))
            # make the thread daemon so it ends whenever the main thread ends
            t.daemon = True
            # start the thread
            t.start()        
            
            
            
            
            
    
    
    
    def listening(self, client_socket, client_address):
        
        while True:
            try:
                msg = client_socket.recv(1024).decode()
            

            except:     
                #No connection means they disconnected so remove from network
                print("A Client Has Disconnected")
                self.network.remove_person_from_network(client_address)
                print(self.network)  
                break
            
            
            if ":" in msg:
                msg_split = msg.split(":")
                
                
                person_connected = Person(msg_split[0], msg_split[1], msg_split[2])
                
                #Set proper ip that was connected to server w
                person_connected.set_ipv4_address(client_address[0])
                
                
                #Apply secondary address because same network clients will have the same ip's so people playing on the same network
                #need to be differentiated from one another
                person_connected.set_client_addy_secondary(client_address[1])
                self.network.add_person_to_network(person_connected)
                print("{} has connected".format(person_connected.get_username()))
                print(self.network)
                
                
            else:
                
                user = self.network.find_username(self.client_sockets.index(client_socket))
                
                msg = "{}: {}".format(user, msg)
                for s in self.client_sockets:
                    if s != client_socket:
                        
                        try:
                            s.send(msg.encode())
                        except:
                            print("No one was there, connections are closed")
                    
                
                
                
            if not msg:
                #not there anymore remove from network
                
                print("A Client Has Disconnected")
                #testing
                #print(client_socket)
                #print(client_address)
                self.network.remove_person_from_network(client_address)
                print(self.network)
                break
                
                
                
    