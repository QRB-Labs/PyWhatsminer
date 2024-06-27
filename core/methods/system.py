from core.api import WhatsminerAPI, WhatsminerAccessToken
from core.models import Summary, Status, StatusMessage
from core.utils import process_response

from typing import Any

from deprecated import deprecated


class System:
    """
    This class provides methods for miner's system.
    """
    def __init__(self, client):
        self.client = client
        self.api: WhatsminerAPI = client.api
        self.token: WhatsminerAccessToken = client._access_token
        
    
    def reboot(self) -> Any:
        """
        This operation simply reboots miner's system.
        """
        return self.api.exec_command(self.token, "reboot")


    def reset(self) -> Any:
        """
        This operation resets the miner to factory settings.
        """
        return self.api.exec_command(self.token, "factory_reset")
    
    
    # TODO: Check status model
    def get_status(self) -> Any:
        """
        This method returns miner's status.
        
        WARNING: Response model can be incorrect. Will be fixed in the future.
        """
        data = process_response(self.api.exec_command(self.token, "status"))
        message = StatusMessage(*data['Msg'].values())
        data.update({"Msg": message})

        return Status(*data.values())
    
    
    def get_summary(self) -> Any:
        """
        This method returns miner's summary.
        """
        data = process_response(self.api.exec_command(self.token, "summary"))
        summary = process_response(data['SUMMARY'][0])
        
        return Summary(*summary.values())
    
    
    def get_api_version(self) -> Any:
        """
        This method returns miner's API version.
        """
        return self.api.exec_command(self.token, "get_version")
    
    
    def get_dev_details(self) -> Any:
        """
        This method returns miner's device details.
        """
        return self.api.exec_command(self.token, "details")
    
    
    def get_devs(self) -> Any:
        """
        This method returns information for each hash board.
        """
        return self.api.exec_command(self.token, "devs")
    
    
    def get_pools(self) -> Any:
        """
        This method returns pool miner information.
        """
        return self.api.exec_command(self.token, "pools")
    
    
    # TODO: Implement this
    @deprecated(reason="Not work. Will be implemented in the future.")
    def get_token(self) -> Any:
        """
        This method returns miner's access token.
        
        WARNING: This method actually not work. Will be implemented in the future.
        """
        return self.api.exec_command(self.token, "get_token")
    