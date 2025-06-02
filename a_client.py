from a_CLIENTCLASS import Client
from a_person import Person
from a_modern_ui import Modern_ui
#from chat_ui import Chat
import socket

"""
Client() class is found in a_CLIENTCLASS.py

The class establishes the connection, the variables are passed here.
And connection is closed here in a_client.py
"""




  

#Variables
#143.42.8.236 - cloud
#

SERVER_HOST = "143.42.8.236" #- linode server named "Tutorial"
#SERVER_HOST = "10.102.155.3"
SERVER_PORT = 9000



#Create the Client connection with the Client() class
client = Client(SERVER_HOST, SERVER_PORT)



#Create and pop up the username login page
modern_ui = Modern_ui()

username = modern_ui.username
password = modern_ui.password





#Create the person class to hold the information of the client that is connecting that he just input
person = Person(client.server_host, username, password)
#print(person)
client.pass_person(person)





#call the clients chat object
client.call_chat(username)




#client closed
client.sock.close()
    
    
    
    
