import flet as ft
from view.AppPage import AppPage
from controller.DashboardController import INPUT_ID
from view.material.IssueBook import *
from controller.BookController import Books
import base64
from controller.Borrow_Controller import borrowed_check,checklatereturn,borrow

class Dashboard(AppPage):
#---------- this is for issuebook ---------#
    InputID = ft.Ref[ft.TextField]()
    bookdisplay = ft.Ref[ft.Container]()
    bookid = ft.Ref[ft.TextField]()
    booktitle = ft.Ref[ft.TextField]()
    bookauthor = ft.Ref[ft.TextField]()
    bookcategory = ft.Ref[ft.TextField]()
    bookprice = ft.Ref[ft.TextField]()
    bookimage = ft.Ref[ft.Container]()
    issuebutton = ft.Ref[ft.ElevatedButton]()
    daylimit = 3
#------------------------------------------#
    def __init__(self, root, route):
        super().__init__(root=root, route=route)
        self.page.did_mount = self.did_mount

    def Borrow_button(self,e):
        pass
        #self.borrow = borrow(borrowerID=self.InputID.current.value,bookID=self.bookid.current.value,daylimit=self.daylimit)

    def IDchecker(self,e):
        try:
            self.Set_book_info = Books(self.bookid.current.value)
            self.booktitle.current.value = self.Set_book_info[1]
            self.bookcategory.current.value = self.Set_book_info[2]
            self.bookauthor.current.value = self.Set_book_info[3]
            self.bytesrt = self.Set_book_info[4]
            self.bookimage.current.image_src_base64 = base64.b64encode(self.bytesrt).decode('utf-8')
            self.bookprice.current.value = self.Set_book_info[5]
            if self.booktitle.current.value != None:
                self.issuebutton.current.visible = True
            else:
                self.issuebutton.current.disabled = False
            self.page.update()
        except :
            self.booktitle.current.value = None
            self.bookcategory.current.value = None
            self.bookauthor.current.value = None
            self.bookimage.current.image_src_base64 = None
            self.bookprice.current.value = None
            self.page.update()







    def checker(self,e):
        try:
            self.SetValue = INPUT_ID(self.InputID.current.value)
            FIRSTNAME.value = self.SetValue[0][1]
            LASTNAME.value = self.SetValue[0][2]
            EMAIL.value = self.SetValue[0][3]
            PHONENUMBER.value = self.SetValue[0][4]
            ADDRESS.value = self.SetValue[0][5]
            AVATAR.image_src_base64 = self.SetValue[0][6]
            COURSE.value = self.SetValue[0][7]
            if self.SetValue[0][1] != None:
                self.bookdisplay.current.visible = True
            else:
                self.bookdisplay.current.visible = False
            self.page.update()
        except:
            FIRSTNAME.value = None
            LASTNAME.value = None
            EMAIL.value = None
            PHONENUMBER.value = None
            ADDRESS.value = None
            AVATAR.image_src_base64 = None
            COURSE.value = None
            self.page.update()


    def did_mount(self):
        self.get_page()
        self.bookdisplay.current.visible = False
        borrowed_check()
        checklatereturn()

    def get_page(self) -> ft.View:
        self.page.controls =\
        [
            ft.ResponsiveRow \
                (
                    controls=\
                        [
                            ft.Column \
                                (
                                    col=2,
                                    controls=\
                                    [
                                        ft.Container \
                                            (
                                                bgcolor=ft.colors.SECONDARY_CONTAINER,
                                                padding=10,
                                                border_radius=16,
                                                width=250,
                                                height=820,
                                                content=ft.Column \
                                                    (
                                                        controls=\
                                                        [
                                                            ft.Container \
                                                                (
                                                                    height=5
                                                                ),
                                                            ft.TextButton \
                                                                    (
                                                                    text="Dashboard",
                                                                    icon=ft.icons.DASHBOARD,
                                                                    on_click=None,

                                                                ),
                                                            ft.TextButton \
                                                                (
                                                                    text="AddBook",
                                                                    icon=ft.icons.ADD,
                                                                    on_click=None,
                                                                ),
                                                            ft.TextButton \
                                                                (
                                                                    text="DeleteBook",
                                                                    icon=ft.icons.DELETE,
                                                                    on_click=None,
                                                                ),
                                                            ft.TextButton \
                                                                (
                                                                    text="Payment",
                                                                    icon=ft.icons.PAYMENTS,
                                                                    on_click=None,
                                                                ),
                                                            ft.TextButton \
                                                                (
                                                                    text="ReturnBook",
                                                                    icon=ft.icons.KEYBOARD_RETURN,
                                                                    on_click=None,
                                                                ),
                                                            ft.TextButton \
                                                                (
                                                                    text="IssueBook",
                                                                    icon=ft.icons.MENU_BOOK,
                                                                    on_click=None,
                                                                ),
                                                            ft.TextButton \
                                                                (
                                                                    text="Maintenance",
                                                                    icon=ft.icons.SETTINGS,
                                                                    on_click=None
                                                                ),
                                                            ft.TextButton \
                                                                (
                                                                    text="LogOut",
                                                                    icon=ft.icons.LOGOUT,
                                                                    on_click=None
                                                                )
                                                        ]
                                                    )
                                            )
                                    ]
                                ),
                            ft.Column \
                                (
                                    ref=None,
                                    col=10,
                                    controls= \
                                        [
                                            ft.Container(
                                                visible=True,
                                                padding=10,
                                                bgcolor=ft.colors.TERTIARY_CONTAINER,
                                                width=10000,
                                                height=820,
                                                border_radius=15,
                                                content=(
                                                    ft.Column(
                                                        controls=[
                                                            ft.Container(
                                                                padding=10,
                                                                border_radius=9,
                                                                bgcolor=ft.colors.ON_TERTIARY,
                                                                width=10000,
                                                                height=100,
                                                                content=ft.Text(
                                                                    value=" Issue",
                                                                    size=50,
                                                                    font_family="ROBOTO"
                                                                )
                                                            ),
                                                            ft.Container(
                                                                content=(
                                                                    ft.TextField(
                                                                        label="Student ID:",
                                                                        border_color=ft.colors.PRIMARY,
                                                                        ref=self.InputID,
                                                                        on_change=self.checker,
                                                                        value=None

                                                                    )
                                                                )
                                                            ),
                                                            ft.Container(
                                                                height=120,
                                                                content=(
                                                                    ft.Column(
                                                                        controls=[
                                                                            ft.Row(
                                                                                controls=[
                                                                                    ft.Container \
                                                                                        (
                                                                                            width=10
                                                                                        ),
                                                                                    AVATAR,
                                                                                    ft.Container \
                                                                                        (
                                                                                            width=10
                                                                                        ),
                                                                                    ft.Column(
                                                                                        controls=[
                                                                                            FIRSTNAME,
                                                                                            ADDRESS,
                                                                                        ]
                                                                                    ),
                                                                                    ft.Column(
                                                                                        controls=[
                                                                                            LASTNAME,
                                                                                            PHONENUMBER,
                                                                                        ]
                                                                                    ),
                                                                                    ft.Column(
                                                                                        controls=[
                                                                                            COURSE,
                                                                                            EMAIL,
                                                                                        ]
                                                                                    )
                                                                                ]
                                                                            )
                                                                        ]
                                                                    )
                                                                )
                                                            ),
                                                            ft.Container \
                                                                (
                                                                    width=5
                                                                ),
                                                            ft.Container \
                                                                (
                                                                    ref=self.bookdisplay,
                                                                    content= \
                                                                        (
                                                                            ft.Column \
                                                                                (
                                                                                    controls=\
                                                                                    [
                                                                                        ft.TextField \
                                                                                            (
                                                                                                ref=self.bookid,
                                                                                                border_color=ft.colors.PRIMARY,
                                                                                                label="Book ID:",
                                                                                                on_change=self.IDchecker
                                                                                            ),
                                                                                        ft.Container \
                                                                                            (
                                                                                                content=ft.Row \
                                                                                                    (
                                                                                                        controls=\
                                                                                                        [
                                                                                                            ft.Container \
                                                                                                                (
                                                                                                                    width=10
                                                                                                                ),
                                                                                                            ft.Container \
                                                                                                                (
                                                                                                                    ref=self.bookimage,
                                                                                                                    border_radius=16,
                                                                                                                    image_fit=ft.ImageFit.COVER,
                                                                                                                    width=130,
                                                                                                                    height=130,
                                                                                                                    image_src=None

                                                                                                                ),
                                                                                                            ft.Container \
                                                                                                                (
                                                                                                                    width=10
                                                                                                                ),
                                                                                                            ft.Column \
                                                                                                                (
                                                                                                                    controls=\
                                                                                                                    [
                                                                                                                        ft.TextField \
                                                                                                                            (
                                                                                                                                ref=self.booktitle,
                                                                                                                                width=550,
                                                                                                                                disabled=True,
                                                                                                                                border="underline",
                                                                                                                                label="Title",
                                                                                                                                border_color=ft.colors.PRIMARY,

                                                                                                                            ),
                                                                                                                        ft.TextField \
                                                                                                                            (
                                                                                                                                ref=self.bookcategory,
                                                                                                                                width=550,
                                                                                                                                disabled=True,
                                                                                                                                border="underline",
                                                                                                                                border_color=ft.colors.PRIMARY,
                                                                                                                                label="Category",
                                                                                                                            )
                                                                                                                    ]
                                                                                                                ),
                                                                                                            ft.Column \
                                                                                                                (
                                                                                                                    controls=\
                                                                                                                    [
                                                                                                                        ft.TextField \
                                                                                                                            (
                                                                                                                                ref=self.bookauthor,
                                                                                                                                width=400,
                                                                                                                                disabled=True,
                                                                                                                                border="underline",
                                                                                                                                border_color=ft.colors.PRIMARY,
                                                                                                                                label="Author"
                                                                                                                            ),
                                                                                                                        ft.TextField \
                                                                                                                            (
                                                                                                                                ref=self.bookprice,
                                                                                                                                width=400,
                                                                                                                                disabled=True,
                                                                                                                                border="underline",
                                                                                                                                border_color=ft.colors.PRIMARY,
                                                                                                                                label="Book Price"
                                                                                                                            )
                                                                                                                    ]
                                                                                                                )
                                                                                                        ]
                                                                                                    )
                                                                                            ),
                                                                                        ft.ElevatedButton \
                                                                                            (
                                                                                                on_click=self.Borrow_button,
                                                                                                ref=self.issuebutton,
                                                                                                width=1200,
                                                                                                text="Borrow"
                                                                                            )
                                                                                    ]
                                                                                )
                                                                        )

                                                                )
                                                        ]
                                                    )
                                                )
                                            )
                                        ]
                                )
                        ],
                    expand=True
                )
        ]
        return self.page
