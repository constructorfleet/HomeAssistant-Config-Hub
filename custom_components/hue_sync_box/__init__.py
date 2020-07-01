"""Philips Hue Sync Box integration."""

import ipaddress

import homeassistant.helpers.config_validation as cv
import voluptuous as vol

from .const import *
from . import services

DEFAULT_NAME = 'Hue Sync'


def coerce_ip(value):
    """Validate that provided value is a valid IP address."""
    if not value:
        raise vol.Invalid("Must define an IP address")
    try:
        ipaddress.IPv4Network(value)
    except ValueError:
        raise vol.Invalid("Not a valid IP address")
    return value


PLATFORM_SCHEMA = cv.PLATFORM_SCHEMA.extend({
    voluptuous.Required(CONF_IP_ADDRESS): vol.All(
            cv.string,
            coerce_ip),
    voluptuous.Required(CONF_ACCESS_TOKEN): cv.string,
    voluptuous.Optional(CONF_NAME, DEFAULT_NAME): cv.string,
})


async def async_setup(hass, config):
  hass.data[DOMAIN] = {}
  return True
