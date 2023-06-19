import flet as ft
from controller.Auth_Control import Login
from view.AppPage import AppPage
class Authview (AppPage):
    def __init__(self, root, route):
        super().__init__(root=root, route=route)
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    username = ft.Ref[ft.TextField]()
    password = ft.Ref[ft.TextField]()

    def get_page(self,) -> ft.View:
        self.page.controls = [
            ft.TextField(label="Username", prefix_icon=ft.icons.PERSON, width=500,ref=self.username,border='underline',value="Admin"),
            ft.TextField(password=True,label="Password", prefix_icon=ft.icons.KEY, width=500,ref=self.password,border='underline',autofocus=True,value="Admin123",on_submit=self.on_Login),
            ft.Container(height=30),
            ft.FilledButton(text="Login", width=500, on_click=self.on_Login)
        ]
        return self.page

    def on_Login(self, e):
        if (Login(self.password.current.value)) != None:
            self.root.go('/dashboard')
        else:
            self.password.current.error_text = "Incorrect Password"
            self.page.update()
