import flet as ft
from view.AppPage import AppPage
from controller.DashboardController import INPUT_ID
from view.material.IssueBook import *
from controller.BookController import Books,check_borrowed_book
import base64
from controller.Borrow_Controller import borrowed_check, checklatereturn, borrow
from controller.returnController import borrID
from controller.returnController import returnbook
from controller.AddController import AddBook,AddBorrower
from controller.deletecontroller import deletebook,deleteborrower
from controller.MaintenanceController import maintenance,setborrowlimit

class Dashboard(AppPage):
    inputborrowedlimit = ft.Ref[ft.TextField]()
    booklatereturn = 10
    borrowed_book_limit = None
    # ---------- this is for issuebook ---------#
    borrowed_book_limit_messege = ft.Ref[ft.Text]()
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
# ----------this is for returnbook----------#
    InputIDreturn = ft.Ref[ft.TextField]()
    avatar = ft.Ref[ft.Container]()
    name = ft.Ref[ft.TextField]()
    lastname = ft.Ref[ft.TextField]()
    address = ft.Ref[ft.TextField]()
    phonenumber = ft.Ref[ft.TextField]()
    course = ft.Ref[ft.TextField]()
    email = ft.Ref[ft.TextField]()
    returnlistview = ft.Ref[ft.Row]()
    returncells = ft.Ref[ft.DataTable]()
    bookidreturn = ft.Ref[ft.TextField]()
# ---------For change page----------#
    issuebookvisible = ft.Ref[ft.Container]()
    returnbookvisile = ft.Ref[ft.Container]()
    addbookvisible = ft.Ref[ft.Container]()
    pulloutbookvisible = ft.Ref[ft.Container]()
    addborrowervisible = ft.Ref[ft.Container]()
    dashboardvisible = ft.Ref[ft.Container]()
    maintenancevisible = ft.Ref[ft.Container]()
#----------For Addbook---------------#
    addbookbutton = ft.Ref[ft.Text]()
    showiddialog = None
    addshowcreateid = ft.Ref[ft.Column]()
    book_id_created = ft.Ref[ft.Column]()
    abtitle = ft.Ref[ft.TextField]()
    abcategory = ft.Ref[ft.TextField]()
    abauthor = ft.Ref[ft.TextField]()
    abimage = ft.Ref[ft.Container]()
    abprice = ft.Ref[ft.TextField]()
    abimagepath = None
    abqty = ft.Ref[ft.TextField]()
#-----------For Addborrower------=---#
    id_created = ft.Ref[ft.Text]()
    create_id_dialog = None
    fillouterror = ft.Ref[ft.Text]()
    adborrimage = ft.Ref[ft.Container]()
    adborrimagepath = None
    adborrfname = ft.Ref[ft.TextField]()
    adborrlname = ft.Ref[ft.TextField]()
    adborremail = ft.Ref[ft.TextField]()
    adborrpnumber = ft.Ref[ft.TextField]()
    adborraddress = ft.Ref[ft.TextField]()
    adborrcourse = ft.Ref[ft.TextField]()
