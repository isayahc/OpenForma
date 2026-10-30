"""Deterministic firmware-scaffold generation from the hardware IR."""

from __future__ import annotations

from forma_core.firmware.drivers import DRIVER_STUBS, DriverStub, lookup_driver
from forma_core.firmware.examples import esp32_example_ir, nano_example_ir
from forma_core.firmware.generate import generate_firmware
from forma_core.firmware.models import FirmwareScaffold, FirmwareTarget
from forma_core.firmware.targets import (
    BOARD_MAPPINGS,
    BoardMapping,
    UnknownBoardError,
    get_board_mapping,
    get_mapping_for_target,
)
from forma_core.firmware.validation import firmware_target_rules

__all__ = [
    "BOARD_MAPPINGS",
    "DRIVER_STUBS",
    "BoardMapping",
    "DriverStub",
    "FirmwareScaffold",
    "FirmwareTarget",
    "UnknownBoardError",
    "esp32_example_ir",
    "firmware_target_rules",
    "generate_firmware",
    "get_board_mapping",
    "get_mapping_for_target",
    "lookup_driver",
    "nano_example_ir",
]
