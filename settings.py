import flet as ft

class GameSettings:
    def __init__(self):
        self.overs = 1
        self.difficulty = "Normal"

    def show_settings_dialog(self, page: ft.Page):
        def save_settings(e):
            self.overs = int(overs_dropdown.value)
            self.difficulty = difficulty_dropdown.value
            page.dialog.open = False
            page.update()

        def cancel(e):
            page.dialog.open = False
            page.update()

        overs_dropdown = ft.Dropdown(
            label="Number of Overs",
            options=[ft.dropdown.Option(str(i)) for i in range(1, 6)],
            value=str(self.overs),
            text_style=ft.TextStyle(color=ft.colors.WHITE),
            label_style=ft.TextStyle(color=ft.colors.WHITE70),
        )
        difficulty_dropdown = ft.Dropdown(
            label="Difficulty",
            options=[ft.dropdown.Option(d) for d in ["Easy", "Normal", "Hard"]],
            value=self.difficulty,
            text_style=ft.TextStyle(color=ft.colors.WHITE),
            label_style=ft.TextStyle(color=ft.colors.WHITE70),
        )

        dialog = ft.AlertDialog(
            title=ft.Text("Game Settings", color=ft.colors.WHITE),
            content=ft.Column([overs_dropdown, difficulty_dropdown]),
            actions=[
                ft.TextButton("Cancel", on_click=cancel, style=ft.ButtonStyle(color=ft.colors.WHITE)),
                ft.TextButton("Save", on_click=save_settings, style=ft.ButtonStyle(color=ft.colors.WHITE)),
            ],
            bgcolor=ft.colors.BLUE_GREY_800,
        )

        page.dialog = dialog
        dialog.open = True
        page.update()

game_settings = GameSettings()