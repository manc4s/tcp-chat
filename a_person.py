class Person():
    
    
    def __init__(self, ipv4_address, username, password):
        
        self._ipv4_address = ipv4_address
        self._username = username 
        self._password = password
        self._client_addy_secondary = None
        
    def __str__(self):
        
        return "address : {}\nusername : {}\npassword : {}".format(self._ipv4_address, self._username, self._password)
        
        
        
    def get_ipv4_address(self):
        return self._ipv4_address
    
    
    
    def get_username(self):
        return self._username

    
    
    def get_password(self):
        return self._password
    
    
    def get_client_addy_secondary(self):
        return self._client_addy_secondary
    
    
    def set_ipv4_address(self, other):
        self._ipv4_address = other
    
    
    def set_username(self):
        pass
    
    
    def set_password(self):
        pass
    
    
    
    def set_client_addy_secondary(self, address):
        self._client_addy_secondary = address