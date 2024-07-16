import random
import flet as ft
import subprocess
import keyboard
from theme import apply_theme, TITLE_STYLE, BODY_STYLE
from settings import game_settings

# Updated button style
BUTTON_STYLE = ft.ButtonStyle(
    color=ft.colors.WHITE,
    bgcolor=ft.colors.BLUE_GREY_800,
    padding=10,
    shape=ft.RoundedRectangleBorder(radius=10),
)

def main(page: ft.Page):
    page.window.maximized = True
    page.title = "Hand Cricket Game"
    
    # Apply a darker theme
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.theme = ft.Theme(color_scheme=ft.ColorScheme(
        primary=ft.colors.BLUE_400,
        primary_container=ft.colors.BLUE_900,
        secondary=ft.colors.TEAL_400,
        background=ft.colors.BLUE_GREY_900,
    ))

    choice = None
    balls = None

    def toss(toss_choice):
        nonlocal choice, balls
        T1 = random.randint(1, 6)
        T2 = random.randint(1, 6)
        toss_sum = T1 + T2
        is_even = toss_sum % 2 == 0
        user_wins = (is_even and toss_choice == 1) or (not is_even and toss_choice == 0)

        if user_wins:
            result_text.value = f"You won the toss! It was {'Even' if is_even else 'Odd'}."
            choice_buttons.visible = True
        else:
            choice = random.choice([1, 2])
            result_text.value = f"You lost the toss. It was {'Even' if is_even else 'Odd'}."
            result_text.value += f"\nComputer chose to {'Bat' if choice == 1 else 'Ball'} first."
            balls = get_balls()
            choice_buttons.visible = False
            letsplay_button.visible = True
        
        page.update()

    def toss_odd(e):
        toss(0)

    def toss_even(e):
        toss(1)

    def choose_bat(e):
        nonlocal choice, balls
        choice = 1
        balls = get_balls()
        letsplay_button.visible = True
        page.update()

    def choose_ball(e):
        nonlocal choice, balls
        choice = 2
        balls = get_balls()
        letsplay_button.visible = True
        page.update()

    def get_balls():
        return game_settings.overs * 6

    def start_game(e):
        page.window.maximized = True
        subprocess.Popen(["python", "HandCricket.py", str(choice), str(balls)])
        page.window_destroy()

    def on_enter(e):
        keyboard.press_and_release("enter")

    intro_text = ft.Text("Welcome to the Game of Hand Cricket", style=TITLE_STYLE, color=ft.colors.WHITE)
    toss_instruction = ft.Text("Let's Begin with the Toss", style=BODY_STYLE, color=ft.colors.WHITE70)
    toss_buttons = ft.Container(
        content=ft.Row([
            ft.ElevatedButton("Odd", on_click=toss_odd, width=150, height=50, style=BUTTON_STYLE),
            ft.ElevatedButton("Even", on_click=toss_even, width=150, height=50, style=BUTTON_STYLE)
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
        padding=ft.padding.only(top=20)
    )
    result_text = ft.Text("", style=BODY_STYLE, color=ft.colors.BLUE_200, text_align=ft.TextAlign.CENTER)
    choice_buttons = ft.Container(
        content=ft.Row([
            ft.ElevatedButton("Bat", on_click=choose_bat, width=150, height=50, style=BUTTON_STYLE),
            ft.ElevatedButton("Ball", on_click=choose_ball, width=150, height=50, style=BUTTON_STYLE)
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
        padding=ft.padding.only(top=20),
        visible=False
    )
    letsplay_button = ft.Container(
        content=ft.ElevatedButton("Let's Play", on_click=start_game, width=150, height=50, style=BUTTON_STYLE),
        padding=ft.padding.only(top=20),
        visible=False
    )

    content = ft.Column([
        intro_text,
        toss_instruction,
        toss_buttons,
        result_text,
        choice_buttons,
        letsplay_button
    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)

    page.add(ft.Container(content=content, padding=ft.padding.all(20)))

ft.app(target=main)