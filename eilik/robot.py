"""
EilikRobot - High-level interface for Eilik robot interaction.

This class provides a user-friendly API for discovering, connecting to,
and introspecting Eilik robots via Bluetooth LE.
"""

import logging
from typing import List, Optional

from bleak.backends.device import BLEDevice
from bleak.backends.service import BleakGATTService

from eilik.ble.client import BLEClient

logger = logging.getLogger(__name__)


class EilikRobot:
    """
    High-level interface for Eilik robot interaction.
    
    This class provides methods for:
    - Scanning for Eilik devices
    - Connecting and disconnecting
    - Introspecting GATT services and characteristics
    """

    def __init__(self, name_filter: Optional[str] = "Eilik"):
        """
        Initialize the EilikRobot interface.
        
        Args:
            name_filter: Device name filter for scanning (default: "Eilik")
        """
        self._ble_client = BLEClient()
        self._name_filter = name_filter

    async def scan(self, timeout: float = 10.0) -> List[BLEDevice]:
        """
        Scan for Eilik robots.
        
        Args:
            timeout: Scan duration in seconds
            
        Returns:
            List of discovered Eilik devices
        """
        return await self._ble_client.scan(
            timeout=timeout,
            name_filter=self._name_filter,
        )

    async def connect(self, address: Optional[str] = None) -> bool:
        """
        Connect to an Eilik robot.
        
        Args:
            address: Device address (MAC). If None, will attempt to
                     connect to the first device found in a scan.
                     
        Returns:
            True if connection successful, False otherwise
        """
        if address is None:
            # Auto-discover and connect to first device
            devices = await self.scan(timeout=5.0)
            if not devices:
                logger.error("No Eilik devices found")
                return False
            address = devices[0].address
            logger.info(f"Auto-connecting to {devices[0].name} ({address})")

        return await self._ble_client.connect(address)

    async def disconnect(self) -> None:
        """Disconnect from the current robot."""
        await self._ble_client.disconnect()

    async def list_gatt(self) -> List[BleakGATTService]:
        """
        List all GATT services and characteristics.
        
        This is useful for protocol discovery and research.
        
        Returns:
            List of GATT services with their characteristics
            
        Raises:
            RuntimeError: If not connected to a device
        """
        if not self._ble_client.is_connected:
            raise RuntimeError("Not connected to a device. Call connect() first.")

        client = self._ble_client.client
        if client is None:
            raise RuntimeError("BLE client not available")

        services = []
        for service in client.services:
            services.append(service)
            logger.info(f"Service: {service.uuid} ({service.description or 'Unknown'})")
            for char in service.characteristics:
                props = ", ".join(char.properties)
                logger.info(
                    f"  Characteristic: {char.uuid} "
                    f"({char.description or 'Unknown'}) "
                    f"[{props}]"
                )

        return services

    @property
    def is_connected(self) -> bool:
        """Check if currently connected to a robot."""
        return self._ble_client.is_connected

    @property
    def address(self) -> Optional[str]:
        """Get the address of the currently connected robot."""
        return self._ble_client.address
