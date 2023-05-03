import math

from .jcon import Jcon


class RumbleController:
    def __init__(self, jconL: Jcon, jconR: Jcon) -> None:
        self._jcon_L = jconL
        self._jcon_R = jconR
        self._max_pos_left = 0
        self._max_pos_right = 0

    def update(self, pos: float) -> None:
        if pos > 0:
            self._max_pos_left = max(self._max_pos_left, pos)
            rumble_level = math.floor(pos / self._max_pos_left * 12)
            self._jcon_L.send_rumble(min(rumble_level, 11))
            self._jcon_R.send_rumble(0)
        elif pos < 0:
            pos = abs(pos)
            self._max_pos_right = max(self._max_pos_right, pos)
            rumble_level = math.floor(pos / self._max_pos_right * 12)
            self._jcon_L.send_rumble(0)
            self._jcon_R.send_rumble(min(rumble_level, 11))
        else:
            self._jcon_L.send_rumble(0)
            self._jcon_R.send_rumble(0)
