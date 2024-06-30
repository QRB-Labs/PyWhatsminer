# PyWhatsminer
Unofficial python api-client for MicroBT Whatsminer ASICs
---
_Code adapted from a python file found in the Whatsminer Telegram group that is credited to `@passby`_


## Installation
Python 3.x is required. (Tested on Python 3.11 and newer)

```
pip install pywhatsminer
```

## Basic Usage
Instantiate a `Client` for each ASIC that you want to access. Then make read-only or writeable API calls by using the chapters and their methods.

Read-only information can be retrieved with just the ASIC's ip address:

```python
from pywhatsminer import Client

asic = Client(ip="192.168.0.117")

summary = asic.System.get_summary()
print(summary)
```
The methods of recording and interacting with the machine require authorization using an administrator password:
```python
from pywhatsminer import Client

asic = Client(ip="192.168.0.117", port=4028, password="SatoshiAnonymoto123")

asic.Power.off()
```
Tokens for writeable API calls are renewed automatically after they expire (30 minutes).

### Managing multiple ASICs
You could define a whole server farm's worth of Whatsminer ASICs and manage them all in one script:

```python
from pywhatsminer import Client

asics = [
    Client(ip="192.168.0.117", port=4028, password="123"),
    Client(ip="192.168.0.118", port=4028, password="123"),
    Client(ip="192.168.0.119", port=4028, password="123")
]

for asic in asics:
    if asic.System.get_summary().temperature > 80:
        asic.Power.off(respbefore=True)
```


## API Documentation
At the moment, the project is under development, so the documentation on the methods is not ready yet, but nevertheless, you can use the documentation on the methods of the Whatsminer API, which will repeat most of the names of the methods and their logic in the module.

[WhatsminerAPI-V2.0.5.pdf](docs/WhatsminerAPI-V2.0.5.pdf)


## Package distribution notes
_There are just notes to self for updating the pypi distribution_
* Update the release number in `setup.py` and commit to repo.
* Draft a new release in github using the same release number.
* Run `python setup.py sdist`
* Publish the distribution to pypi: `twine upload dist/*`

