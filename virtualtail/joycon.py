import hid


VENDOR_ID = 1406
PRODUCT_ID_L = 8198
PRODUCT_ID_R = 8199


class Joycon:
    def __init__(self) -> None:
        self._device = None
        self._packet_id = 0

    def connect(self) -> None:
        self._device = hid.device()
        self._device.open(VENDOR_ID, PRODUCT_ID_L)

    def send_rumble(self, rumble_level: int) -> None:
        assert self._device is not None
        packet = self._get_rumble_packet(rumble_level)
        self._device.write(packet)

    def _get_rumble_packet(self, rumble_level: int) -> list[int]:
        assert 0 <= rumble_level <= 12
        rumble_code = (12 - rumble_level) << 2
        rumble_data = [1, 0, rumble_code, 0] * 2
        packet = [0x10, self._get_packet_id()] + rumble_data
        return packet

    def _get_packet_id(self) -> int:
        current_id = self._packet_id
        self._packet_id = (current_id + 1) % 0x10
        return current_id
