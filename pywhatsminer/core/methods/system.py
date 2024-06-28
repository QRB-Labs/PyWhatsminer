from pywhatsminer.core.api import WhatsminerAPI, WhatsminerAccessToken
from pywhatsminer.core.models import Summary, Status, Api, Dev, Devs, DevDetail, DevDetails, Pool, Pools, Info, ErrorCode, Errors
from pywhatsminer.core.utils import process_response

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
    
    
    def download_logs(self) -> Any:
        """
        This operation downloads miner's logs.
        """
        return self.api.exec_command(self.token, "download_logs")
    
    
    # TODO: Check status model
    def get_status(self) -> Status:
        """
        This method returns miner's status.
        
        WARNING: Response model can be incorrect. Will be fixed in the future.
        """
        data = process_response(self.api.get_read_only_info(self.token, "status"))

        return Status(*data['Msg'].values())
    
    
    def get_summary(self) -> Summary:
        """
        This method returns miner's summary.
        """
        data = process_response(self.api.get_read_only_info(self.token, "summary"))
        summary = process_response(data['SUMMARY'][0])
        
        return Summary(*summary.values())
    
    
    def get_api_version(self) -> Api:
        """
        This method returns miner's API version.
        """
        data = process_response(self.api.get_read_only_info(self.token, "get_version"))
    
        return Api(*data['Msg'].values())
    
    
    def get_dev_details(self) -> DevDetails:
        """
        This method returns miner's device details.
        """
        data = self.api.get_read_only_info(self.token, "devdetails")
        devdetails = DevDetails(details=[])
        
        for devdetail in data['DEVDETAILS']:
            devdetail = process_response(devdetail)
            devdetail.pop('ID')
            devdetails.details.append(DevDetail(*devdetail.values()))
    
        return devdetails
    
    
    def get_devs(self) -> Devs:
        """
        This method returns information for each hash board.
        """
        data = self.api.get_read_only_info(self.token, "devs")
        devs = Devs(devs=[])
    
        for dev in data['DEVS']:
            dev = process_response(dev)
            devs.devs.append(Dev(*dev.values()))
    
        return devs
    
    
    def get_pools(self) -> Pools:
        """
        This method returns pool miner information.
        """
        data = self.api.get_read_only_info(self.token, "pools")
        pools = Pools(pools=[])
        
        for pool in data['POOLS']:
            pool = process_response(pool)
            pools.pools.append(Pool(*pool.values()))
            
        return pools    
    
    
    def get_miner_info(self, *fields: str) -> Any:
        """
        This method returns miner's information.
        Params:
            - *fields: str - you can select the fields that you want to return, returns all if not specified.
        
        `WARNING`: looks like fields are not working, in any case api returns all fields in response.
        """
        data = self.api.get_read_only_info(self.token, "get_miner_info", {'info':f"{",".join(fields)}"})
        info = Info(**data['Msg'])
        
        return info
    
    
    # TODO: Implement this
    def get_error_codes(self) -> Any:
        """
        This method returns miner's error codes.
        
        `WARNING`: This method actually don't parse response and gives raw json in response. Will be implemented in the future.
        """
        data = self.api.get_read_only_info(self.token, "get_error_code")
        
        return data

    
    # TODO: Implement this
    @deprecated(reason="Not work. Will be implemented in the future.")
    def get_token(self) -> Any:
        """
        This method returns miner's access token.
        
        `WARNING`: This method actually don't work. Will be implemented in the future.
        """
        return self.api.get_read_only_info(self.token, "get_token")
    