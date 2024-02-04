from bleak import BleakClient

@service
def get_oclean_battery(mac=None, entity_id=None):
    """get_oclean_battery example using pyscript."""
    # log.info(f"get_oclean_battery: got mac {mac}")
    bleakClient = BleakClient(mac)

    try:
        if not bleakClient.connect():
            log.error(f"Failed to connect to {mac}")
            return

        battery_level = bleakClient.read_gatt_char('00002a19-0000-1000-8000-00805f9b34fb')
        # log.info(f"Battery Level: {battery_level[0]}%")
        input_number.set_value(entity_id=entity_id, value=battery_level[0])

    finally:
        bleakClient.disconnect()
