class UnathorizedError(Exception):
    def __init__(self, message):
        super().__init__(message)


class WhatsminerAPIError(Exception):
    def __init__(self, message = None, code = None):
        super().__init__(f"[Error {code}] - {message}")


def ProcessError(code = None, message = None):
    if code == 14:
        raise WhatsminerAPIError("Invalid API command or data provided.", code)
    if code == 23:
        raise UnathorizedError("Your token must be enabled for write access to use this method. Use Client.enable_write_access() and provide admin password to enable it.")
    if code == 24:
        raise UnathorizedError("Your admin password is incorrect.")
    if code == 45:
        raise WhatsminerAPIError("Permission denied.", code)
    if code == 132:
        raise WhatsminerAPIError("Command error.", code)
    if code == 135:
        raise WhatsminerAPIError("Check token error.", code)
    if code == 136:
        raise WhatsminerAPIError("Limit of number of connections exceeded. Try to use Client(cache=True) after cooldown to save your auth_token data and reduce the number of connections.", code)
    if code == 137:
        raise WhatsminerAPIError("Base64 decoding error.", code)
    raise WhatsminerAPIError(message, code)
