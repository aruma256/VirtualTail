from threading import Thread
import time

import flet as ft

from ..tail_tracker import TailTracker
from ..osc_value_provider import OSCValueProvider


class HomeView(ft.View):
    def __init__(self, page: ft.Page):
        self._position_text = ft.Text("aaa")
        super().__init__(
            route="/",
            controls=[
                ft.AppBar(
                    title=ft.Text("Test app"),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                ),
                ft.ElevatedButton(
                    "Start",
                    on_click=self._start_button_clicked,
                ),
                self._position_text,
                ft.ElevatedButton(
                    "OSS License",
                    on_click=lambda _: page.go("/osslicense"),
                ),
            ],
        )

    def _start_button_clicked(self, *args):
        print(*args)
        value_provider = OSCValueProvider()
        value_provider.start()
        self._tail_tracker = TailTracker(value_provider)
        Thread(target=self._update, daemon=True).start()

    def _update(self):
        while True:
            self._tail_tracker.update()
            self._position_text.value = str(self._tail_tracker._position)
            self.page.update()
            time.sleep(0.1)
