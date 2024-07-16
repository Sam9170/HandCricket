import flet as ft
import subprocess
from theme import apply_theme, TITLE_STYLE, BODY_STYLE
from loading import show_loading, hide_loading
from tutorial import show_tutorial
from settings import game_settings
from leaderboard import leaderboard

# Updated button style
BUTTON_STYLE = ft.ButtonStyle(
    color=ft.colors.WHITE,
    bgcolor=ft.colors.BLUE_GREY_800,
    padding=10,
    shape=ft.RoundedRectangleBorder(radius=10),
)

def main(page: ft.Page):
    page.title = "Hand Cricket Game"
    page.window.maximized = True
    
    # Apply a darker theme
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.theme = ft.Theme(color_scheme=ft.ColorScheme(
        primary=ft.colors.BLUE_400,
        primary_container=ft.colors.BLUE_900,
        secondary=ft.colors.TEAL_400,
        background=ft.colors.BLUE_GREY_900,
    ))

    def navigate_to(index):
        loading_screen = show_loading(page)
        content.controls.clear()
        if index == 0:
            content.controls.append(home_page())
        elif index == 1:
            content.controls.append(about_page())
        elif index == 2:
            content.controls.append(login_page())
        hide_loading(page, loading_screen)
        page.update()

    def login(e):
        username = username_input.value
        password = password_input.value
        if username == "admin" and password == "password":
            login_result.value = "Login Successful!"
            login_result.color = ft.colors.GREEN
            loading_screen = show_loading(page)
            subprocess.run(["python", "TossPage.py"])
            hide_loading(page, loading_screen)
        else:
            login_result.value = "Invalid credentials, please try again."
            login_result.color = ft.colors.RED
        page.update()


    def home_page():
        return ft.Column([
            ft.Text("Welcome to Hand Cricket!", style=TITLE_STYLE, color=ft.colors.WHITE),
            ft.ElevatedButton("How to Play", on_click=lambda _: show_tutorial(page), style=BUTTON_STYLE),
            ft.ElevatedButton("Settings", on_click=lambda _: game_settings.show_settings_dialog(page), style=BUTTON_STYLE),
            ft.ElevatedButton("Leaderboard", on_click=lambda _: leaderboard.show_leaderboard(page), style=BUTTON_STYLE),
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)

    def about_page():
        return ft.Column([
            ft.CircleAvatar(content=ft.Icon(ft.icons.PERSON_2_OUTLINED), color=ft.colors.YELLOW_200, bgcolor=ft.colors.AMBER_700),
            ft.Text("About the Developer", style=TITLE_STYLE, color=ft.colors.WHITE),
            ft.Text("This Game is under development developed by a passionate software developer with expertise in Python. The developer is dedicated to creating efficient and user-friendly applications.", 
                    style=BODY_STYLE, color=ft.colors.WHITE70, text_align=ft.TextAlign.CENTER),
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)

    def login_page():
        global username_input, password_input, login_result
        username_input = ft.TextField(
            label="Username",
            width=300,
            border_color=ft.colors.BLUE_400,
            border_width=2,
            focused_border_color=ft.colors.BLUE_200,
            hint_text="Enter your username",
            icon=ft.icons.PERSON,
            text_style=ft.TextStyle(color=ft.colors.WHITE),
            label_style=ft.TextStyle(color=ft.colors.WHITE70),
        )
        password_input = ft.TextField(
            label="Password",
            password=True,
            width=300,
            border_color=ft.colors.BLUE_400,
            border_width=2,
            focused_border_color=ft.colors.BLUE_200,
            hint_text="Enter your password",
            icon=ft.icons.LOCK,
            text_style=ft.TextStyle(color=ft.colors.WHITE),
            label_style=ft.TextStyle(color=ft.colors.WHITE70),
        )
        login_result = ft.Text("", color=ft.colors.RED)
        return ft.Container(
            content=ft.Column([
                username_input,
                password_input,
                ft.ElevatedButton("Login", on_click=login, style=BUTTON_STYLE),
                login_result
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
            alignment=ft.alignment.center
        )

    global username_input, password_input, login_result
    username_input = ft.TextField()
    password_input = ft.TextField()
    login_result = ft.Text()
    content = ft.Column()

    content.controls.append(home_page())

    page.navigation_bar = ft.NavigationBar(
        bgcolor=ft.colors.BLUE_GREY_800,
        selected_index=0,
        on_change=lambda e: navigate_to(e.control.selected_index),
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.icons.PERSON, label="About Us"),
            ft.NavigationBarDestination(icon=ft.icons.LOGIN, label="Login"),
        ]
    )

    page.add(ft.Container(
        content=content,
        alignment=ft.alignment.center,
        padding=ft.padding.all(20)
    ))

ft.app(target=main)
    

# import flet as ft
# import subprocess
# import sys
# from theme import apply_theme, TITLE_STYLE, BODY_STYLE, BUTTON_STYLE
# from loading import show_loading, hide_loading
# from tutorial import show_tutorial
# from settings import game_settings
# from leaderboard import leaderboard

# def main(page: ft.Page):
#     page.title = "Hand Cricket Game"
#     page.window.maximized = True
    
#     # Apply a darker theme
#     page.bgcolor = ft.colors.BLUE_GREY_900
#     page.theme = ft.Theme(color_scheme=ft.ColorScheme(
#         primary=ft.colors.BLUE_400,
#         primary_container=ft.colors.BLUE_900,
#         secondary=ft.colors.TEAL_400,
#         background=ft.colors.BLUE_GREY_900,
#     ))

#     def navigate_to(index):
#         loading_screen = show_loading(page)
#         content.controls.clear()
#         if index == 0:
#             content.controls.append(home_page())
#         elif index == 1:
#             content.controls.append(about_page())
#         elif index == 2:
#             content.controls.append(login_page())
#         hide_loading(page, loading_screen)
#         page.update()

#     def login(e):
#         username = username_input.value
#         password = password_input.value
#         if username == "admin" and password == "password":
#             login_result.value = "Login Successful!"
#             login_result.color = ft.colors.GREEN
#             loading_screen = show_loading(page)
#             page.update()
#             subprocess.Popen(["python", "TossPage.py"])
#             page.window_destroy()
#         else:
#             login_result.value = "Invalid credentials, please try again."
#             login_result.color = ft.colors.RED
#         page.update()

#     def home_page():
#         return ft.Column([
#             ft.Text("Welcome to Hand Cricket!", style=TITLE_STYLE, color=ft.colors.WHITE),
#             ft.ElevatedButton("How to Play", on_click=lambda _: show_tutorial(page), style=BUTTON_STYLE),
#             ft.ElevatedButton("Settings", on_click=lambda _: game_settings.show_settings_dialog(page), style=BUTTON_STYLE),
#             ft.ElevatedButton("Leaderboard", on_click=lambda _: leaderboard.show_leaderboard(page), style=BUTTON_STYLE),
#         ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)

#     def about_page():
#         return ft.Column([
#             ft.CircleAvatar(content=ft.Icon(ft.icons.PERSON_2_OUTLINED), color=ft.colors.YELLOW_200, bgcolor=ft.colors.AMBER_700),
#             ft.Text("About the Developer", style=TITLE_STYLE, color=ft.colors.WHITE),
#             ft.Text("This Game is under development developed by a passionate software developer with expertise in Python. The developer is dedicated to creating efficient and user-friendly applications.", 
#                     style=BODY_STYLE, color=ft.colors.WHITE70, text_align=ft.TextAlign.CENTER),
#         ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)

#     def login_page():
#         global username_input, password_input, login_result
#         username_input = ft.TextField(
#             label="Username",
#             width=300,
#             border_color=ft.colors.BLUE_400,
#             border_width=2,
#             focused_border_color=ft.colors.BLUE_200,
#             hint_text="Enter your username",
#             icon=ft.icons.PERSON,
#             text_style=ft.TextStyle(color=ft.colors.WHITE),
#             label_style=ft.TextStyle(color=ft.colors.WHITE70),
#         )
#         password_input = ft.TextField(
#             label="Password",
#             password=True,
#             width=300,
#             border_color=ft.colors.BLUE_400,
#             border_width=2,
#             focused_border_color=ft.colors.BLUE_200,
#             hint_text="Enter your password",
#             icon=ft.icons.LOCK,
#             text_style=ft.TextStyle(color=ft.colors.WHITE),
#             label_style=ft.TextStyle(color=ft.colors.WHITE70),
#         )
#         login_result = ft.Text("", color=ft.colors.RED)
#         return ft.Container(
#             content=ft.Column([
#                 username_input,
#                 password_input,
#                 ft.ElevatedButton("Login", on_click=login, style=BUTTON_STYLE),
#                 login_result
#             ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
#             alignment=ft.alignment.center
#         )

#     global username_input, password_input, login_result
#     username_input = ft.TextField()
#     password_input = ft.TextField()
#     login_result = ft.Text()
#     content = ft.Column()

#     content.controls.append(home_page())

#     page.navigation_bar = ft.NavigationBar(
#         bgcolor=ft.colors.BLUE_GREY_800,
#         selected_index=0,
#         on_change=lambda e: navigate_to(e.control.selected_index),
#         destinations=[
#             ft.NavigationBarDestination(icon=ft.icons.HOME, label="Home"),
#             ft.NavigationBarDestination(icon=ft.icons.PERSON, label="About Us"),
#             ft.NavigationBarDestination(icon=ft.icons.LOGIN, label="Login"),
#         ]
#     )

#     page.add(ft.Container(
#         content=content,
#         alignment=ft.alignment.center,
#         padding=ft.padding.all(20)
#     ))

# ft.app(target=main)