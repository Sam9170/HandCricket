import flet as ft

def create_loading_screen():
    return ft.Container(
        content=ft.Column([
            ft.ProgressRing(),
            ft.Text("Loading...", style=ft.TextStyle(size=20))
        ], alignment=ft.MainAxisAlignment.CENTER),
        alignment=ft.alignment.center,
        expand=True
    )

def show_loading(page: ft.Page):
    loading_screen = create_loading_screen()
    page.add(loading_screen)
    page.update()
    return loading_screen

def hide_loading(page: ft.Page, loading_screen):
    page.remove(loading_screen)
    page.update()