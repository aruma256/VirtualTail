import flet as ft


class HomeView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(
            route="/",
            controls=[
                ft.AppBar(
                    title=ft.Text("Test app"),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                ),
                ft.ElevatedButton(
                    "OSS License",
                    on_click=lambda _: page.go("/osslicense"),
                ),
            ],
        )
