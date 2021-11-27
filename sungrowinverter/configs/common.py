"""Sensor Entity Description for the Growatt integration."""
from __future__ import annotations

from dataclasses import dataclass

TEMP_CELSIUS = "°C"
KILO_WATT_HOUR = "kWh"
WATT = "W"
KILO_WATT = "kW"
KILOGRAMS = "kg"
PERCENTAGE = "%"
VOLTAGE = "V"
AMPERE = "A"
HERTZ = "Hz"
CHARGE_CURRENT = "C"
VOLT_AMPS = "VA"
HOUR = "h"
MINUTE = "min"

@dataclass
class ModBusRegister:
    """Describes a modbus register to be called"""

    address: int
    key: str
    data_type: str

    transform: str | None = None
    unit_precision: float | None = None
    unit_of_measure: str | None = None
    table: dict[int:str] | None = None
    description: str | None = None
    length: int | None = None
    valid_inverters: list | None = None
    dataset: str | None = None

    def __init__(self, address, key, data_type, unit_precision=None, unit_of_measure=None, table=None, description=None, transform=None, length=None, valid_inverters=None, dataset=None) -> None:
        self.address = address
        self.key = key
        self.data_type = data_type
        self.length = length
        self.transform = transform
        self.unit_precision = unit_precision
        self.unit_of_measure = unit_of_measure
        self.table = table
        self.description = description
        self.valid_inverters = valid_inverters
        self.dataset = dataset

@dataclass
class SungrowInverterModel:
    """Describes a Sungrow Inverter"""

    device_code: int
    model: str
    inverter_type: str
    mppt_inputs: int | None = None

    serial_number: str | None = None
    nominal_output_power: str | None = None

    def __init__(self, device_code, model, inverter_type, mppt_inputs=None, nominal_output_power=None, serial_number=None) -> None:
        self.device_code = device_code
        self.model = model
        self.inverter_type = inverter_type
        self.mppt_inputs = mppt_inputs
        self.nominal_output_power = nominal_output_power
        self.serial_number = serial_number


OUTPUT_TYPE_CODES: dict = {
    0: "Single phase",
    1: "Three phase (3P4L)",
    2: "Three phase (3P3L)",
}

GRID_STATE_CODES = {
    0xAA: "Off Grid",
    0x55: "On Grid",
}

BATTERY_TYPES = {
    0: "Lead-acid Narada",
    1: "Li-ion Samsung",
    2: "No Battery",
    3: "Lead-acid Other",
    4: "Li-ion US2000A",
    5: "Li-ion LG",
    6: "Li-ion US2000B",
    7: "Li-ion GCL",
    8: "Li-ion Bluesun",
    9: "Li-ion Sungrow",
    10: "Li-ion BYD",
}