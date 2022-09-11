"""Constants for Proxmox integration."""
from __future__ import annotations

import logging
from homeassistant.backports.enum import StrEnum


DOMAIN = "proxmoxve"
INTEGRATION_NAME = "Proxmox VE"

LOGGER = logging.getLogger(__package__)

CONF_CONTAINERS = "containers"
CONF_LXC = "lxc"
CONF_NODE = "node"
CONF_NODES = "nodes"
CONF_QEMU = "qemu"
CONF_REALM = "realm"
CONF_VMS = "vms"

DEFAULT_PORT = 8006
DEFAULT_REALM = "pve"
DEFAULT_VERIFY_SSL = False

ID = "vmid"
COORDINATORS = "coordinators"
PROXMOX_CLIENT = "proxmox_client"


class ProxmoxType(StrEnum):
    """Proxmox type of information."""

    Proxmox = "proxmox"
    Node = "node"
    QEMU = "qemu"
    LXC = "lxc"


COMMAND_REBOOT = "reboot"
COMMAND_RESUME = "resume"
COMMAND_SHUTDOWN = "shutdown"
COMMAND_START = "start"
COMMAND_STOP = "stop"
COMMAND_SUSPEND = "suspend"  # API notes 'This is experimental.'  https://pve.proxmox.com/pve-docs/api-viewer/#/nodes/{node}/lxc/{vmid}/status/suspend
COMMAND_RESET = "reset"

VM_COMMANDS = (
    COMMAND_REBOOT,
    COMMAND_RESUME,
    COMMAND_SHUTDOWN,
    COMMAND_START,
    COMMAND_STOP,
    COMMAND_SUSPEND,
    COMMAND_RESET,
)
