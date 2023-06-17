import flet as ft
from view.AppPage import AppPage
from view.auth_view import Authview
from view.dashboard import Dashboard
def main(page: ft.Page):

    pages: list[AppPage] = [
        Authview(root=page, route='/'),
        Dashboard(root=page, route='/dashboard')

        # Register your pages here
    ]

    theme = ft.Theme(
        use_material3=True
    )
    page.theme_mode = "DARK"
    page.theme = theme
    page.dark_theme = theme
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()
    def route_change(_):
        page.views.clear()
        print(pages[0].page.route)

        sel = tuple(filter(lambda x: x.page.route == page.route, pages))
        page.views.append(sel[0].get_page())
        page.go(sel[0].page.route)

    page.on_route_change = route_change
    page.go(page.route)
