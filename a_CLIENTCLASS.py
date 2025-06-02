import socket
import random
from threading import Thread
from datetime import datetime
import time


#import a_person file because it needs to know what a Person() object is.
import a_person
from chat_ui import Chat




class  Client():
    
    def __init__(self, SERVER_HOST, SERVER_PORT):

        # initialize TCP socket to self.sock
        self.sock = socket.socket()
        print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
        
        
        # connect to the server
        self.sock.connect((SERVER_HOST, SERVER_PORT))
        print("[+] Connected.")
        
        self.server_host = SERVER_HOST
        
        self.chat = None
        
        
        
        
        
        
        
        self.t = Thread(target=self.listen_for_messages, args = (self.sock,))
        # make the thread daemon so it ends whenever the main thread ends
        self.t.daemon = True
        # start the thread
        self.t.start()
        
        
        

        
    def pass_person(self, person):
        """
        passes a Person() object from a_client when the player inputs all the information
        this persons information will be broken down and sent over to the server which will then be pushed to the network class
        """
        
        msg = "{}:{}:{}".format(person.get_ipv4_address(), person.get_username(), person.get_password())
        
        #Send the player info to the socket 
        self.sock.send(msg.encode())
        
        
        
    
    
    
    def listen_for_messages(self, cs):
        while True:
            message = cs.recv(1024).decode()
            
            message += "\n"
            #print(self.chat)
            if self.chat != None:
                #print("got to here")
                self.chat.chat_newline()            
                self.chat.textbox.insert(self.chat.line, message)
                        
            #print(message)
        
        
        
        
    def call_chat(self, username):
        self.chat = Chat(self.sock, username)
  
        self.chat.textbox.insert(self.chat.line, "{}\n".format(self.chat))
        self.chat.chat_newline()
        
        self.chat.chat_show()
        
        
        
        
    
    
