# SungrowInverter

Provides a way to query Sungrow residential hybrid or string inverters for current state and statistics using ModBus TCP client.

## Usage

```python
from sungrowinverter inport SungrowInverter

client = SungrowInverter("192.168.1.27")
await client.async_update()

#Get a list data returned from the inverter.
print(client.data)
```

## Methods and Variables

### Methods

### Variables

## Note
