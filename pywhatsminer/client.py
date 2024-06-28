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
    def __init__(self, ip: str, port: int = 4028, password: str | None = "admin"):
        self._access_token = WhatsminerAccessToken(ip, port, password)
        self.api = WhatsminerAPI()

        self.Power = Power(self)
        self.System = System(self)
        self.Config = Config(self)