"""
Configuration:

To use the hello_world component you will need to add the following to your
configuration.yaml file.

ticktick:
"""
from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from .constants import DOMAIN


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Setup of the TickTick integration."""
    return True