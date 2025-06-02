import socket
from threading import Thread




class Network():
    
    
    def __init__(self, socket_connection):
        self.sock = socket_connection
        #List of Person() objects
        self.player_list = []  
        self.usernames = []
        self.passwords = []

        
        
    def __str__(self):
        
        out = "Network:"
        
        if len(self.player_list) == 0:
            out += "\nNo Players are connected"
        
        for i in range(0, (len(self.player_list))):
            out += "\nPlayer {} Active".format(self.player_list[i].get_username())
        
        
        return out
        
        
    def add_person_to_network(self, person):
        """
        pass Person() class from a_person.py
        will contain
        ipv4 address from each client
        their username
        their password
        some info about them
        all of these will be passed when the player is CONNECTING in the a_client.py file
        """
        self.player_list.append(person)
        self.usernames.append(person.get_username())
        self.passwords.append(person.get_password())
        
    
    
    def remove_person_from_network(self, client_address):
        """
        removes a person from the network when they disconnect from the server
        """
        
        
        #client_address returns a tuple where the first is the ipv4, use it to match which player left the network.
        #print(client_address[0], client_address[1])
        # Comments were for testing, this was giving me a lot of issues, originally i was using client_socket not address
        for p in self.player_list:
    
            if p.get_ipv4_address() == client_address[0]:
                
                if p.get_client_addy_secondary() == client_address[1]:
                    

                    self.player_list.remove(p)
    
    
    def find_username(self, n):
        return self.usernames[n]
                 
        
        
    """
    Need to make code that removes player from player list that corresponds to the client_socket that is closed in server when it prints 'A client Has Disconnected'
    this will be called there,
    they will also be removed from the a_SERVERCLASS self.client_sockets list
    so it needs to be removed from two areas when its called so that every point of connection is removed so theres no confusion
    """