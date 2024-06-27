from core.api import WhatsminerAPI, WhatsminerAccessToken
from core.models import PSU, PSU_Message
from core.utils import process_response

from typing import Any


class Power:
    def __init__(self, client):
        self.client = client
        self.api: WhatsminerAPI = client.api
        self.token: WhatsminerAccessToken = client._access_token
        
    
    def on(self) -> Any:
        """
        This operation simply starts mining and turns on the power output of the power board.
        """
        return self.api.exec_command(self.token, "power_on")
    

    def off(self, respbefore: bool = False) -> Any:
        """
        This operation simply stops mining and turns off the power output of the power board.
        There was no power outage on the control board
        
        Params:
            - respbefore: bool = False - when true, the miner returns the data first and then closes the hashboard, otherwise close the hashboard first and then return the data.
        """
        return self.api.exec_command(self.token, "power_off", {"respbefore": respbefore})
        
    
    def restart(self) -> Any:
        """
        This operation restarts the miner.
        """
        return self.api.exec_command(self.token, "restart_btminer")
    
    
    def switch_mode(self, mode: str) -> Any:
        """
        This operation changes miner's power mode.
        
        Params:
            - mode: str - new power mode. Possible fields: "low", "normal", "high"
        """
        assert mode in ["low", "normal", "high"]
        
        return self.api.exec_command(self.token, "switch_mode", {"mode": mode})


    def get_psu(self) -> Any:
        """
        This method returns miner's power system status.
        """
        data = process_response(self.api.exec_command(self.token, "get_psu"))
        message = PSU_Message(*data['Msg'].values())
        data.update({"Msg": message})

        return PSU(*data.values())