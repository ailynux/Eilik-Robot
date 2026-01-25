"""
Bluetooth Low Energy client for Eilik robots.

This module provides low-level BLE communication functionality using bleak.
"""

import asyncio
import logging
from typing import List, Optional

from bleak import BleakClient, BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

logger = logging.getLogger(__name__)


class BLEClient:
    """
    Low-level BLE client for scanning and connecting to devices.
    
    This class handles the basic Bluetooth LE operations needed for
    device discovery and connection management.
    """

    def __init__(self):
        """Initialize the BLE client."""
        self._client: Optional[BleakClient] = None
        self._device_address: Optional[str] = None

    async def scan(
        self,
        timeout: float = 10.0,
        name_filter: Optional[str] = None,
    ) -> List[BLEDevice]:
        """
        Scan for Bluetooth LE devices.
        
        Args:
            timeout: Scan duration in seconds
            name_filter: Optional device name filter (case-insensitive)
            
        Returns:
            List of discovered BLEDevice objects
        """
        logger.info(f"Scanning for BLE devices (timeout: {timeout}s)...")
        
        devices = await BleakScanner.discover(timeout=timeout)
        
        if name_filter:
            filtered = [
                device
                for device in devices
                if device.name and name_filter.lower() in device.name.lower()
            ]
            logger.info(f"Found {len(filtered)} devices matching '{name_filter}'")
            return filtered
        
        logger.info(f"Found {len(devices)} devices")
        return devices

    async def connect(self, address: str) -> bool:
        """
        Connect to a BLE device by address.
        
        Args:
            address: Bluetooth device address (MAC address)
            
        Returns:
            True if connection successful, False otherwise
        """
        if self._client and self._client.is_connected:
            logger.warning("Already connected to a device")
            return True

        try:
            logger.info(f"Connecting to {address}...")
            self._client = BleakClient(address)
            await self._client.connect()
            self._device_address = address
            logger.info(f"Connected to {address}")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to {address}: {e}")
            self._client = None
            self._device_address = None
            return False

    async def disconnect(self) -> None:
        """Disconnect from the current device."""
        if self._client and self._client.is_connected:
            logger.info(f"Disconnecting from {self._device_address}...")
            await self._client.disconnect()
            logger.info("Disconnected")
        
        self._client = None
        self._device_address = None

    @property
    def is_connected(self) -> bool:
        """Check if currently connected to a device."""
        return self._client is not None and self._client.is_connected

    @property
    def client(self) -> Optional[BleakClient]:
        """Get the underlying BleakClient instance."""
        return self._client

    @property
    def address(self) -> Optional[str]:
        """Get the address of the currently connected device."""
        return self._device_address
