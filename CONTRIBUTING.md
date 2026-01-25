# Contributing to Eilik Robot Interface

Thank you for your interest in contributing! This project is in early stages and focuses on research and discovery of the Eilik BLE protocol.

## How to Contribute

### Reporting Issues

Before opening an issue, please:
- Check if the issue already exists
- For questions or discussions, use [GitHub Discussions](https://github.com/ailynux/eilik-robot/discussions) instead of issues
- Be respectful and understand this is a research project

### Contributing Code

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/your-feature-name`)
3. **Make your changes**
   - Follow Python style guidelines (PEP 8)
   - Add tests if applicable
   - Update documentation as needed
4. **Commit your changes** (`git commit -m 'Add some feature'`)
5. **Push to the branch** (`git push origin feature/your-feature-name`)
6. **Open a Pull Request**

### Research Contributions

We especially welcome contributions that help document the Eilik BLE protocol:
- GATT service/characteristic UUIDs
- Observed behavior patterns
- Protocol reverse engineering notes
- Connection troubleshooting tips

Please document findings in `docs/research/ble-gatt.md`.

### Code Style

- Use Python 3.8+ features
- Follow PEP 8 style guide
- Use type hints where helpful
- Write clear docstrings
- Keep functions focused and testable

### Testing

- Write tests for new functionality
- Run tests before submitting: `pytest tests/`
- Ensure all tests pass

### Documentation

- Update README.md if adding major features
- Document new functions with docstrings
- Update research notes when discovering protocol details

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/eilik-robot.git
cd eilik-robot

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest tests/
```

## Questions?

Feel free to open a discussion or reach out if you have questions about contributing!
