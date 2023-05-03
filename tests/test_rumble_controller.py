# Written with ChatGPT


from unittest.mock import Mock
from virtualtail.jcon import Jcon
from virtualtail.rumble_controller import RumbleController


class TestRumbleController:
    def test_init(self):
        jcon_l = Mock(spec=Jcon)
        jcon_r = Mock(spec=Jcon)
        controller = RumbleController(jcon_l, jcon_r)
        assert controller._jcon_L == jcon_l
        assert controller._jcon_R == jcon_r
        assert controller._max_pos_left == 0
        assert controller._max_pos_right == 0

    def test_update_with_positive_pos(self):
        jcon_l = Mock(spec=Jcon)
        jcon_r = Mock(spec=Jcon)
        controller = RumbleController(jcon_l, jcon_r)

        controller.update(1)
        jcon_l.send_rumble.assert_called_with(11)
        jcon_r.send_rumble.assert_called_with(0)
        assert controller._max_pos_left == 1
        assert controller._max_pos_right == 0

    def test_update_with_negative_pos(self):
        jcon_l = Mock(spec=Jcon)
        jcon_r = Mock(spec=Jcon)
        controller = RumbleController(jcon_l, jcon_r)

        controller.update(-1)
        jcon_l.send_rumble.assert_called_with(0)
        jcon_r.send_rumble.assert_called_with(11)
        assert controller._max_pos_left == 0
        assert controller._max_pos_right == 1

    def test_update_with_zero_pos(self):
        jcon_l = Mock(spec=Jcon)
        jcon_r = Mock(spec=Jcon)
        controller = RumbleController(jcon_l, jcon_r)

        controller.update(0)
        jcon_l.send_rumble.assert_called_with(0)
        jcon_r.send_rumble.assert_called_with(0)
