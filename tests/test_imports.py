"""Test that the package can be imported correctly."""

import pytest


def test_import_eilik():
    """Test that the main package can be imported."""
    import eilik
    assert eilik.__version__ is not None


def test_import_robot():
    """Test that EilikRobot can be imported."""
    from eilik.robot import EilikRobot
    assert EilikRobot is not None


def test_import_ble_client():
    """Test that BLEClient can be imported."""
    from eilik.ble.client import BLEClient
    assert BLEClient is not None


def test_robot_initialization():
    """Test that EilikRobot can be instantiated."""
    from eilik.robot import EilikRobot
    robot = EilikRobot()
    assert robot is not None
    assert not robot.is_connected
