"""Sungrow inverter register definitions for the model, serial and nominal power output."""

from sungrowinverter.configs.common import (
    ModBusRegister,
    SungrowInverterModel,
    KILO_WATT,
    VOLTAGE,
    AMP_HOUR,
    BATTERY_TYPES,
)

INVERTER_SCAN = {
    "read": [{"scan_start": 4989, "scan_range": 12}],
    "holding": [{"scan_start": 13054, "scan_range": 3}],
}

INVERTER_READ_REGISTERS: tuple[ModBusRegister, ...] = (
    ModBusRegister(4990, "serial_number", "UTF8", length=10),
    ModBusRegister(5000, "device_type_code", "U16"),
    ModBusRegister(5001, "nominal_output_power", "U16", 0.1, KILO_WATT),
)

INVERTER_HOLDING_REGISTERS: tuple[ModBusRegister, ...] = (
    ModBusRegister(13055, "battery_type", "U16", table=BATTERY_TYPES),
    ModBusRegister(13056, "battery_nominal_voltage", "U16", 0.1, VOLTAGE),
    ModBusRegister(13057, "battery_capacity", "U16", 1, AMP_HOUR),
)

INVERTER_MODELS: list[SungrowInverterModel] = (
    SungrowInverterModel(0xD03, "SH5K", "hybrid", 2),
    SungrowInverterModel(0xD06, "SH3K6", "hybrid", 2),
    SungrowInverterModel(0xD07, "SH4K6", "hybrid", 2),
    SungrowInverterModel(0xD09, "SH5K-20", "hybrid", 2),
    SungrowInverterModel(0xD0A, "SH3K6-30", "hybrid", 2),
    SungrowInverterModel(0xD0B, "SH4K6-30", "hybrid", 2),
    SungrowInverterModel(0xD0C, "SH5K-30", "hybrid", 2),
    SungrowInverterModel(0xD0D, "SH3.6RS", "hybrid", 2),
    SungrowInverterModel(0xD0E, "SH4.6RS", "hybrid", 2),
    SungrowInverterModel(0xD0F, "SH5.0RS", "hybrid", 2),
    SungrowInverterModel(0xD10, "SH6.0RS", "hybrid", 2),
    SungrowInverterModel(0xE00, "SH5.0RT", "hybrid", 2),
    SungrowInverterModel(0xE01, "SH6.0RT", "hybrid", 2),
    SungrowInverterModel(0xE02, "SH8.0RT", "hybrid", 2),
    SungrowInverterModel(0xE03, "SH10RT", "hybrid", 2),
    SungrowInverterModel(0xE0D, "SH6.0RT-V112", "hybrid", 2),
    SungrowInverterModel(0xE0E, "SH8.0RT-V112", "hybrid", 2),
    SungrowInverterModel(0xE0F, "SH10RT-V112", "hybrid", 2),
    SungrowInverterModel(0x26,'SG10KTL','string',2),
    SungrowInverterModel(0x27,'SG30KTL','string',2),
    SungrowInverterModel(0x28,'SG15KTL','string',2),
    SungrowInverterModel(0x29,'SG12KTL','string',2),
    SungrowInverterModel(0x2A,'SG20KTL','string',2),
    SungrowInverterModel(0x2C,'SG30KU','string',2),
    SungrowInverterModel(0x2D,'SG36KTL','string',2),
    SungrowInverterModel(0x2E,'SG36KU','string',2),
    SungrowInverterModel(0x2F,'SG40KTL','string',2),
    SungrowInverterModel(0x70,'SG30KTL-M-V31','string',3),
    SungrowInverterModel(0x72,'SG34KJ','string',2),
    SungrowInverterModel(0x73,'LP_P34KSG','string',1),
    SungrowInverterModel(0x74,'SG36KTL-M','string',3),
    SungrowInverterModel(0x010F,'SG60KTL','string',1),
    SungrowInverterModel(0x011B,'SG50KTL-M-20','string',4),
    SungrowInverterModel(0x0131,'SG60KTL-M','string',4),
    SungrowInverterModel(0x0132,'SG60KU-M','string',4),
    SungrowInverterModel(0x0134,'SG33KTL-M','string',3),
    SungrowInverterModel(0x0135,'SG40KTL-M','string',3),
    SungrowInverterModel(0x0136,'SG60KU','string',1),
    SungrowInverterModel(0x0137,'SG49K5J','string',4),
    SungrowInverterModel(0x0138,'SG80KTL','string',1),
    SungrowInverterModel(0x0139,'SG80KTL-M','string',4),
    SungrowInverterModel(0x013B,'SG125HV','string',1),
    SungrowInverterModel(0x013C,'SG12KTL-M','string',2),
    SungrowInverterModel(0x013D,'SG33K3J','string',3),
    SungrowInverterModel(0x013E,'SG10KTL-M','string',2),
    SungrowInverterModel(0x013F,'SG8KTL-M','string',2),
    SungrowInverterModel(0x0141,'SG30KTL-M','string',3),
    SungrowInverterModel(0x0142,'SG15KTL-M','string',2),
    SungrowInverterModel(0x0143,'SG20KTL-M','string',2),
    SungrowInverterModel(0x0147,'SG5KTL-MT','string',2),
    SungrowInverterModel(0x0148,'SG6KTL-MT','string',2),
    SungrowInverterModel(0x0149,'SG17KTL-M','string',2),
    SungrowInverterModel(0x014C,'SG111HV','string',1),
    SungrowInverterModel(0x2430,'SG5.0RT','string',2),
    SungrowInverterModel(0x2431,'SG6.0RT','string',2),
    SungrowInverterModel(0x2432,'SG8.0RT','string',2),
    SungrowInverterModel(0x2432,'SG8.0RT','string',2),
    SungrowInverterModel(0x2433,'SG10RT','string',2),
    SungrowInverterModel(0x2434,'SG12RT','string',2),
    SungrowInverterModel(0x2435,'SG15RT','string',2),
    SungrowInverterModel(0x2436,'SG17RT','string',2),
    SungrowInverterModel(0x2437,'SG20RT','string',2),
    SungrowInverterModel(0x243C,'SG7.0RT','string',2),
    SungrowInverterModel(0x243D,'SG3.0RT','string',2),
    SungrowInverterModel(0x243E,'SG4.0RT','string',2),
    SungrowInverterModel(0x2C00,'SG33CX','string',3),
    SungrowInverterModel(0x2C01,'SG40CX','string',4),
    SungrowInverterModel(0x2C02,'SG50CX','string',5),
    SungrowInverterModel(0x2C03,'SG125HV-20','string',1),
    SungrowInverterModel(0x2C06,'SG110CX','string',9),
    SungrowInverterModel(0x2C0A,'SG36CX-US','string',3),
    SungrowInverterModel(0x2C0B,'SG60CX-US','string',5),
    SungrowInverterModel(0x2C0C,'SG250HX','string',12),
    SungrowInverterModel(0x2C0F,'SG10KTL-MT','string',2),
    SungrowInverterModel(0x2C10,'SG30CX','string',3),
    SungrowInverterModel(0x2C11,'SG250HX-US','string',12),
    SungrowInverterModel(0x2C12,'SG100CX','string',12),
    SungrowInverterModel(0x2C13,'SG250HX-IN','string',12),
    SungrowInverterModel(0x2C15,'SG25CX-SA','string',3),
    SungrowInverterModel(0x2C22,'SG75CX','string',9),
    # Maybe a correct inverter setting for unsupported SG5K-D??
    SungrowInverterModel(0x126,'SG5K-D','string',2),
    # Supplied in Issue #7
    SungrowInverterModel(0x2600,'SG2.0RS-S','string',2),
)
