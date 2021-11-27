"""
#
# Sungrow Grid Connect String Inverter Series
#
# Valid device types:
#   SG3.0RT, SG4.0RT, SG5.0RT, SG6.0RT, SG7.0RT，SG8.0RT, SG10RT, SG12RT, SG15RT, SG17RT, SG20RT
#   SG30KTL-M, SG30KTL-M-V31, SG33KTL-M, SG36KTL-M, SG33K3J, SG49K5J, SG34KJ, LP_P34KSG,
#   SG50KTL-M-20, SG60KTL, G80KTL, SG80KTL-20, SG60KU-M
#   SG5KTL-MT, SG6KTL-MT, SG8KTL-M, SG10KTL-M, SG10KTL-MT, SG12KTL-M, SG15KTL-M,
#   SG17KTL-M, SG20KTL-M,
#   SG80KTL-M, SG85BF, SG80HV, SG80BF, SG110HV-M, SG111HV, SG125HV, SG125HV-20
#   SG25CX-SA, SG30CX, SG33CX, SG40CX, SG50CX, SG36CX-US, SG60CX-US, SG75CX, SG100CX
#   SG100CX-JP, SG110CX, SG136TX, SG225HX, SG250HX
#   SG250HX-IN, SG250HX-US
#
#   Discontinued (as @ 2021-07-12):
#   SG30KTL, SG10KTL, SG12KTL, SG15KTL, SG20KTL, SG30KU, SG36KTL, SG36KU, SG40KTL,
#   SG40KTL-M, SG50KTL-M, SG60KTL-M, SG60KU
#
# Sungrow string inverter register definitions
"""

from sungrowinverter.configs.common import (
    ModBusRegister,
    TEMP_CELSIUS,
    KILO_WATT_HOUR,
    WATT,
    VOLTAGE,
    AMPERE,
    HERTZ,
    OUTPUT_TYPE_CODES,
    HOUR,
    MINUTE,
    VOLT_AMPS,
)

DEVICE_WORK_STATE_1_CODES = {
    0x0:    "Run",
    0x8000: "Stopped",
    0x1300: "Key stop",
    0x1500: "Emergency stop",
    0x1400: "Standby",
    0x1200: "Initial standby",
    0x1600: "Starting",
    0x9100: "Alarm run",
    0x8100: "Derating run",
    0x8200: "Dispatch run",
    0x5500: "Fault",
}

DEVICE_WORK_STATE_2_CODES = {
    0b0000000000000000001: "status_run",
    0b0000000000000000010: "status_stop",
    0b0000000000000000100: "status_key_stop",
    0b0000000000000001000: "status_initial_standby",
    0b0000000000000010000: "status_standby",
    0b0000000000000100000: "status_emergency_stop",
    0b0000000000001000000: "status_starting",
    0b0000000001000000000: "status_fault",
    0b0000000010000000000: "status_alarm_run",
    0b0000000100000000000: "status_derating_run",
    0b0000001000000000000: "status_dispatch_run",
    0b0000010000000000000: "status_communicate_fault",
    0b0100000000000000000: "status_grid_connected",
    0b1000000000000000000: "status_fault_stop",
}

COUNTRY_CODES = {
    61: "America",
    98: "America(1741-SA)",
    59: "America(Hawaii)",
    97: "America(ISO-NE)",
    27: "Arab Emirates",
    6: "Australia",
    20: "Australia (West)",
    5: "Austria",
    25: "Austria (Vorarlberg)",
    8: "Belgium",
    66: "Brazil",
    60: "Canada",
    65: "Chile",
    14: "China",
    67: "Chinese Taipei",
    7: "Czech",
    9: "Denmark",
    76: "EN50549-1 Europe",
    77: "EN50549-2 Europe",
    40: "Finland",
    2: "France",
    1: "Germany",
    0: "Great Britain",
    11: "Greece (Island)",
    10: "Greece (Land)",
    29: "Hungary",
    26: "IND India",
    41: "Ireland",
    28: "Israel",
    3: "Italy",
    69: "Japan",
    63: "Korea",
    30: "Malaysia",
    170: "Mexico",
    12: "Netherlands",
    38: "Oman",
    16: "Other 50Hz",
    62: "Other 60Hz",
    31: "Philippines",
    32: "Poland",
    34: "Poland",
    13: "Portugal",
    17: "Romania",
    39: "Sandi Arabia",
    64: "South Africa",
    4: "Spain",
    15: "Sweden",
    18: "Thailand",
    35: "Thailand-MEA",
    19: "Turkey",
    36: "Vietnam",
}