#-----------pullout book ----------------#
    pulloutbookID = ft.Ref[ft.TextField]()
    pulloutbooktitle = ft.Ref[ft.TextField]()
    pulloutbookcategory = ft.Ref[ft.TextField]()
    pulloutbookauthor = ft.Ref[ft.TextField]()
    pulloutbookprice  = ft.Ref[ft.TextField]()
    pulloutbookimage = ft.Ref[ft.Container]()
    pulloutbutton = ft.Ref[ft.ElevatedButton]()

    def __init__(self, root, route):
        super().__init__(root=root, route=route)
        self.page.did_mount = self.did_mount

    def borrowedlimitupdate(self,e):
        maintenance(borrowedlimit=self.inputborrowedlimit.current.value)
        self.page.update()

    def close_dlg(self,e):
        self.showiddialog.open = False
        self.abtitle.current.value = ""
        self.abqty.current.value = ""
        self.abprice.current.value = ""
        self.abauthor.current.value = ""
        self.abimagepath = ""
        self.abimage.current.image_src_base64 = ""
        self.abcategory.current.value = ""
        self.page.page.update()

    def close_dlg2(self, e):
        self.create_id_dialog.open = False
        self.adborrpnumber.current.value = ""
        self.adborraddress.current.value = ""
        self.adborrcourse.current.value = ""
        self.adborrimage.current.image_src_base64 = ""
        self.adborremail.current.value = ""
        self.adborrimagepath = ""
        self.adborrfname.current.value = ""
        self.adborrlname.current.value = ""
        self.page.page.update()
    def image_to_base64(self,file_path):
        with open(file_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            return encoded_string.decode("utf-8")

    def image_for_borrower(self,e: ft.FilePickerResultEvent):
        if e.files:
            for file in e.files:
                file_path = file.path.replace("\\", "/")
                self.adborrimage.current.image_src_base64 = self.image_to_base64(file_path)
                self.adborrimagepath = file_path
                print(self.adborrimagepath)
                self.page.update()
    def addborrower(self,e):
        if \
                (
                        self.adborrfname.current.value == None or self.adborrlname.current.value == None or self.adborrcourse.current.value == None or self.adborrimagepath == None or self.adborremail.current.value == None or self.adborrpnumber.current.value == None or self.adborraddress.current.value == None
                ):
            self.fillouterror.current.value = "You Forget Fill Out SomeThing!"
            self.page.update()
        else:
            self.addborrid=AddBorrower(fname=self.adborrfname.current.value,lname=self.adborrlname.current.value,email=self.adborremail.current.value,pnumber=self.adborrpnumber.current.value,address=self.adborraddress.current.value,avatar_path=self.adborrimagepath,course=self.adborrcourse.current.value)
            self.page.page.dialog = self.create_id_dialog
            self.create_id_dialog.open = True
            self.id_created.current.value = f'BORROWER_ID: {self.addborrid}'
            self.page.page.update()


    def on_dialog_result(self,e: ft.FilePickerResultEvent):
        if e.files:
            for file in e.files:
                file_path = file.path.replace("\\", "/")
                self.abimage.current.image_src_base64 = self.image_to_base64(file_path)
                self.abimagepath = file_path
                self.page.update()

    def delborrower(self,e):
        pass
        #deleteborrower(borrrowerID=)
    def PULLOUT(self,e):
        deletebook(bookID=self.pulloutbookID.current.value)
        self.pulloutbooktitle.current.value = None
        self.pulloutbookcategory.current.value = None
        self.pulloutbookauthor.current.value = None
        self.pulloutbookimage.current.image_src_base64 = None
        self.pulloutbookprice.current.value = None
        self.pulloutbutton.current.disabled = True
        self.page.update()
    def delbook(self,e):
        try:
            self.extractbook = Books(self.pulloutbookID.current.value)
            self.pulloutbooktitle.current.value=self.extractbook[1]#title
            self.pulloutbookcategory.current.value=self.extractbook[2]#category
            self.pulloutbookauthor.current.value=self.extractbook[3]#author
            self.pulloutbookimage.current.image_src_base64=base64.b64encode(self.extractbook[4]).decode('utf-8')
            self.pulloutbookprice.current.value=self.extractbook[5]#price
            self.pulloutbutton.current.disabled = False
            self.page.update()
        except:
            self.pulloutbooktitle.current.value = None
            self.pulloutbookcategory.current.value = None
            self.pulloutbookauthor.current.value = None
            self.pulloutbookimage.current.image_src_base64 = None
            self.pulloutbookprice.current.value = None
            self.pulloutbutton.current.disabled = True
            self.page.update()





    def addbook(self,e):
        if (self.abimagepath == None or self.abtitle.current.value == None
        or self.abcategory.current.value == None or self.abauthor.current.value == None
        or self.abprice.current.value == None
        ):
            self.addbookbutton.current.value = "You Forget FillOut SomeThing!"
            self.page.update()
        else:
            self.showcreated=AddBook(title=self.abtitle.current.value,categoty=self.abcategory.current.value,author=self.abauthor.current.value,image_path=self.abimagepath,price=self.abprice.current.value,qty=self.abqty.current.value)
            for i in self.showcreated:
                self.addshowcreateid.current.controls.append \
                    (
                        ft.Row \
                            (
                                controls=\
                                [
                                    ft.Text \
                                        (
                                            value=i[0]
                                        ),
                                    ft.Container \
                                        (
                                            width=125
                                        ),
                                    ft.Text \
                                        (
                                            value=i[1]
                                        )
                                ]
                            )
                    )
            self.page.page.dialog = self.showiddialog
            self.showiddialog.open = True
            self.addbookbutton.current.value = ''
            self.page.page.update()
    def pagetoissue(self,e):
        self.returnbookvisile.current.visible = False
        self.issuebookvisible.current.visible = True
        self.addbookvisible.current.visible = False
        self.pulloutbookvisible.current.visible = False
        self.addborrowervisible.current.visible = False
        self.dashboardvisible.current.visible = False
        self.maintenancevisible.current.visible = False
        borrowed_check()
        checklatereturn()
        self.page.update()
    def pagetoreturn(self,e):
        self.returnbookvisile.current.visible = True
        self.issuebookvisible.current.visible = False
        self.addbookvisible.current.visible = False
        self.pulloutbookvisible.current.visible = False
        self.addborrowervisible.current.visible = False
        self.dashboardvisible.current.visible = False
        self.maintenancevisible.current.visible = False
        borrowed_check()
        checklatereturn()
        self.page.update()
    def pagetoaddbook(self,e):
        self.returnbookvisile.current.visible = False
        self.issuebookvisible.current.visible = False
        self.addbookvisible.current.visible = True
        self.pulloutbookvisible.current.visible = False
        self.addborrowervisible.current.visible = False
        self.dashboardvisible.current.visible = False
        self.maintenancevisible.current.visible = False
        borrowed_check()
        checklatereturn()
        self.page.update()
    def pagetodeletebook(self,e):
        self.returnbookvisile.current.visible = False
        self.issuebookvisible.current.visible = False
        self.addbookvisible.current.visible = False
        self.pulloutbookvisible.current.visible = True
        self.addborrowervisible.current.visible = False
        self.dashboardvisible.current.visible = False
        self.maintenancevisible.current.visible = False
        borrowed_check()
        checklatereturn()
        self.page.update()
    def pagetoaddborrower(self, e):
        self.returnbookvisile.current.visible = False
        self.issuebookvisible.current.visible = False
        self.addbookvisible.current.visible = False
        self.pulloutbookvisible.current.visible = False
        self.addborrowervisible.current.visible = True
        self.dashboardvisible.current.visible = False
        self.maintenancevisible.current.visible = False
        borrowed_check()
        checklatereturn()
        self.page.update()
    def pagetodashboard(self,e):
        self.returnbookvisile.current.visible = False
        self.issuebookvisible.current.visible = False
        self.addbookvisible.current.visible = False
        self.pulloutbookvisible.current.visible = False
        self.addborrowervisible.current.visible = False
        self.dashboardvisible.current.visible = True
        self.maintenancevisible.current.visible = False
        borrowed_check()
        checklatereturn()
        self.page.update()
    def pagetomaintenance(self,e):
        self.returnbookvisile.current.visible = False
        self.issuebookvisible.current.visible = False
        self.addbookvisible.current.visible = False
        self.pulloutbookvisible.current.visible = False
        self.addborrowervisible.current.visible = False
        self.dashboardvisible.current.visible = False
        self.maintenancevisible.current.visible = True
        borrowed_check()
        checklatereturn()
        self.page.update()

    def pagetologout(self,e):
        self.root.go('/')
    def returnbutton(self, e):
        try:
            returnbook(self.bookidreturn.current.value)
            self.bookidreturn.current.value = None
            self.bookidreturn.current.autofocus = True
            self.page.update()

        except:
            self.bookidreturn.current.autofocus = True
            self.page.update()

    def returnchecker(self, e):
        self.returncells.current.rows.clear()
        self.setreturn = borrID(self.InputIDreturn.current.value)

        if len(self.setreturn) == 0:
            self.name.current.value = None
            self.lastname.current.value = None
            self.email.current.value = None
            self.phonenumber.current.value = None
            self.address.current.value = None
            self.avatar.current.image_src_base64 = None
            self.course.current.value = None
            self.page.update()

        for row in self.setreturn:
            self.name.current.value = row[5]  # fname
            self.lastname.current.value = row[6]  # lastname
            self.email.current.value = row[7]  # email
            self.phonenumber.current.value = row[8]  # phonenum
            self.address.current.value = row[9]  # address
            self.avatar.current.image_src_base64 = base64.b64encode(row[10]).decode('utf-8')
            self.course.current.value = row[11]  # course
            self.returncells.current.rows.append(
                ft.DataRow
                (
                    cells=[
                        ft.DataCell(ft.Text(value=row[0])),
                        ft.DataCell(ft.Text(value=row[1])),
                        ft.DataCell(ft.Text(value=row[2])),
                        ft.DataCell(ft.Text(value=row[3])),
                        ft.DataCell(ft.Text(value=row[4])),
                    ]
                )
            )
            self.page.update()

    def Borrow_button(self, e):
        if len(check_borrowed_book(self.InputID.current.value)) >= self.borrowed_book_limit:
            self.borrowed_book_limit_messege.current.value = f"BorrowedLimitReached: {self.borrowed_book_limit}"
            self.page.update()
        else:
            borrow(borrowerID=self.InputID.current.value,bookID=self.bookid.current.value, daylimit=self.daylimit)
            self.bookid.current.value = None
            self.booktitle.current.value = None
            self.bookcategory.current.value = None
            self.bookauthor.current.value = None
            self.bookimage.current.image_src_base64 = None
            self.bookprice.current.value = None
            self.page.update()

    def IDchecker(self, e):

        try:
            self.Set_book_info = Books(self.bookid.current.value)
            self.booktitle.current.value = self.Set_book_info[1]
            self.bookcategory.current.value = self.Set_book_info[2]
            self.bookauthor.current.value = self.Set_book_info[3]
            self.bytesrt = self.Set_book_info[4]
            self.bookimage.current.image_src_base64 = base64.b64encode(
                self.bytesrt).decode('utf-8')
            self.bookprice.current.value = self.Set_book_info[5]
            self.issuebutton.current.disabled = False
            if self.booktitle.current.value != None:
                self.issuebutton.current.visible = True
            else:
                self.issuebutton.current.disabled = False
            self.page.update()
        except:
            self.borrowed_book_limit_messege.current.value = None
            self.issuebutton.current.disabled = True
            self.booktitle.current.value = None
            self.bookcategory.current.value = None
            self.bookauthor.current.value = None
            self.bookimage.current.image_src_base64 = None
            self.bookprice.current.value = None
            self.page.update()

    def checker(self, e):
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
        borrowed_check()
        checklatereturn()
        self.borrowed_book_limit = setborrowlimit()[1]
        self.inputborrowedlimit.current.value = setborrowlimit()[1]
        self.file_picker2 = ft.FilePicker(on_result=self.image_for_borrower)
        self.file_picker = ft.FilePicker(on_result=self.on_dialog_result)
        self.page.page.overlay.append(self.file_picker)
        self.page.page.overlay.append(self.file_picker2)
        self.page.update()
        self.showiddialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("There is the ID:"),
        content=ft.Column \
            (
                ref=self.addshowcreateid,
                controls=\
                [
                    ft.Row \
                        (
                            controls=\
                            [
                                ft.Text \
                                    (
                                        value="ID:"
                                    ),
                                ft.Container \
                                    (
                                        width=150
                                    ),
                                ft.Text \
                                    (
                                        value="TITLE:"
                                    )
                            ]
                        )
                ]
            ),
        actions=[
            ft.TextButton("ok", on_click=self.close_dlg)
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        self.create_id_dialog =ft.AlertDialog(
        modal=True,
        title=ft.Text("There is the ID:"),
        content=ft.Text(ref=self.id_created),
        actions=[
            ft.TextButton("ok", on_click=self.close_dlg2)
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

    def get_page(self) -> ft.View:
        self.page.controls =\
            [
                ft.ResponsiveRow
                (
                    controls=[
                        ft.Column
                        (
                            col=2,
                            controls=[
                                ft.Container
                                (
                                    bgcolor=ft.colors.SECONDARY_CONTAINER,
                                    padding=10,
                                    border_radius=16,
                                    width=250,
                                    height=820,
                                    content=ft.Column
                                    (
                                        controls=[
                                            ft.Container
                                            (
                                                height=5
                                            ),
                                            ft.TextButton
                                            (
                                                text="Dashboard",
                                                icon=ft.icons.DASHBOARD,
                                                on_click=self.pagetodashboard,

                                            ),
                                            ft.TextButton
                                            (
                                                text="Add Book",
                                                icon=ft.icons.MY_LIBRARY_BOOKS,
                                                on_click=self.pagetoaddbook,
                                            ),
                                            ft.TextButton
                                            (
                                                text="PullOut Book",
                                                icon=ft.icons.DELETE,
                                                on_click=self.pagetodeletebook,
                                            ),
                                            ft.TextButton
                                            (
                                                text="Add Borrower",
                                                icon=ft.icons.PERSON_OUTLINED,
                                                on_click=self.pagetoaddborrower,
                                            ),
                                            ft.TextButton
                                            (
                                                text="Return Book",
                                                icon=ft.icons.KEYBOARD_RETURN,
                                                on_click=self.pagetoreturn,
                                            ),
                                            ft.TextButton
                                            (
                                                text="IssueBook",
                                                icon=ft.icons.MENU_BOOK,
                                                on_click=self.pagetoissue,
                                            ),
                                            ft.TextButton
                                            (
                                                text="Maintenance",
                                                icon=ft.icons.SETTINGS,
                                                on_click=self.pagetomaintenance
                                            ),
                                            ft.TextButton
                                            (
                                                text="LogOut",
                                                icon=ft.icons.LOGOUT,
                                                on_click=self.pagetologout
                                            )
                                        ]
                                    )
                                )
                            ]
                        ),
                        ft.Column
                        (
                            ref=None,
                            col=10,
                            controls=[
                                ft.Container \
                                    (
                                        ref=None,
                                        visible=False
                                    ),
                                ft.Container \
                                    (
                                        padding=10,
                                        bgcolor=ft.colors.TERTIARY_CONTAINER,
                                        width=10000,
                                        height=820,
                                        border_radius=15,
                                        ref=self.maintenancevisible,
                                        visible=True,
                                        content= \
                                            (
                                                ft.Column \
                                                    (
                                                        controls=\
                                                        [
                                                            ft.Container \
                                                                (
                                                                    padding=10,
                                                                    border_radius=9,
                                                                    bgcolor=ft.colors.ON_TERTIARY,
                                                                    width=10000,
                                                                    height=90,
                                                                    content= \
                                                                        (

                                                                            ft.Text \
                                                                                (
                                                                                    "Maintenance",
                                                                                    size=50
                                                                                )
                                                                        )
                                                                ),
                                                            ft.Container \
                                                                (
                                                                    height=15
                                                                ),
                                                            ft.Row \
                                                                (
                                                                    controls=\
                                                                    [
                                                                        ft.TextField \
                                                                            (
                                                                                ref=self.inputborrowedlimit,
                                                                                label='BorrowedLimit',
                                                                                on_submit=self.borrowedlimitupdate,

                                                                            ),
                                                                        ft.Dropdown \
                                                                            (
                                                                                label="Theme",
                                                                                options=\
                                                                                [
                                                                                    ft.dropdown.Option(""),
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
                                        padding=10,
                                        bgcolor=ft.colors.TERTIARY_CONTAINER,
                                        width=10000,
                                        height=820,
                                        border_radius=15,
                                        ref=self.addborrowervisible,
                                        visible=False,
                                        content= \
                                            (
                                                ft.Column \
                                                    (
                                                        controls=\
                                                        [
                                                            ft.Container \
                                                                (

                                                                    padding=10,
                                                                    border_radius=9,
                                                                    bgcolor=ft.colors.ON_TERTIARY,
                                                                    width=10000,
                                                                    height=90,
                                                                    content= \
                                                                        (
                                                                            ft.Text \
                                                                                (
                                                                                    value='ADD BORROWER',
                                                                                    size=50
                                                                                )
                                                                        )
                                                                ),
                                                            ft.Container \
                                                                (
                                                                    height=15
                                                                ),
                                                            ft.Container \
                                                                (
                                                                    content= \
                                                                        (
                                                                            ft.Row \
                                                                                (
                                                                                    controls=\
                                                                                    [
                                                                                        ft.Column \
                                                                                            (
                                                                                                controls=\
                                                                                                [
                                                                                                    ft.TextField \
                                                                                                        (
                                                                                                            ref=self.adborrfname,
                                                                                                            prefix_icon=ft.icons.PERSON,
                                                                                                            label='Firstname'
                                                                                                        ),
                                                                                                    ft.TextField \
                                                                                                        (
                                                                                                            ref=self.adborremail,
                                                                                                            prefix_icon=ft.icons.EMAIL_OUTLINED,
                                                                                                            label='Email'
                                                                                                        ),
                                                                                                    ft.TextField \
                                                                                                        (
                                                                                                            ref=self.adborraddress,
                                                                                                            prefix_icon=ft.icons.HOME_MAX_OUTLINED,
                                                                                                            label='Address'
                                                                                                        )
                                                                                                ]
                                                                                            ),
                                                                                        ft.Column \
                                                                                            (
                                                                                                controls=\
                                                                                                [
                                                                                                    ft.TextField \
                                                                                                        (
                                                                                                            ref=self.adborrlname,
                                                                                                            prefix_icon=ft.icons.PERSON,
                                                                                                            label='Lastname'
                                                                                                        ),
                                                                                                    ft.TextField \
                                                                                                        (
                                                                                                            ref=self.adborrpnumber,
                                                                                                            prefix_icon=ft.icons.PHONE,
                                                                                                            label='Phone'
                                                                                                        ),
                                                                                                    ft.TextField \
                                                                                                        (
                                                                                                            ref=self.adborrcourse,
                                                                                                            prefix_icon=ft.icons.GOLF_COURSE_OUTLINED,
                                                                                                            label='Course'
                                                                                                        )
                                                                                                ]
                                                                                            ),
                                                                                        ft.Container \
                                                                                            (
                                                                                                width=100
                                                                                            ),
                                                                                        ft.Container \
                                                                                            (
                                                                                                content= \
                                                                                                    (
                                                                                                        ft.Column \
                                                                                                            (
                                                                                                                controls= \
                                                                                                                [
                                                                                                                    ft.Container \
                                                                                                                        (
                                                                                                                            image_fit=ft.ImageFit.COVER,
                                                                                                                            ref=self.adborrimage,
                                                                                                                            border_radius=16,
                                                                                                                            width=170,
                                                                                                                            height=170,
                                                                                                                            bgcolor=ft.colors.ON_TERTIARY
                                                                                                                        ),
                                                                                                                    ft.ElevatedButton \
                                                                                                                        (
                                                                                                                            width=170,
                                                                                                                            text='BROWSE',
                                                                                                                            on_click=lambda _: self.file_picker2.pick_files(allow_multiple=True)
                                                                                                                        )
                                                                                                                ]
                                                                                                            )
                                                                                                    )
                                                                                            )
                                                                                    ]
                                                                                )
                                                                        )
                                                                ),
                                                            ft.ElevatedButton \
                                                                (
                                                                    text="Register",
                                                                    on_click=self.addborrower,
                                                                    width=1200
                                                                ),
                                                            ft.Text \
                                                                (
                                                                    color=ft.colors.ERROR,
                                                                    value="",
                                                                    ref=self.fillouterror
                                                                )

                                                        ]
                                                    )
                                            )
                                    ),
                                ft.Container \
                                    (
                                        ref=self.dashboardvisible,
                                        visible=False
                                    ),
                                #---------------FOR PULLOUT BOOK-----------------#
                                ft.Container \
                                    (
                                        padding=10,
                                        bgcolor=ft.colors.TERTIARY_CONTAINER,
                                        width=10000,
                                        height=820,
                                        border_radius=15,
                                        ref=self.pulloutbookvisible,
                                        visible=False,
                                        content= \
                                            (
                                                ft.Column \
                                                    (
                                                        controls=\
                                                        [
                                                            ft.Container \
                                                                (
                                                                    padding=10,
                                                                    border_radius=9,
                                                                    bgcolor=ft.colors.ON_TERTIARY,
                                                                    width=10000,
                                                                    height=90,
                                                                    content= \
                                                                        (
                                                                            ft.Text \
                                                                                (
                                                                                    value="PullOut Book",
                                                                                    size=50
                                                                                )
                                                                        )
                                                                ),
                                                            ft.TextField \
                                                                (
                                                                    ref=self.pulloutbookID,
                                                                    label='BookID',
                                                                    on_change=self.delbook
                                                                ),
                                                            ft.Container \
                                                                (
                                                                    width=10
                                                                ),
                                                            ft.Container \
                                                                (
                                                                    content= \
                                                                        (
                                                                            ft.Row \
                                                                                (
                                                                                    controls=\
                                                                                    [
                                                                                        ft.Column \
                                                                                            (
                                                                                                controls=\
                                                                                                [
                                                                                                    ft.TextField \
                                                                                                        (
                                                                                                            width=450,
                                                                                                            ref=self.pulloutbooktitle,
                                                                                                            label='Title'
                                                                                                        ),
                                                                                                    ft.TextField \
                                                                                                        (
                                                                                                            width=450,
                                                                                                            ref=self.pulloutbookcategory,
                                                                                                            label='category'
                                                                                                        ),
                                                                                                    ft.TextField \
                                                                                                        (
                                                                                                            width=450,
                                                                                                            ref=self.pulloutbookauthor,
                                                                                                            label='author'
                                                                                                        ),
                                                                                                    ft.TextField \
                                                                                                        (
                                                                                                            width=450,
                                                                                                            ref=self.pulloutbookprice,
                                                                                                            label='price'
                                                                                                        )
                                                                                                ]
                                                                                            ),
                                                                                        ft.Container \
                                                                                            (
                                                                                                width=200
                                                                                            ),
                                                                                        ft.Container \
                                                                                            (
                                                                                                image_fit=ft.ImageFit.COVER,
                                                                                                ref=self.pulloutbookimage,
                                                                                                border_radius=16,
                                                                                                bgcolor=ft.colors.ON_TERTIARY,
                                                                                                width=250,
                                                                                                height=250
                                                                                            )
                                                                                    ]
                                                                                )
                                                                        )
                                                                ),
                                                            ft.ElevatedButton \
                                                                (
                                                                    ref=self.pulloutbutton,
                                                                    disabled=True,
                                                                    on_click=self.PULLOUT,
                                                                    text="PULLOUT",
                                                                    width=1200
                                                                )
                                                        ]
                                                    )
                                            )
                                    ),
                                ft.Container \
                                    (
                                        ####################################### For addbook

                                        ref=self.addbookvisible,
                                        visible=False,
                                        padding=10,
                                        bgcolor=ft.colors.TERTIARY_CONTAINER,
                                        width=10000,
                                        height=820,
                                        border_radius=15,
                                        content= \
                                            (
                                                ft.Column \
                                                    (
                                                        controls=\
                                                        [
                                                            ft.Container \
                                                                (
                                                                    padding=10,
                                                                    border_radius=9,
                                                                    bgcolor=ft.colors.ON_TERTIARY,
                                                                    width=10000,
                                                                    height=90,
                                                                    content= \
                                                                        (
                                                                            ft.Text \
                                                                                (
                                                                                    value="ADD BOOK",
                                                                                    size=50
                                                                                )
                                                                        )
                                                                ),
                                                            ft.Container \
                                                                (
                                                                    content= \
                                                                        (
                                                                            ft.Row \
                                                                                (
                                                                                    controls=\
                                                                                    [
                                                                                        ft.Column \
                                                                                            (
                                                                                                controls=\
                                                                                                [
                                                                                                    ft.TextField \
                                                                                                        (
                                                                                                            label="Title",
                                                                                                            ref=self.abtitle,
                                                                                                            width=450,
                                                                                                        ),
                                                                                                    ft.TextField \
                                                                                                        (
                                                                                                            label="Category",
                                                                                                            ref=self.abcategory,
                                                                                                            width=450,
                                                                                                        ),
                                                                                                    ft.TextField \
                                                                                                        (
                                                                                                            label="Author",
                                                                                                            ref=self.abauthor,
                                                                                                            width=450,
                                                                                                        ),
                                                                                                    ft.TextField \
                                                                                                            (
                                                                                                            label="Price",
                                                                                                            ref=self.abprice,
                                                                                                            width=450,
                                                                                                        ),
                                                                                                    ft.TextField \
                                                                                                        (
                                                                                                            label='How many?',
                                                                                                            ref=self.abqty,
                                                                                                            width=450
                                                                                                        )
                                                                                                ]
                                                                                            ),
                                                                                        ft.Container \
                                                                                            (
                                                                                                width=200

                                                                                            ),
                                                                                        ft.Container \
                                                                                            (
                                                                                                content= \
                                                                                                    (
                                                                                                        ft.Column \
                                                                                                            (
                                                                                                                controls=\
                                                                                                                [
                                                                                                                    ft.Container \
                                                                                                                        (
                                                                                                                            image_fit=ft.ImageFit.COVER,
                                                                                                                            ref=self.abimage,
                                                                                                                            border_radius=16,
                                                                                                                            bgcolor=ft.colors.ON_TERTIARY,
                                                                                                                            width=250,
                                                                                                                            height=250

                                                                                                                        ),
                                                                                                                    ft.Container \
                                                                                                                        (
                                                                                                                            content= \
                                                                                                                                (
                                                                                                                                    ft.Row \
                                                                                                                                        (
                                                                                                                                            controls=\
                                                                                                                                            [
                                                                                                                                                ft.ElevatedButton \
                                                                                                                                                    (
                                                                                                                                                        width=250,
                                                                                                                                                        text="BROWSE",
                                                                                                                                                        on_click=lambda _: self.file_picker.pick_files(allow_multiple=True)
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
                                                                        )
                                                                ),
                                                            ft.ElevatedButton \
                                                                (
                                                                    text="AddBook",
                                                                    width=800,
                                                                    on_click=self.addbook
                                                                ),
                                                            ft.Text \
                                                                (
                                                                    value="",
                                                                    ref=self.addbookbutton,
                                                                    color=ft.colors.ERROR
                                                                )
                                                        ]
                                                    )
                                            )
                                    ),
                                ft.Container
                                (
                                    #############################################
                                    visible=False,  # >>> THIS FOR RETURNBOOK PAGE
                                    padding=10,
                                    bgcolor=ft.colors.TERTIARY_CONTAINER,
                                    width=10000,
                                    height=820,
                                    border_radius=15,
                                    ref=self.returnbookvisile,
                                    content=(
                                        ft.Column(
                                            controls=[
                                                ft.Container(
                                                    padding=10,
                                                    border_radius=9,
                                                    bgcolor=ft.colors.ON_TERTIARY,
                                                    width=10000,
                                                    height=90,
                                                    content=(
                                                        ft.Text(
                                                            value="Return",
                                                            size=50
                                                        )
                                                    )
                                                ),
                                                ft.TextField(
                                                    ref=self.InputIDreturn,
                                                    label="ID:",
                                                    on_change=self.returnchecker
                                                ),
                                                ft.Container(
                                                    height=120,
                                                    content=ft.Row(
                                                        controls=[
                                                            ft.Container(
                                                                width=10
                                                            ),
                                                            ft.Container(
                                                                image_fit=ft.ImageFit.COVER,
                                                                image_src_base64=None,
                                                                border_radius=25,
                                                                width=150,
                                                                height=130,
                                                                ref=self.avatar
                                                            ),
                                                            ft.Container(
                                                                width=10
                                                            ),
                                                            ft.Column(
                                                                controls=[
                                                                    ft.TextField(
                                                                        height=55,
                                                                        label="Name",
                                                                        ref=self.name
                                                                    ),
                                                                    ft.TextField(
                                                                        height=55,
                                                                        label="Address",
                                                                        ref=self.address
                                                                    )
                                                                ]
                                                            ),
                                                            ft.Column(
                                                                controls=[
                                                                    ft.TextField(
                                                                        height=55,
                                                                        label="Lastname",
                                                                        ref=self.lastname
                                                                    ),
                                                                    ft.TextField(
                                                                        height=55,
                                                                        label="Phonenumber",
                                                                        ref=self.phonenumber
                                                                    )
                                                                ]
                                                            ),
                                                            ft.Column(
                                                                controls=[
                                                                    ft.TextField(
                                                                        height=55,
                                                                        label="Course",
                                                                        ref=self.course
                                                                    ),
                                                                    ft.TextField(
                                                                        height=55,
                                                                        label="Email",
                                                                        ref=self.email
                                                                    )

                                                                ]
                                                            )
                                                        ]
                                                    )
                                                ),
                                                ft.Container(
                                                    ref=None,
                                                    height=500,
                                                    width=1200,
                                                    content=(
                                                        ft.Column(
                                                            controls=[
                                                                ft.TextField(
                                                                    autofocus=True,
                                                                    ref=self.bookidreturn,
                                                                    label="Book ID:",
                                                                    on_submit=self.returnbutton
                                                                ),
                                                                ft.ElevatedButton(
                                                                    on_click=self.returnbutton,
                                                                    text='RETURN'
                                                                ),
                                                                ft.Container(
                                                                    content=(
                                                                        ft.DataTable(
                                                                            ref=self.returncells,
                                                                            columns=[
                                                                                ft.DataColumn(
                                                                                    ft.Text('Return ID')),
                                                                                ft.DataColumn(
                                                                                    ft.Text('Book Title')),
                                                                                ft.DataColumn(
                                                                                    ft.Text('Issue Date')),
                                                                                ft.DataColumn(
                                                                                    ft.Text('Return Date')),
                                                                                ft.DataColumn(
                                                                                    ft.Text('Late Return Date'))
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
                                    )

                                ),
                                # -------------------------------------------------------------------------------------------------------------------------------------------------------------#
                                ft.Container(
                                    ref=self.issuebookvisible,
                                    visible=False,  # >>> THIS FOR ISSUEBOOK PAGE
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
                                                        height=90,
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
                                                                            ft.Container(
                                                                                width=10
                                                                            ),
                                                                            AVATAR,
                                                                            ft.Container(
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
                                                ft.Container(
                                                        width=5
                                                        ),
                                                ft.Container(
                                                        ref=self.bookdisplay,
                                                        content=(
                                                            ft.Column(
                                                                controls=[
                                                                    ft.TextField(

                                                                        ref=self.bookid,
                                                                        border_color=ft.colors.PRIMARY,
                                                                        label="Book ID:",
                                                                        on_change=self.IDchecker
                                                                    ),
                                                                    ft.Container(
                                                                        content=ft.Row(
                                                                            controls=[
                                                                                ft.Container(
                                                                                    width=10
                                                                                ),
                                                                                ft.Container(
                                                                                    ref=self.bookimage,
                                                                                    border_radius=16,
                                                                                    image_fit=ft.ImageFit.COVER,
                                                                                    width=130,
                                                                                    height=130,
                                                                                    image_src=None

                                                                                ),
                                                                                ft.Container(
                                                                                    width=10
                                                                                ),
                                                                                ft.Column(
                                                                                    controls=[
                                                                                        ft.TextField(
                                                                                            prefix_icon=ft.icons.TITLE_OUTLINED,
                                                                                            ref=self.booktitle,
                                                                                            width=550,
                                                                                            disabled=True,
                                                                                            border="underline",
                                                                                            label="Title",
                                                                                            border_color=ft.colors.PRIMARY,

                                                                                        ),
                                                                                        ft.TextField(
                                                                                            prefix_icon=ft.icons.CATEGORY_OUTLINED,
                                                                                            ref=self.bookcategory,
                                                                                            width=550,
                                                                                            disabled=True,
                                                                                            border="underline",
                                                                                            border_color=ft.colors.PRIMARY,
                                                                                            label="Category",
                                                                                        )
                                                                                    ]
                                                                                ),
                                                                                ft.Column(
                                                                                    controls=[
                                                                                        ft.TextField(
                                                                                            prefix_icon=ft.icons.PERSON_3,
                                                                                            ref=self.bookauthor,
                                                                                            width=400,
                                                                                            disabled=True,
                                                                                            border="underline",
                                                                                            border_color=ft.colors.PRIMARY,
                                                                                            label="Author"
                                                                                        ),
                                                                                        ft.TextField(
                                                                                            prefix_icon=ft.icons.PRICE_CHANGE_ROUNDED,
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
                                                                    ft.ElevatedButton(
                                                                        disabled=True,
                                                                        on_click=self.Borrow_button,
                                                                        ref=self.issuebutton,
                                                                        width=1200,
                                                                        text="Borrow"
                                                                    ),
                                                                    ft.Text \
                                                                        (
                                                                            ref=self.borrowed_book_limit_messege,
                                                                            color=ft.colors.ERROR
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
