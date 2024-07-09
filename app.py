import flet as ft
import subprocess

def main(page: ft.Page):
    page.title = "Hand Cricket Game"

    def navigate_to(index):
        content.controls.clear()
        if index == 0:
            content.controls.append(home_page())
        elif index == 1:
            content.controls.append(about_page())
        elif index == 2:
            content.controls.append(login_page())
        page.update()

    def login(e):
        username = username_input.value
        password = password_input.value
        if username == "admin" and password == "password":
            login_result.value = "Login Successful!"
            login_result.color = ft.colors.GREEN
            subprocess.run(["python", "TossPage.py"])
        else:
            login_result.value = "Invalid credentials, please try again."
            login_result.color = ft.colors.RED
        page.update()

    def home_page():
        return ft.Text("Welcome to the Home Page!", size=24, text_align=ft.TextAlign.CENTER)

    def about_page():
        return ft.Column([
            ft.Image(src="developer.jpg", width=150, height=150),
            ft.Text("About the Developer", size=24, text_align=ft.TextAlign.CENTER),
            ft.Text("This app was developed by a passionate software developer with expertise in Python and web development. The developer is dedicated to creating efficient and user-friendly applications."),
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)

    def login_page():
        global username_input, password_input, login_result
        username_input = ft.TextField(
            label="Username",
            width=300,
            border_color=ft.colors.BLUE,
            border_width=2,
            focused_border_color=ft.colors.BLUE_ACCENT,
            hint_text="Enter your username",
            icon=ft.icons.PERSON
        )
        password_input = ft.TextField(
            label="Password",
            password=True,
            width=300,
            border_color=ft.colors.BLUE,
            border_width=2,
            focused_border_color=ft.colors.BLUE_ACCENT,
            hint_text="Enter your password",
            icon=ft.icons.LOCK
        )
        login_result = ft.Text("", color=ft.colors.RED)
        return ft.Container(
            content=ft.Column([
                username_input,
                password_input,
                ft.ElevatedButton("Login", on_click=login),
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

    page.navigation_bar = ft.CupertinoNavigationBar(
        bgcolor=ft.colors.INDIGO_400,
        inactive_color=ft.colors.GREY,
        active_color=ft.colors.BLACK,
        on_change=lambda e: navigate_to(e.control.selected_index),
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.icons.PERSON, label="About Us"),
            ft.NavigationBarDestination(
                icon=ft.icons.LOGIN_OUTLINED,
                selected_icon=ft.icons.LOGIN,
                label="Login",
            ),
        ]
    )

    page.add(ft.Container(
        content=ft.Column([
            content
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
        padding=ft.padding.all(20))
    )

ft.app(target=main)