# the scan register start 1 less than the actual register recorded in specs.
# reason being registers start at 0, document for modbus usually refers to register 1 as the start of registers.
STRING_SCAN = {
    "read": [
        {"scan_start": 4999, "scan_range": 114},
        {"scan_start": 5114, "scan_range": 40},
        {"scan_start": 7012, "scan_range": 24},
        # {"scan_start": 6199, "scan_range": 100},
        # {"scan_start": 6399, "scan_range": 100},
        # {"scan_start": 6499, "scan_range": 100},
    ],
    "holding": [
        {"scan_start": 4999, "scan_range": 6},
        {"scan_start": 12999, "scan_range": 101},
    ],
}

STRING_READ_REGISTERS: tuple[ModBusRegister, ...] = (
    ModBusRegister(5002, "output_type", "U16", table=OUTPUT_TYPE_CODES),
    ModBusRegister(5003, "daily_power_yield", "U16", 0.1, KILO_WATT_HOUR),
    ModBusRegister(5004, "total_power_yield", "U32", unit_of_measure=KILO_WATT_HOUR),
    ModBusRegister(5005, "total_running_time", "U32", unit_of_measure=HOUR),
    ModBusRegister(5008, "inside_temperature", "U16", 0.1, TEMP_CELSIUS, description="Internal inverter temperature"),
    ModBusRegister(5009, "total_aparent_power", "U32", unit_of_measure=VOLT_AMPS),
    ModBusRegister(5011, "mppt_1_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5012, "mppt_1_current", "U16", 0.1, AMPERE),
    ModBusRegister(5013, "mppt_2_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5014, "mppt_2_current", "U16", 0.1, AMPERE),
    ModBusRegister(5015, "mppt_3_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5016, "mppt_3_current", "U16", 0.1, AMPERE),
    ModBusRegister(5017, "total_dc_power", "U32", unit_of_measure=WATT, description="PV power that is usable (inverter after inefficiency)"),
    ModBusRegister(5019, "grid_voltage", "U16", 0.1, VOLTAGE), # here for single phase only (not applicable for 3 phase)
    ModBusRegister(5019, "phase_a_voltage", "U16", 0.1, VOLTAGE, description="Phase A (1-2) voltage is also the grid voltage on a single phase inverter"),
    ModBusRegister(5020, "phase_b_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5021, "phase_c_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5022, "phase_a_current", "U16", 0.1, AMPERE),
    ModBusRegister(5023, "phase_b_current", "U16", 0.1, AMPERE),
    ModBusRegister(5024, "phase_c_current", "U16", 0.1, AMPERE),
    ModBusRegister(5031, "total_active_power", "U32", unit_of_measure=WATT),
    ModBusRegister(5033, "total_reactive_power", "S32", unit_of_measure="var"),
    ModBusRegister(5035, "power_factor", "U16", 0.001),
    ModBusRegister(5036, "grid_frequency", "U16", 0.1, HERTZ),
    ModBusRegister(5038, "work_state_1", "U16", table=DEVICE_WORK_STATE_1_CODES),
    ModBusRegister(5049, "nominal_reactive_power", "U16", 0.1, "kVar"),
    ModBusRegister(5071, "array_insulation_resistance", "U16", unit_of_measure="kΩ"),
    ModBusRegister(5038, "work_state_2", "U32", transform="BINARY", length=19, table=DEVICE_WORK_STATE_2_CODES, description='Tanslates into work states (refer appendix 2 of sungrow refernce)'),
    ModBusRegister(5083, "meter_power", "S32", unit_of_measure=WATT, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5085, "meter_a_phase_power", "S32", unit_of_measure=WATT, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5087, "meter_b_phase_power", "S32", unit_of_measure=WATT, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5089, "meter_c_phase_power", "S32", unit_of_measure=WATT, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5091, "load_power", "S32", unit_of_measure=WATT, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5093, "daily_export_energy", "U32", 0.1, KILO_WATT_HOUR, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5095, "total_export_energy", "U32", 0.1, KILO_WATT_HOUR, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5097, "daily_import_energy", "U32", 0.1, KILO_WATT_HOUR, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5099, "total_import_energy", "U32", 0.1, KILO_WATT_HOUR, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5101, "daily_direct_energy_consumption", "U32", 0.1, KILO_WATT_HOUR, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5103, "total_direct_energy_consumption", "U32", 0.1, KILO_WATT_HOUR, valid_inverters=[0x013C,0x013E,0x013F,0x0142,0x0143,0x0147,0x0148,0x0149,0x2C0F]),
    ModBusRegister(5113, "daily_running_time", "U16", MINUTE),
    ModBusRegister(5114, "present_country", "U16", table=COUNTRY_CODES),
    ModBusRegister(5115, "mppt_4_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5116, "mppt_4_current", "U16", 0.1, AMPERE),
    ModBusRegister(5117, "mppt_5_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5118, "mppt_5_current", "U16", 0.1, AMPERE),
    ModBusRegister(5119, "mppt_6_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5120, "mppt_6_current", "U16", 0.1, AMPERE),
    ModBusRegister(5121, "mppt_7_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5122, "mppt_7_current", "U16", 0.1, AMPERE),
    ModBusRegister(5123, "mppt_8_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5124, "mppt_8_current", "U16", 0.1, AMPERE),

    ModBusRegister(5128, "monthly_power_yields", "U32", 0.1, KILO_WATT_HOUR),

    ModBusRegister(5130, "mppt_9_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5131, "mppt_9_current", "U16", 0.1, AMPERE),
    ModBusRegister(5132, "mppt_10_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5133, "mppt_10_current", "U16", 0.1, AMPERE),
    ModBusRegister(5134, "mppt_11_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5135, "mppt_11_current", "U16", 0.1, AMPERE),
    ModBusRegister(5136, "mppt_12_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(5137, "mppt_12_current", "U16", 0.1, AMPERE),

    ModBusRegister(5144, "total_power_yields", "U32", 0.1, KILO_WATT_HOUR,
        valid_inverters=[0x139,0x13B,0x13C,0x13E,0x13F,0x142,0x143,0x147,0x148,0x149,
                         0x14C,0x2430,0x2431,0x2432,0x2433,0x2434,0x2435,0x2436,0x2437,0x2437,
                         0x243C,0x243D,0x243E,0x2C00,0x2C01,0x2C02,0x2C03,0x2C06,0x2C0A,0x2C0B,
                         0x2C0C,0x2C0F,0x2C10,0x2C11,0x2C12,0x2C13,0x2C15,0x2C22]),

    ModBusRegister(5148, "grid_frequency_hr", "U16", 0.1, HERTZ,
        valid_inverters=[0x139,0x13B,0x13C,0x13E,0x13F,0x142,0x143,0x147,0x148,0x149,
                         0x14C,0x2430,0x2431,0x2432,0x2433,0x2434,0x2435,0x2436,0x2437,0x2437,
                         0x243C,0x243D,0x243E,0x2C00,0x2C01,0x2C02,0x2C03,0x2C06,0x2C0A,0x2C0B,
                         0x2C0C,0x2C0F,0x2C10,0x2C11,0x2C12,0x2C13,0x2C15,0x2C22]),
)

STRING_HOLDING_REGISTERS: tuple[ModBusRegister, ...] = (
    ModBusRegister(5000, "year", "U16"),
    ModBusRegister(5001, "month", "U16"),
    ModBusRegister(5002, "day", "U16"),
    ModBusRegister(5003, "hour", "U16"),
    ModBusRegister(5004, "minute", "U16"),
    ModBusRegister(5005, "second", "U16"),
)