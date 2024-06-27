from core.api import WhatsminerAccessToken, WhatsminerAPI
from core.methods.power import Power
from core.methods.system import System
from core.methods.config import Config


class Client:
    def __init__(self, ip: str, port: int = 4028, password: str | None = "admin"):
        self._access_token = WhatsminerAccessToken(ip, port, password)
        self.api = WhatsminerAPI()

        self.Power = Power(self)
        self.System = System(self)
        self.Config = Config(self)