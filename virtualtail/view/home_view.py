from threading import Thread
import time

import flet as ft

from ..jcon import Jcon
from ..rumble_controller import RumbleController
from ..tail_tracker import TailTracker
from ..osc_value_provider import OSCValueProvider


class HomeView(ft.View):
    def __init__(self, page: ft.Page):
        self._app_bar = ft.AppBar(
            title=ft.Text("Test app"),
            bgcolor=ft.colors.SURFACE_VARIANT,
        )
        self._position_text = ft.Text()
        self._connect_controllers_button = ft.ElevatedButton(
            "Connect Controllers",
            on_click=self._connect_controllers_button_clicked,
        )
        self._start_osc_server_button = ft.ElevatedButton(
            "Start OSC-Server",
            on_click=self._start_osc_server_button_clicked,
        )
        self._oss_button = ft.ElevatedButton(
            "OSS License",
            on_click=lambda _: page.go("/osslicense"),
        )
        super().__init__(
            route="/",
            controls=[
                self._app_bar,
                self._connect_controllers_button,
                self._start_osc_server_button,
                self._position_text,
                self._oss_button,
            ],
        )

    def _connect_controllers_button_clicked(self, _):
        jconL = Jcon("L")
        jconL.connect()
        jconR = Jcon("R")
        jconR.connect()
        self._rumble_controller = RumbleController(jconL, jconR)
        self._jcons = (jconL, jconR)

    def _start_osc_server_button_clicked(self, _):
        self._start_osc_server_button.disabled = True
        value_provider = OSCValueProvider()
        value_provider.start()
        self._tail_tracker = TailTracker(value_provider)
        Thread(target=self._update, daemon=True).start()

    def _update(self):
        while True:
            self._tail_tracker.update()
            current_position = self._tail_tracker._position
            self._position_text.value = str(current_position)
            self._rumble_controller.update(current_position)
            self.page.update()
            time.sleep(0.06)
