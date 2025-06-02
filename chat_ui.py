import customtkinter
from functools import partial
import keyboard
from threading import Thread


class Chat():
    
    
    def __init__(self, client_socket, username):
    
        customtkinter.set_appearance_mode("dark")
        #"blue, green, dakr-blue"
        customtkinter.set_default_color_theme("green")


        self.root = customtkinter.CTk()
        self.root.geometry = ("500x350")
        
        self.client_socket = client_socket
        self.user_username = username
        
        self.line = "0.1"
        
        self.textbox = customtkinter.CTkTextbox(master=self.root, width=500)
        #self.textbox.pack(pady=0, padx=0, fill = "both", expand=True, side=customtkinter.TOP)
        #textbox.grid(row=0, column=0)
        #self.textbox.insert(self.line, "HI THERE") 
        #self.textbox.insert(self.line, "Yo")
        
        self.frame = customtkinter.CTkFrame(master=self.root)
        #frame.pack(pady=5, padx=5, fill="both", expand=True)
        
        

            
        
        
        #label = customtkinter.CTkLabel(master=frame, text="Chat")
        #label.pack(pady=0, padx=200)
        
        
       
        

        
        #self.checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
        #self.checkbox.pack(pady=12, padx=10)
        
        
        
        self.button = customtkinter.CTkButton(master=self.frame, width = 20, text="Send", command=self.send_button_clicked)#partial(login, entry1.get(), entry2.get(), checkbox.get())
        #button.pack(anchor='se', pady=0, padx=10, side=customtkinter.BOTTOM)
        
        
        
        self.chatmessage = customtkinter.CTkEntry(master=self.frame, width = 500, placeholder_text="Type Here")
        #self.chat.pack(pady=(0,0), padx=0, side=customtkinter.BOTTOM)
        
        
        
        
        
        
        
        
        

    
    
    def chat_show(self):
        
        self.textbox.pack(pady=0, padx=0, fill = "both", expand=True, side=customtkinter.TOP)
        self.frame.pack(pady=5, padx=5, fill="both", expand=True)
        self.button.pack(anchor='se', pady=0, padx=10, side=customtkinter.BOTTOM)
        self.chatmessage.pack(pady=(0,0), padx=0, side=customtkinter.BOTTOM)
    
    
        self.root.mainloop()        



    def __str__(self):
        return  "{}'s chat box".format(self.user_username)
    
    

    def send_button_clicked(self):
           
        self.chat_newline()
        chat = "{}\n".format(self.chatmessage.get())
          
        self.client_socket.send(chat.encode())
        self.textbox.insert(self.line, chat)
            #Closes the UI 
            #self.root.destroy()
            
            
        if self.chatmessage.get() == "quit":
            self.root.destroy()        
            
            
    def chat_newline(self):
        self.line = float(self.line)
        self.line += 1
        self.line = str(self.line)     
        
    
    
   
        
            
            

#x = Chat("ok", "hi")
#print(x)
#x.show()