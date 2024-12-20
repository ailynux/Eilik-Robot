# 🤖 Eilik Robot Interface 
### - heavy planning to do but want to customize this robot

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Bluetooth](https://img.shields.io/badge/bluetooth-LE-blue.svg)](https://www.bluetooth.com/)

Welcome to the Eilik Robot Interface project! This repository provides tools and libraries to interact with and customize your Eilik companion robot, turning it into an even more versatile and personalized robotic friend.
![image](https://github.com/user-attachments/assets/eb88bdb6-f42c-4464-94f9-8b17f3b38bec)

## ✨ Features

- 🎮 Complete Bluetooth LE control interface
- 🎵 Custom animation and sound sequence creation
- 📱 Real-time interaction capabilities
- 🔄 Extensible behavior programming
- 📊 Sensor data monitoring and logging
- 🎨 LED pattern customization
- 🤝 Multi-robot interaction support

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Bluetooth LE capable hardware
- An Eilik robot (firmware version X.X or higher)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ailynux/eilik-robot.git
cd eilik-robot
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your robot:
```bash
python setup.py configure
```

## 📖 Usage

### Basic Connection

```python
from eilik.robot import EilikRobot

async def main():
    robot = EilikRobot()
    await robot.connect()
    
    # Make your Eilik wave
    await robot.perform_action("wave")
    
    await robot.disconnect()
```

### Custom Behavior Programming

```python
# Create a custom dance sequence
@robot.behavior
async def happy_dance():
    await robot.move("spin")
    await robot.led_pattern("rainbow")
    await robot.play_sound("happy")
```

## 🎯 Example Projects

1. **Mood Light Assistant**
   - Use Eilik as an ambient light that responds to room conditions
   - Customize LED patterns based on time of day

2. **Desktop Companion**
   - Integration with your computer's status
   - Meeting notifications
   - Break time reminders

3. **Interactive Teaching Aid**
   - Educational animations
   - Quiz response indicators
   - Student engagement tracking

## 🛠 Advanced Configuration

### Bluetooth Settings

```yaml
bluetooth:
  scan_timeout: 10
  retry_attempts: 3
  connection_interval: 50
```

### Animation Sequences

```yaml
animations:
  happy_dance:
    - move: spin
    - led: rainbow
    - sound: chirp
    duration: 5000
```

## 📚 API Documentation

Detailed documentation for all available functions and customization options:

- [Connection Management](docs/connection.md)
- [Movement Controls](docs/movement.md)
- [LED Patterns](docs/led-patterns.md)
- [Sound Control](docs/sound.md)
- [Sensor Data](docs/sensors.md)
- [Custom Behaviors](docs/behaviors.md)

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Check code style
flake8 eilik/
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- The Eilik robot creator community
- Contributors to the Bluetooth LE Python libraries


## 🗺 Roadmap

- [ ] Web-based control interface
- [ ] Mobile app integration
- [ ] Group choreography support
- [ ] Machine learning behavior models
- [ ] Voice command integration
- [ ] Environmental awareness features

---

<p align="center">Made with ❤️ for the Eilik community</p>
