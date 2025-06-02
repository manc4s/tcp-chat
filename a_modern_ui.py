import customtkinter
from functools import partial






class Modern_ui():
    
    
    def __init__(self):
    
        customtkinter.set_appearance_mode("dark")
        #"blue, green, dakr-blue"
        customtkinter.set_default_color_theme("green")


        self.root = customtkinter.CTk()
        self.root.geometry = ("500x350")
        
        
        frame = customtkinter.CTkFrame(master=self.root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        
        
        
        label = customtkinter.CTkLabel(master=frame, text="Login System")
        label.pack(pady=12, padx=10)
        
        
        self.username = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
        self.username.pack(pady=12, padx=10)
        
        
        self.password = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
        self.password.pack(pady=12, padx=10)
        
        
        
        #self.checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
        #self.checkbox.pack(pady=12, padx=10)
        
        
        
        button = customtkinter.CTkButton(master=frame, text="Login", command=self.login_button_clicked)#partial(login, entry1.get(), entry2.get(), checkbox.get())
        button.pack(pady=12,padx=10)
        
        
        button_create = customtkinter.CTkButton(master=frame, text="Create Account", command=self.login_button_clicked)#partial(login, entry1.get(), entry2.get(), checkbox.get())
        button_create.pack(pady=12,padx=10)        
        
        
        
        self.root.mainloop()        





    def login_button_clicked(self):
            self.username = self.username.get()
            self.password = self.password.get()
           
            
            #Closes the UI 
            self.root.destroy()
            
         
    


