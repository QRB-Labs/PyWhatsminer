from pywhatsminer.core import WhatsminerAccessToken, WhatsminerAPI
from pywhatsminer.core.methods.power import Power
from pywhatsminer.core.methods.system import System
from pywhatsminer.core.methods.config import Config


class Client:
    """
    ## The basic client object for interacting with the Whatsminer API
    
    `Simple usage case:`
    ```Python
    from pywhatsminer import Client
    
    asic = Client(ip="192.168.0.117", port=4028, password="SatoshiAnonymoto123")
    
    asic.Power.on()
    ```
    """
    def __init__(self, ip: str, port: int = 4028, password: str | None = None):
        self._access_token = WhatsminerAccessToken(ip, port, password)
        self.api = WhatsminerAPI()

        self.Power = Power(self)
        self.System = System(self)
        self.Config = Config(self)
        
        
    def enable_write_access(self, password: str):
        self._access_token.enable_write_access(password)
        
    
    def __repr__(self):
        return f"Client(ip={self._access_token.ip_address}, port={self._access_token.port}, password={self._access_token._admin_password})"
    

    def __str__(self):
        return f"Client(ip={self._access_token.ip_address}, port={self._access_token.port}, password={self._access_token._admin_password})"
    
    
    def __eq__(self, other):
        return self._access_token == other._access_token
    
    
    def __hash__(self):
        return hash(self._access_token)
