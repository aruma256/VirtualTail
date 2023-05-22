from .osc_value_provider import OSCValueProvider


class TailTracker:
    def __init__(self, osc_value_provider: OSCValueProvider) -> None:
        self._osc_value_provider = osc_value_provider
        self._initialized = False
        self._position = 0.
        self._left_touched = False
        self._prev_left_proximity = 0.
        self._right_touched = False
        self._prev_right_proximity = 0.
        self._is_grabbed = False

    def initialized(self) -> bool:
        return self._initialized

    def update(self) -> None:
        left, right = self._osc_value_provider.get_latest_values()
        if left is not None and right is not None:
            self._initialized = True
            self._position = left - right
            self._left_touched = (self._osc_value_provider.left_proximity > 0.7)
            self._right_touched = (self._osc_value_provider.right_proximity > 0.7)
            self._is_grabbed = self._osc_value_provider.grabbed

    def get_position(self) -> float:
        assert self.initialized()
        return self._position
