import flet as ft

def main(page: ft.Page):
    page.title = "Hand Cricket Game"

    def navigate_to(route):
        if route == "Home":
            content.controls.clear()
            content.controls.append(home_page())
        elif route == "About":
            content.controls.clear()
            content.controls.append(about_page())
        elif route == "Login":
            content.controls.clear()
            content.controls.append(login_page())
        page.update()

    def login(e):
        username = username_input.value
        password = password_input.value
        if username == "admin" and password == "password":
            login_result.value = "Login Successful!"
        else:
            login_result.value = "Invalid credentials, please try again."
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
        username_input = ft.TextField(label="Username", width=300)
        password_input = ft.TextField(label="Password", password=True, width=300)
        login_result = ft.Text("", color=ft.colors.RED)
        return ft.Column([
            username_input,
            password_input,
            ft.ElevatedButton("Login", on_click=login),
            login_result
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    global username_input, password_input, login_result
    username_input = ft.TextField()
    password_input = ft.TextField()
    login_result = ft.Text()
    content = ft.Column()

    content.controls.append(home_page())

    navbar = ft.Container(
        ft.Row([
            ft.ElevatedButton("Home", on_click=lambda e: navigate_to("Home")),
            ft.ElevatedButton("About", on_click=lambda e: navigate_to("About")),
            ft.ElevatedButton("Login", on_click=lambda e: navigate_to("Login"))
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
        padding=ft.padding.only(bottom=20)
    )

    page.add(ft.Container(
        content=ft.Column([
            navbar,
            content
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
        padding=ft.padding.all(20))
    )

ft.app(target=main)
