"""Constants."""
from __future__ import annotations

from typing import Final

_DEFAULT_SYSVAR_REGISTRY_ENABLED: bool = False
DEFAULT_SYSVAR_SCAN_INTERVAL: Final = 30
DEVICE_FIRMWARE_CHECK_ENABLED: Final = True
DEVICE_FIRMWARE_CHECK_INTERVAL: Final = 21600  # 6h
DEVICE_FIRMWARE_DELIVERING_CHECK_INTERVAL: Final = 3600  # 1h
DEVICE_FIRMWARE_UPDATING_CHECK_INTERVAL: Final = 300  # 5m
MASTER_SCAN_INTERVAL: Final = 3600  # 1h


def get_default_sysvar_registry_enabled() -> bool:
    """Return the _DEFAULT_SYSVAR_REGISTRY_ENABLED const."""
    return _DEFAULT_SYSVAR_REGISTRY_ENABLED
