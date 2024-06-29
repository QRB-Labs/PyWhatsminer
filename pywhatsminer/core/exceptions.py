class UnathorizedError(Exception):
    def __init__(self, message):
        super().__init__(message)
        
        
class WhatsminerAPIError(Exception):
    def __init__(self, message = None, code = None):
        super().__init__(f"[Error {code}] - {message}")
        
            
def ProcessError(code = None, message = None):
    match code:
        case 14:
            raise WhatsminerAPIError("Invalid API command or data provided.", code)
        case 23:
            raise UnathorizedError("Your token must be enabled for write access to use this method. Use Client.enable_write_access() and provide admin password to enable it.")
        case 24:
            raise UnathorizedError("Your admin password is incorrect.")
        case 45:
            raise WhatsminerAPIError("Permission denied.", code)
        case 132:
            raise WhatsminerAPIError("Command error.", code)
        case 135:
            raise WhatsminerAPIError("Check token error.", code)
        case 136:
            raise WhatsminerAPIError("Limit of number of connections exceeded. Try to use Client(cache=True) after cooldown to save your auth_token data and reduce the number of connections.", code)
        case 137:
            raise WhatsminerAPIError("Base64 decoding error.", code)
        case _:
            raise WhatsminerAPIError(message, code)
        