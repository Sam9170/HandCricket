import flet as ft

# Define color scheme
PRIMARY_COLOR = ft.colors.BLUE
SECONDARY_COLOR = ft.colors.LIGHT_BLUE_700
BACKGROUND_COLOR = ft.colors.GREY_100
TEXT_COLOR = ft.colors.GREY_900

# Define styles
TITLE_STYLE = ft.TextStyle(size=24, weight=ft.FontWeight.BOLD, color=TEXT_COLOR)
BODY_STYLE = ft.TextStyle(size=16, color=TEXT_COLOR)
BUTTON_STYLE = ft.ButtonStyle(
    color=PRIMARY_COLOR,
    bgcolor=SECONDARY_COLOR,
    padding=10,
    shape=ft.RoundedRectangleBorder(radius=10),
)

def apply_theme(page: ft.Page):
    page.bgcolor = BACKGROUND_COLOR
    page.theme = ft.Theme(color_scheme=ft.ColorScheme(
        primary=PRIMARY_COLOR,
        secondary=SECONDARY_COLOR,
    ))
    page.update()