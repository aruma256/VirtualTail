import flet as ft

from .osc_value_provider import OSCValueProvider
from .view.home_view import HomeView
from .view.osslicense_view import OSSLicenseView


def main(page: ft.Page):
    page.title = "サンプル"

    osc_value_provider = OSCValueProvider()
    osc_value_provider.start()

    def route_change(route):
        page.views.clear()
        page.views.append(HomeView(page))
        if page.route == "/osslicense":
            page.views.append(OSSLicenseView(page))
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


def start():
    ft.app(target=main)
