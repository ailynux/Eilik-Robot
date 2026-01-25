"""
Example: Connect to an Eilik robot and introspect GATT services.

This script demonstrates how to connect to a device and list all
available GATT services and characteristics for protocol research.
"""

import asyncio
import logging
import sys

from eilik.robot import EilikRobot

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


async def main():
    """Connect to an Eilik and list GATT services."""
    robot = EilikRobot()

    # If address provided as command line argument, use it
    address = sys.argv[1] if len(sys.argv) > 1 else None

    if address:
        print(f"Connecting to {address}...")
        success = await robot.connect(address)
    else:
        print("Scanning for Eilik robots...")
        devices = await robot.scan(timeout=5.0)

        if not devices:
            print("No Eilik devices found.")
            print("\nUsage: python introspect.py [DEVICE_ADDRESS]")
            return

        print(f"Found {len(devices)} device(s)")
        print(f"Connecting to {devices[0].name} ({devices[0].address})...")
        success = await robot.connect(devices[0].address)

    if not success:
        print("Failed to connect")
        return

    print("Connected!\n")
    print("=" * 60)
    print("GATT Services and Characteristics:")
    print("=" * 60)
    print()

    try:
        services = await robot.list_gatt()
        print(f"\nFound {len(services)} service(s)")
        print("\nTip: Document discovered UUIDs in docs/research/ble-gatt.md")
    except Exception as e:
        print(f"Error listing GATT services: {e}")
    finally:
        print("\nDisconnecting...")
        await robot.disconnect()
        print("Disconnected")


if __name__ == "__main__":
    asyncio.run(main())
