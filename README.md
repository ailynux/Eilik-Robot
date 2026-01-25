# 🤖 Eilik Robot Interface

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Bluetooth](https://img.shields.io/badge/bluetooth-LE-blue.svg)](https://www.bluetooth.com/)

Welcome to the Eilik Robot Interface project! This repository provides tools and libraries to interact with and customize your Eilik companion robot, turning it into an even more versatile and personalized robotic friend.

![image](https://github.com/user-attachments/assets/eb88bdb6-f42c-4464-94f9-8b17f3b38bec)

## 🚧 Project Status

This project is currently **early-stage / research + scaffolding**.

EnergizeLab does not provide a public open-source API for Eilik at this time, so this repo focuses on:
- BLE discovery / connection scaffolding
- documenting observed GATT services/characteristics
- building a clean foundation for future community-driven tooling

✅ **What works today:**
- Repo structure + tooling (in progress)
- BLE scan + device introspection (planned for v0.1)

⚠️ **What does NOT exist yet:**
- Reliable "wave/dance/sound" actions
- A stable protocol implementation
- Complete control interface

> **Disclaimer:** This project is not affiliated with EnergizeLab. Use at your own risk. Please be patient for features that require reverse engineering.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Bluetooth LE capable hardware
- An Eilik robot

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ailynux/eilik-robot.git
cd eilik-robot
```

2. Install required dependencies:
```bash
pip install -e .
```

Or install with development dependencies:
```bash
pip install -e ".[dev]"
```

## 📖 Usage

### Basic BLE Scanning

```python
from eilik.robot import EilikRobot

async def main():
    robot = EilikRobot()
    
    # Scan for Eilik devices
    devices = await robot.scan(timeout=10.0)
    print(f"Found {len(devices)} devices")
    
    for device in devices:
        print(f"  - {device.name} ({device.address})")
```

### Device Introspection

```python
async def main():
    robot = EilikRobot()
    
    # Connect to a device
    await robot.connect("XX:XX:XX:XX:XX:XX")  # Replace with your device address
    
    # List GATT services and characteristics
    services = await robot.list_gatt()
    for service in services:
        print(f"Service: {service.uuid}")
        for char in service.characteristics:
            print(f"  Characteristic: {char.uuid}")
    
    await robot.disconnect()
```

See the `examples/` directory for more complete examples.

## Current Goals (v0.1)

- [x] Project structure and tooling
- [ ] BLE device scanning
- [ ] Device connection and disconnection
- [ ] GATT service/characteristic introspection
- [ ] Research notes documentation

## 📚 Documentation

- [Research Notes](docs/research/ble-gatt.md) - Documented GATT services and characteristics
- [Connection Guide](docs/connection.md) - How to connect to your Eilik (coming soon)

## 🤝 Contributing

I welcome contributions! Please read the [Contributing Guide](CONTRIBUTING.md) first.

### Development Setup

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/

# Check code style (if configured)
flake8 eilik/
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- The Eilik robot creator community
- Contributors to the Bluetooth LE Python libraries (especially `bleak`)

## 🗺 Roadmap

- [ ] v0.1: BLE scanning and introspection
- [ ] v0.2: Protocol discovery and documentation
- [ ] v0.3: Basic command interface (if protocol is understood)
- [ ] Future: Custom behaviors, animations, and integrations

---

<p align="center">Made with ❤️ for the Eilik community</p>
