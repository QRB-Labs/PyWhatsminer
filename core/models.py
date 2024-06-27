from dataclasses import dataclass
from dataclasses_json import dataclass_json

from datetime import datetime, timedelta


@dataclass_json
@dataclass
class Summary:
    elapsed: int
    mhs_avg: float
    mhs_5s: float
    mhs_1m: float
    mhs_5m: float
    mhs_15m: float
    hs_rate: float
    accepted: int
    rejected: int
    total_mh: float
    temperature: float
    avg_frequency: int
    fan_speed_in: int
    fan_speed_out: int
    power_watts: int
    power_rate: float
    pool_rejected_percent: float
    pool_stale_percent: float
    uptime: timedelta
    target_frequency: int
    target_mhs: float
    env_temp: float
    power_mode: str
    factory_ghs: int
    power_limit: int
    chip_temp_min: float
    chip_temp_max: float
    chip_temp_avg: float
    btminer_fast_boot_enabled: str
    upfreq_complete: bool
    

# TODO: Validate models, maybe incorrect. Needs some tests.
@dataclass_json
@dataclass
class StatusMessage:
    miner_off: bool
    miner_off_reason: str
    miner_off_time: int
    firmware_version: str
    power_mode: str
    power_limit_set: bool
    hash_percent: int
    
    
@dataclass_json
@dataclass
class Status:
    status: str
    when: datetime
    code: int
    message: StatusMessage
    description: str
    

@dataclass_json
@dataclass
class PSU_Message:
    name: str
    hardware_version: str
    software_version: str 
    model: str
    enabled: bool
    iin: int
    vin: int
    pin: int
    fan_speed: int
    serial_no: str
    vendor: int
    temperature: float


@dataclass_json
@dataclass
class PSU:
    status: str
    when: datetime
    code: int
    message: dict
    description: str