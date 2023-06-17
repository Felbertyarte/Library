import flet as ft
#Select Category
ft.Container \
        (
                visible=False,

        )

#############################
INPUTSID = ft.TextField \
    (
        label="StudentID",
        border_color=ft.colors.PRIMARY,
        border_width=2,
        ref=None,
        on_change=None,
        value=0
    )

AVATAR = ft.Container \
        (
        image_fit=ft.ImageFit.COVER,
        image_src_base64=None,
        border_radius=25,
        width=150,
        height=130
        )

FIRSTNAME = ft.TextField \
        (
        text_size=15,
        height=55,
        border="underline",
        disabled=True,
        label="FirstName",
        value=None
    )
LASTNAME = ft.TextField \
        (
        height=55,
        border="underline",
        disabled=True,
        label="Lastname",
        value=None
    )
ADDRESS = ft.TextField \
        (
        height=55,
        border="underline",
        disabled=True,
        label="address",
        value=None

    )
PHONENUMBER = ft.TextField \
        (
        height=55,
        border="underline",
        disabled=True,
        label="PhoneNumber",
        value=None
    )
EMAIL = ft.TextField \
        (
        height=55,
        border="underline",
        disabled=True,
        label="Email",
        value=None
    )
COURSE = ft.TextField \
        (
        height=55,
        border="underline",
        disabled=True,
        label="Course",
        value=None
    )



