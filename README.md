# SungrowInverter

Provides a way to query Sungrow residential hybrid or string inverters for current state and statistics using ModBus TCP client.

Currently does not support any writing to holding registers (for now).

## Supported Residental Inverters

### Hybrid/Storage Inverters - inverter that support a battery

Residential Hybrid Single Phase Inverter for Low Voltage Battery [48V to 70V]

SH3K6 / SH4K6 / SH5K-V13 (SH5K) / SH5K-20 / SH4K6-30 / SH5K-30 / SH3K6-30

Residential Hybrid Single Phase Inverter wide battery voltage range [80V to 460V]

SH3.6RS / SH4.6RS / SH5.0RS / SH6.0RS

Residential Hybrid Three Phase Inverter wide battery voltage range [80V to 460V]

SH5.0RT / SH6.0RT / SH8.0RT / SH10RT

### String Inverters - Solar panel and grid connection only

SG3.0RT, SG4.0RT, SG5.0RT, SG6.0RT, SG7.0RT，SG8.0RT, SG10RT, SG12RT, SG15RT, SG17RT, SG20RT
SG30KTL-M, SG30KTL-M-V31, SG33KTL-M, SG36KTL-M, SG33K3J, SG49K5J, SG34KJ, LP_P34KSG,
SG50KTL-M-20, SG60KTL, G80KTL, SG80KTL-20, SG60KU-M
SG5KTL-MT, SG6KTL-MT, SG8KTL-M, SG10KTL-M, SG10KTL-MT, SG12KTL-M, SG15KTL-M,
SG17KTL-M, SG20KTL-M,
SG80KTL-M, SG85BF, SG80HV, SG80BF, SG110HV-M, SG111HV, SG125HV, SG125HV-20
SG25CX-SA, SG30CX, SG33CX, SG40CX, SG50CX, SG36CX-US, SG60CX-US, SG75CX, SG100CX
SG100CX-JP, SG110CX, SG136TX, SG225HX, SG250HX
SG250HX-IN, SG250HX-US

Discontinued (as @ 2021-07-12):

SG30KTL, SG10KTL, SG12KTL, SG15KTL, SG20KTL, SG30KU, SG36KTL, SG36KU, SG40KTL,
SG40KTL-M, SG50KTL-M, SG60KTL-M, SG60KU


## Usage

If not called from within an async method

```python
from sungrowinverter inport SungrowInverter
import asyncio
...

client = SungrowInverter("192.168.1.27")

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
result = loop.run_until_complete(client.async_update())

#Get a list data returned from the inverter.
print(client.data)
```

If called within an async method in your application
```
from sungrowinverter inport SungrowInverter

client = SungrowInverter("192.168.1.27")
client.async_update()

#Get a list data returned from the inverter.
print(client.model)
print(client.data)
```

## Methods and Variables

### Contructor

`SungrowInverter(ip_address, port=502, slave=0x01, retries3, timeout=60)`

port: modbus TCP port defaults to 502 on sungrow inverters used here

slave: defaulted to 0x01 as per specs your inverter may need to change this.

retries: number of attempts to query the registers on the inverter before failing

timeout: <in seconds> tcp connection is timed out and fails after this long

### Methods

Available methods and how to use

`client.inverter_model()` Returns a object of sungrowinverter.common.SungrowInverterModel with details of model, serial, nominal output power (kWh)

`client.async_update()` Calls set of registers for the relevant inverter and updates data parameter
  
### Parameters Available

#### All inverters
  
  `model:` provides device model (ie. SH5K - as found in current models supported above)

  `device_code:` Sungrow device code found at register 5000 (refer docs for actual codes if needed)

  `serial_number:` Serial number of the inverter

  `nominal_output_power:` The output power that the inverter supports (ie. SH5K is a 5 kWh inverter and will contain 5.0 in this parameter)

  `inverter_type:` [hybrid | string] - type of sungrow inverter that the client is communicating with, hybrid (battery supported inverter SHxxx series or standard inverter SGxxxx series)

  `mppt_input:` The number of mppt inputs the inverter supports, refer notes below.

  `data:` provides a dictionary of data of all registers queried (key = register name, value = register value) refer to the https://github.com/mvandersteen/SungrowInverter/tree/main/sungrowinverter/configs for details on what registers are exposed.

#### Hybrid (storage) inverters only
  
  `battery_type:` , this will show the configured details for the inverter

  `battery_capacity :` hybrid inverters only, this will show the configured details for the inverter
  
  
## Note

client = SungrowInverter("192.168.1.27")
await client.async_update()
  
  `client.data['export_power']` - for this register it is a signed value if positive then the inverter is exporting to the grid, if negative then it is importing from the grid.

  `client.mppt_inputs` - this value dictates how many client.data['mppt_xx_voltage'] & client.data['mppt_xx_current'] register are available. These values have been obtained from the modbus specs found in the documents directory on this repository. If an inverter only supports 1 mppt connection then only 1 set of mppt_1_voltage and mppt_1_current will appear. If the inverter supports more then mppt_<nth>_voltage & mppt_<nth>_current; where nth = the number of mppt inputs the inverter supports; the number available depends on the how many the inverter supports can be 1 to 12 sets of data for current set of support inverters. 
  
