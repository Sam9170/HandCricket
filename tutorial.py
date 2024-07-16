import flet as ft

def show_tutorial(page: ft.Page):
    def close_tutorial(e):
        page.dialog.open = False
        page.update()

    tutorial_text = [
        "Welcome to Hand Cricket!",
        "1. Show fingers to the camera to play.",
        "2. Match the computer's number to take a wicket or get out.",
        "3. Score more runs than your opponent to win!",
    ]
    
    dialog = ft.AlertDialog(
        title=ft.Text("How to Play", color=ft.colors.WHITE),
        content=ft.Column([ft.Text(text, color=ft.colors.WHITE) for text in tutorial_text]),
        actions=[ft.TextButton("Got it!", on_click=close_tutorial, style=ft.ButtonStyle(color=ft.colors.WHITE))],
        bgcolor=ft.colors.BLUE_GREY_800,
    )
    
    page.dialog = dialog
    dialog.open = True
    page.update()