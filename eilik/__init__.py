"""
Eilik Robot Interface

A research and development toolkit for interacting with Eilik robots via Bluetooth LE.

Note: This project is in early development. EnergizeLab does not provide a public
open-source API for Eilik, so this project focuses on BLE discovery and protocol
research.
"""

__version__ = "0.1.0"

from eilik.robot import EilikRobot

__all__ = ["EilikRobot"]
