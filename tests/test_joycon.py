# Written with ChatGPT

from unittest.mock import Mock, patch

import pytest

from virtualtail.joycon import Joycon


VENDOR_ID = 1406
PRODUCT_ID_L = 8198


class TestJoycon:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.joycon = Joycon()
        self.joycon._device = Mock()

    @patch('hid.device')
    def test_connect(self, mock_hid_device):
        mock_hid_device.return_value = self.joycon._device
        self.joycon.connect()
        mock_hid_device.assert_called_once()
        self.joycon._device.open.assert_called_once_with(1406, 8198)

    @pytest.mark.parametrize('rumble_level, expected_packet', [
        (0, [0x10, 0, 1, 0, 48, 0, 1, 0, 48, 0]),  # max rumble level
        (6, [0x10, 0, 1, 0, 24, 0, 1, 0, 24, 0]),  # half rumble level
        (12, [0x10, 0, 1, 0, 0, 0, 1, 0, 0, 0]),  # min rumble level
    ])
    def test_send_rumble(self, rumble_level, expected_packet):
        self.joycon.send_rumble(rumble_level)
        self.joycon._device.write.assert_called_once_with(expected_packet)

    def test_get_packet_id(self):
        assert self.joycon._get_packet_id() == 0
        assert self.joycon._get_packet_id() == 1
        self.joycon._packet_id = 15
        assert self.joycon._get_packet_id() == 15
        assert self.joycon._get_packet_id() == 0
