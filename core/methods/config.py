from core.api import WhatsminerAPI, WhatsminerAccessToken
from typing import Any


class Config:
    def __init__(self, client):
        self.client = client
        self.api: WhatsminerAPI = client.api
        self.token: WhatsminerAccessToken = client._access_token
        
        
    def open_ssh(self) -> Any:
        """
        This operation opens miner's SSH server.
        """
        return self.api.exec_command(self.token, "ssh_open")
    

    def close_ssh(self) -> Any:
        """
        This operation closes miner's SSH server.
        """
        return self.api.exec_command(self.token, "ssh_close")
    