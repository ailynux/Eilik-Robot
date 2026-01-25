"""
Example: Scan for Eilik robots.

This script demonstrates how to scan for Eilik devices on your network.
"""

import asyncio
import logging

from eilik.robot import EilikRobot

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


async def main():
    """Scan for Eilik robots."""
    print("Scanning for Eilik robots...")
    print("(Make sure your Eilik is powered on and in pairing mode)\n")

    robot = EilikRobot()
    devices = await robot.scan(timeout=10.0)

    if not devices:
        print("No Eilik devices found.")
        print("\nTroubleshooting:")
        print("  - Make sure your Eilik is powered on")
        print("  - Check that Bluetooth is enabled on your computer")
        print("  - Try moving the robot closer to your computer")
        return

    print(f"Found {len(devices)} device(s):\n")
    for i, device in enumerate(devices, 1):
        print(f"{i}. {device.name or 'Unknown'}")
        print(f"   Address: {device.address}")
        print(f"   RSSI: {device.rssi} dBm")
        print()


if __name__ == "__main__":
    asyncio.run(main())
