# import random
# import flet as ft
# import HandCricket

# def main(page: ft.Page):
#     page.title = "Hand Cricket Game"

#     def toss_odd(e):
#         toss(0)

#     def toss_even(e):
#         toss(1)

#     def toss(toss_choice):
#         nonlocal choice, balls, result_text, choice_buttons, start_text
#         T1 = random.randint(1, 6)
#         T2 = random.randint(1, 6)
#         toss_sum = T1 + T2
#         is_even = toss_sum % 2 == 0
#         user_wins = (is_even and toss_choice == 1) or (not is_even and toss_choice == 0)

#         if user_wins:
#             result_text.value = f"You won the toss! It was {'Even' if is_even else 'Odd'}."
#             choice_buttons.visible = True
#         else:
#             choice = random.choice([1, 2])
#             result_text.value = f"You lost the toss. It was {'Even' if is_even else 'Odd'}."
#             result_text.value += f"\nComputer chose to {'Bat' if choice == 1 else 'Ball'} first."
#             balls = get_balls()
#             start_innings(balls)
        
#         page.update()

#     def choose_bat(e):
#         nonlocal choice, balls
#         choice = 1
#         balls = get_balls()
#         start_innings(balls)

#     def choose_ball(e):
#         nonlocal choice, balls
#         choice = 2
#         balls = get_balls()
#         start_innings(balls)

#     def get_balls():
#         # For simplicity, let's assume a fixed number of balls
#         return 6

#     def start_innings(balls):
#         nonlocal result_text, start_text
#         start_text.value = f"The game will be played for {balls} balls. Let the game begin!"
#         page.update()
    
#     def lets_play():
#         HandCricket

#     choice = None
#     balls = None

#     intro_text = ft.Text("Welcome to the Game of Hand Cricket", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
#     toss_instruction = ft.Text("Let's Begin with the Toss", size=20, text_align=ft.TextAlign.CENTER)
#     toss_buttons = ft.Container(
#         content=ft.Row([
#             ft.ElevatedButton("Odd", on_click=toss_odd, width=150, height=50),
#             ft.ElevatedButton("Even", on_click=toss_even, width=150, height=50)
#         ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
#         padding=ft.padding.only(top=20)
#     )
#     result_text = ft.Text("", size=18, color=ft.colors.BLUE, text_align=ft.TextAlign.CENTER)
#     choice_buttons = ft.Container(
#         content=ft.Row([
#             ft.ElevatedButton("Bat", on_click=choose_bat, width=150, height=50),
#             ft.ElevatedButton("Ball", on_click=choose_ball, width=150, height=50)
#         ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
#         padding=ft.padding.only(top=20),
#         visible=False
#     )
#     start_text = ft.Text("", size=18, color=ft.colors.GREEN, text_align=ft.TextAlign.CENTER)

#     letsplay_buttons = ft.Container(
#         content=ft.Row([
#             ft.ElevatedButton("Lets Play", on_click=lets_play, width=150, height=50)
#         ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
#         padding=ft.padding.only(top=20)
#     )

#     page.add(
#         ft.Container(
#             content=ft.Column([
#                 intro_text,
#                 toss_instruction,
#                 toss_buttons,
#                 result_text,
#                 choice_buttons,
#                 start_text,
#                 letsplay_buttons
#             ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
#             padding=ft.padding.all(20)
#         )
#     )

# ft.app(target=main)


import random
import flet as ft
import subprocess

def main(page: ft.Page):
    page.title = "Hand Cricket Game"

    def toss_odd(e):
        toss(0)

    def toss_even(e):
        toss(1)

    def toss(toss_choice):
        nonlocal choice, balls, result_text, choice_buttons, start_text, letsplay_button
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
            letsplay_button.visible = True
        
        page.update()

    def choose_bat(e):
        nonlocal choice, balls, letsplay_button
        choice = 1
        balls = get_balls()
        letsplay_button.visible = True
        page.update()

    def choose_ball(e):
        nonlocal choice, balls, letsplay_button
        choice = 2
        balls = get_balls()
        letsplay_button.visible = True
        page.update()

    def get_balls():
        # For simplicity, let's assume a fixed number of balls
        return 6

    def start_game(e):
        # Assuming HandCricket.py is in the same directory
        print("The Game Started")
        subprocess.run(["python", "HandCricket.py", str(choice), str(balls)])

    choice = None
    balls = None

    intro_text = ft.Text("Welcome to the Game of Hand Cricket", size=30, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER)
    toss_instruction = ft.Text("Let's Begin with the Toss", size=20, text_align=ft.TextAlign.CENTER)
    toss_buttons = ft.Container(
        content=ft.Row([
            ft.ElevatedButton("Odd", on_click=toss_odd, width=150, height=50),
            ft.ElevatedButton("Even", on_click=toss_even, width=150, height=50)
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
        padding=ft.padding.only(top=20)
    )
    result_text = ft.Text("", size=18, color=ft.colors.BLUE, text_align=ft.TextAlign.CENTER)
    choice_buttons = ft.Container(
        content=ft.Row([
            ft.ElevatedButton("Bat", on_click=choose_bat, width=150, height=50),
            ft.ElevatedButton("Ball", on_click=choose_ball, width=150, height=50)
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
        padding=ft.padding.only(top=20),
        visible=False
    )
    start_text = ft.Text("", size=18, color=ft.colors.GREEN, text_align=ft.TextAlign.CENTER)

    letsplay_button = ft.Container(
        content=ft.ElevatedButton("Let's Play", on_click=start_game, width=150, height=50),
        padding=ft.padding.only(top=20),
        visible=False
    )

    page.add(
        ft.Container(
            content=ft.Column([
                intro_text,
                toss_instruction,
                toss_buttons,
                result_text,
                choice_buttons,
                start_text,
                letsplay_button
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
            padding=ft.padding.all(20)
        )
    )

ft.app(target=main)
