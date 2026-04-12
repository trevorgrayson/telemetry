# Bluetooth StatsD Bridge PRD 

## Overview
We are building a Python-based Bluetooth bridge that allows local clients to send StatsD-formatted messages to a Bluetooth-connected device. The device will act like a StatsD sink, receiving gauge-type metrics over Bluetooth.

## Functional Requirements
1. **Bluetooth Device Discovery**
   - Scan for available BLE devices.
   - Present available devices (or match by name/ID).

2. **Device Connection**
   - Connect to a chosen BLE device.
   - Store the device address (in a TOML config file) for future reconnections.

3. **StatsD Message Parsing**
   - Accept StatsD gauge format messages (e.g., `metric:value|g`).
   - Focus on gauge-type messages only (e.g., `temperature:42|g`).

4. **Local TCP Server**
   - Set up a local server listening on a specified port.
   - Accept incoming StatsD gauge messages via TCP.
   - Relay parsed gauge messages to the connected Bluetooth device.

5. **Bluetooth Data Relay**
   - Once connected, send StatsD gauge messages over the BLE connection.
   - Handle any device-specific characteristics if needed.

## Non-Functional Requirements
- The system should be lightweight, using core Python libraries plus minimal dependencies (`bleak` for BLE, `tomlkit` for config).
- Messages should be handled in near real-time, with minimal latency.
- The system should reconnect to the last known Bluetooth device automatically.

## Configuration
- Store paired device information in a TOML file.
- Configuration includes:
  - Bluetooth device address
  - Local server port number

## Example StatsD Gauge Message

```
temperature:23.5|g
```

## Future Extensions (Out of Scope)
- Support for additional StatsD metric types (counters, timers, etc.).
- Bi-directional communication with the device.
- Authentication or encryption of messages.

