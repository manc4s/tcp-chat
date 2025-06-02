# tcp-chat



*************
WARNING
THIS CODE WAS DONE ON THE FLY AND IS VERY UNCOMMENTED, ALSO THE CODE FILES ARE NAMED THAT WAY BECAUSE I WAS CODING USING WING101 IDE AND IT WAS JUST EASIER TO ORIENT THE FILES THAT WAY
******************



python socket connection, using python customtkinter module for gui login and chat portion, uses Linode for server.




The a_CLIENTCLASS, a_modern_ui, a_person, a_chat_ui, a_client
must all be run from the same client, all in the same folder, you only must run a_client.py.



On the Server side, In my Case the Linode server, holds the following files
a_person.py a_SERVERCLASS.py a_server.py   a_network.py 

on the server,
go into putty then when you establish the connection, and have trasnfered over the 4 files using WIN scp or your file transfer
software of choice, then you go into putty, make a new directory, and then run the server side,

- python3 a_server.py 

to keep it running even when putty is closed

- screen python3 a_server.py


Once the a_server.py is running and listening for connections, clients can start connecting by running a_client.py from their devices, because the linode server
will allow them to all connect to it with a_server.py running. 
