# SungrowInverter

Provides a way to query Sungrow residential hybrid or string inverters for current state and statistics using ModBus TCP client.

Currently does not support any writing to holding registers (for now).


## Usage

```python
from sungrowinverter inport SungrowInverter

client = SungrowInverter("192.168.1.27")
await client.async_update()

#Get a list data returned from the inverter.
print(client.data)
```

## Methods and Variables

### Contructor

`SungrowInverter(ip_address, port=502, initialize=True, slave=0x01, retries3, timeout=60)`

port: modbus TCP port defaults to 502 on sungrow inverters used here

initialize: <True|False> if set will query inverter during setup of object and determine inverter model, nominal power capability and other statsic inverter related data

slave: defaulted to 0x01 as per specs your inverter may nee to change this.

retries: number of attempts to query the registers on the inverter before failing

timeout: <in seconds> tcp connection is stopped after this long

### Methods

Available methods and how to use

`client.inverter_model()

`client.async_update()

### Variables

client.

## Note
