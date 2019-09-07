# Configuration for hubs used by the distributed, modular Home-Assistant state machine

This is the distributed Home-Assistant module for Z-Wave and Zigbee modems. This instance is intended to not need to be restarted unless absolutely new.

## Setting your variables

Create a `secrets.yaml` file with the following properties defined
	* `zstick_path` - the path to the z-stick device
	* `zwave_security_key` - the sequence of hex codes for secure inclusion
	* `zwave_interval` - the duration of the mesh network poll loop
	* `zigbee_path` - the path to the zigbee device

## 