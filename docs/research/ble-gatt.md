# BLE GATT Research Notes

This document tracks discovered GATT services and characteristics for Eilik robots.

> **Note:** This is a research document. Information here is based on observation and reverse engineering. EnergizeLab does not provide official BLE protocol documentation.

## How to Contribute

When you discover new services or characteristics:

1. Connect to your Eilik using `examples/introspect.py`
2. Document the UUIDs, properties, and any observed behavior
3. Submit a PR with your findings

## Device Information

| Field | Value | Notes |
|-------|-------|-------|
| Device Name | `Eilik` (or variant) | May vary by model |
| Connection Type | Bluetooth Low Energy (BLE) | |
| Pairing | | |

## GATT Services

| Service UUID | Name/Description | Characteristics | Notes |
|--------------|------------------|-----------------|-------|
| | | | *To be discovered* |

## GATT Characteristics

| Characteristic UUID | Service UUID | Properties | Description | Notes |
|---------------------|--------------|------------|-------------|-------|
| | | | | *To be discovered* |

## Protocol Observations

### Connection Behavior
- *Document observed connection patterns here*

### Command Patterns
- *Document any observed command patterns here*

### Response Patterns
- *Document any observed response patterns here*

## Research Log

| Date | Researcher | Findings |
|------|------------|----------|
| | | *Add entries as discoveries are made* |

## Tools Used

- `examples/introspect.py` - GATT service/characteristic discovery
- `bleak` - Python BLE library
- *Add other tools as used*

## References

- [EnergizeLab Support](https://energizelab.com/supportview/eilik003)
- [BLE GATT Specification](https://www.bluetooth.com/specifications/specs/core-specification/)
