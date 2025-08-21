from contextlib import suppress

from datetime import datetime, timedelta


def process_response(response: dict) -> dict:
    if response.get("STATUS") == 'S':
        response['STATUS'] = 'success'
    elif response.get("STATUS") == 'E':
        response['STATUS'] = 'error'
    else:
        response['STATUS'] = None

    for key, value in response.items():
        if type(value) == dict:
            response[key] = process_response(value)
        elif type(value) == str:
            response[key] = value.strip()

            value_xlation = {
                'true': True,
                'false': False,
                'enable': True,
                'disable': False,
                'Alive': True,
                'Dead': False,
                'Y': True,
                'N': False,
                '': None
            }
            if value in value_x5n.keys():
                response[key] = value_xlation[value]

            if type(response[key]) == str and response[key].isdigit():
                response[key] = int(response[key])
            with suppress(ValueError, TypeError):
                response[key] = float(response[key]) if not isinstance(response[key], int) else response[key]

            key_xlation = {
                'When': datetime.fromtimestamp(response[key]),
                'Uptime': timedelta(seconds=response[key]),
                'Elapsed': timedelta(seconds=response[key]),
                'Upfreq Complete': bool(response[key]),
                'upfreq_complete': bool(response[key]),
                'enable': bool(response[key]),
            }

            if key in key_xlation.keys():
                response[key] = key_xlation[key]

    return response
