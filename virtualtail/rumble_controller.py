from .jcon import Jcon


class RumbleController:
    def __init__(self) -> None:
        self._jcon_L = None
        self._jcon_R = None

    def start(self) -> None:
        self._jcon_L = Jcon("L")
        self._jcon_L.connect()
        self._jcon_R = Jcon("R")
        self._jcon_R.connect()

    def update(self, pos: float, left_touched: bool, right_touched: bool, grabbed: bool) -> None:
        assert self._jcon_L and self._jcon_R
        import random
        if grabbed:
            left_level = random.choice((10, 11))
            right_level = random.choice((10, 11))
        else:
            left_level = 0
            right_level = 0
            if left_touched:
                left_level += random.choice((3, 4))
            if right_touched:
                right_level += random.choice((3, 4))
            if pos > 0:
                left_level += round(pos * 3.3 * 10)
            elif pos < 0:
                pos = abs(pos)
                right_level += round(pos * 3.3 * 10)
#        print(left_level, right_level)
        self._jcon_L.send_rumble(min(left_level, 11))
        self._jcon_R.send_rumble(min(right_level, 11))
