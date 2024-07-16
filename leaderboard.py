import flet as ft
import json

class Leaderboard:
    def __init__(self):
        self.scores = self.load_scores()

    def load_scores(self):
        try:
            with open("leaderboard.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_scores(self):
        with open("leaderboard.json", "w") as f:
            json.dump(self.scores, f)

    def add_score(self, name, score):
        self.scores.append({"name": name, "score": score})
        self.scores.sort(key=lambda x: x["score"], reverse=True)
        self.scores = self.scores[:10]  # Keep only top 10
        self.save_scores()

    def show_leaderboard(self, page: ft.Page):
        def close_dialog(e):
            page.dialog.open = False
            page.update()

        leaderboard_items = [ft.DataRow(cells=[
            ft.DataCell(ft.Text(f"{i+1}", color=ft.colors.WHITE)),
            ft.DataCell(ft.Text(score["name"], color=ft.colors.WHITE)),
            ft.DataCell(ft.Text(str(score["score"]), color=ft.colors.WHITE))
        ]) for i, score in enumerate(self.scores)]

        dialog = ft.AlertDialog(
            title=ft.Text("Leaderboard", color=ft.colors.WHITE),
            content=ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Rank", color=ft.colors.WHITE)),
                    ft.DataColumn(ft.Text("Name", color=ft.colors.WHITE)),
                    ft.DataColumn(ft.Text("Score", color=ft.colors.WHITE)),
                ],
                rows=leaderboard_items
            ),
            actions=[ft.TextButton("Close", on_click=close_dialog, style=ft.ButtonStyle(color=ft.colors.WHITE))],
            bgcolor=ft.colors.BLUE_GREY_800,
        )

        page.dialog = dialog
        dialog.open = True
        page.update()

leaderboard = Leaderboard()