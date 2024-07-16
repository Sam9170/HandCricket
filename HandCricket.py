import mediapipe as mp
import random
import cv2
import sys
import flet as ft
import io
from theme import apply_theme, TITLE_STYLE, BODY_STYLE

# Updated button style
BUTTON_STYLE = ft.ButtonStyle(
    color=ft.colors.WHITE,
    bgcolor=ft.colors.BLUE_GREY_800,
    padding=10,
    shape=ft.RoundedRectangleBorder(radius=10),
)

class HandCricketGame:
    def __init__(self, choice, balls):
        self.choice = choice
        self.balls = balls

    def start_game(self):
        self.start_innings(self.balls)

    def start_innings(self, balls):
        print("It's the start of the First Innings!")
        print(f"The game will be played for {self.balls} balls. Let the Game begin")
        print("\n")

        if self.choice == 1:
            self.User_1st_batting(balls)
        elif self.choice == 2:
            self.User_1st_bowling(balls)
        elif self.choice == 3:
            self.Computer_1st_batting(balls)
        else:
            self.Computer_1st_bowling(balls)

    def User_1st_batting(self, balls):
        total_score_c = 0
        total_score_p = 0
        print("You are batting first")
        for i in range(balls):
            print(f"This is the {i} ball")
            comp_num = random.randint(1, 6)
            player_num = detect_finger_count()
            print(f"The computer chose {comp_num}")
            print(f"You chose {player_num}")
            if player_num == comp_num:
                print("Oh you lost wicket\n")
                break
            else:
                total_score_p += player_num
        print(f"You scored {total_score_p}")
        total_score_p += 1
        print("Your gave the target to chase:", total_score_p)
        print("Welcome to the second Innings\n")

        for i in range(balls):
            print(f"This is the {i} ball")
            comp_num = random.randint(1, 6)
            player_num = detect_finger_count()
            print(f"The computer chose {comp_num}")
            print(f"The player chose {player_num}")

            if player_num == comp_num:
                if total_score_c < total_score_p:
                    print("He is out")
                    print("You won the match\n")
                    break
            else:
                total_score_c += comp_num
                if total_score_c >= total_score_p:
                    print("You lost the match")
                    break
        print("The total score of computer is:", total_score_c)

    def User_1st_bowling(self, balls):
        total_score_c = 0
        print("You are bowling first\n")
        for i in range(balls):
            print(f"This the {i} ball\n")
            comp_num = random.randint(1, 6)
            player_num = detect_finger_count()
            print(f"The computer chose {comp_num}")
            print(f"You chose {player_num}")
            if player_num == comp_num:
                print("Yes! You got his wicket")
                break
            else:
                total_score_c += comp_num
        print(f"Computer has scored {total_score_c}")
        total_score_c += 1
        print("Your target to chase is:", total_score_c)
        print("Welcome to the second Innings\n")
        total_score_p = 0
        for i in range(balls):
            print(f"This the {i} ball")
            comp_num = random.randint(1, 6)
            player_num = detect_finger_count()
            print(f"The computer chose {comp_num}")
            print(f"You chose {player_num}")

            if player_num == comp_num:
                if total_score_p < total_score_c:
                    print("You are out")
                    print("You lost the match\n")
                    break
            else:
                total_score_p += player_num
                if total_score_p >= total_score_c:
                    print("You won the match\n")
                    break
        print("Your total is:", total_score_p)

    def Computer_1st_batting(self, balls):
        print("Computer is batting")
        total_score_c = 0
        for i in range(balls):
            print(f"This the {i} ball\n")
            comp_num = random.randint(1, 6)
            player_num = detect_finger_count()
            print(f"The computer chose {comp_num}")
            print(f"You chose {player_num}")
            if player_num == comp_num:
                print("Yes! You got his wicket")
                break
            else:
                total_score_c += comp_num
        print(f"Computer has scored {total_score_c}")
        total_score_c += 1
        print("Your target to chase is:", total_score_c)
        print("Welcome to the second Innings")
        total_score_p = 0
        for i in range(balls):
            print(f"This the {i} ball\n")
            comp_num = random.randint(1, 6)
            player_num = detect_finger_count()
            print(f"The computer chose {comp_num}")
            print(f"You scored {player_num}")

            if player_num == comp_num:
                if total_score_p < total_score_c:
                    print("You are out")
                    print("You lost the match\n")
                    break
            else:
                total_score_p += player_num
                if total_score_p >= total_score_c:
                    print("You won the match")
                    break
        print("Your total is:", total_score_p)

    def Computer_1st_bowling(self, balls):
        print("Computer is bowling")
        total_score_p = 0
        total_score_c = 0
        for i in range(balls):
            print(f"This the {i} ball\n")
            comp_num = random.randint(1, 6)
            player_num = detect_finger_count()
            print(f"The computer chose {comp_num}")
            print(f"You chose {player_num}")
            if player_num == comp_num:
                print("Oh no you lost your wicket\n")
                break
            else:
                total_score_p += player_num
        print(f"You scored {total_score_p}")
        total_score_p += 1
        print("Your gave target to chase:", total_score_p)
        print("Welcome to the second Innings\n")
        for i in range(balls):
            print(f"This the {i} ball\n")
            comp_num = random.randint(1, 6)
            player_num = detect_finger_count()
            print(f"The computer chose {comp_num}")
            print(f"You chose {player_num}")

            if player_num == comp_num:
                if total_score_c < total_score_p:
                    print("He is out")
                    print("You won the match\n")
                    break
            else:
                total_score_c += comp_num
                if total_score_c >= total_score_p:
                    print("You lost the match")
                    break
        print("The total score of computer is:", total_score_c)


def detect_finger_count():
    cap = cv2.VideoCapture(0)
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1)
    mp_drawing = mp.solutions.drawing_utils

    finger_count = 0
    while True:
        success, image = cap.read()
        if not success:
            continue

        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                finger_count = count_fingers(image, results.multi_hand_landmarks)
                cv2.putText(image, f'Fingers: {finger_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                cv2.imshow('MediaPipe Hands', image)
                if cv2.waitKey(5) & 0xFF == 13:  # Press Enter to confirm the number of fingers shown
                    cap.release()
                    cv2.destroyAllWindows()
                    hands.close()
                    return finger_count

        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(5) & 0xFF == 27:  # Press ESC to exit the detection loop
            break

    cap.release()
    cv2.destroyAllWindows()
    hands.close()
    return finger_count

def count_fingers(image, hand_landmarks):
    tips_ids = [4, 8, 12, 16, 20]
    if hand_landmarks:
        landmarks = hand_landmarks[0].landmark
        fingers = []

        if landmarks[tips_ids[0]].x < landmarks[tips_ids[0] - 1].x:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
            if landmarks[tips_ids[id]].y < landmarks[tips_ids[id] - 2].y:
                fingers.append(1)
            else:
                fingers.append(0)

        total_fingers = fingers.count(1)
        if fingers[0] == 1 and total_fingers == 1:
            return 6
        return total_fingers

    return 0

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

    choice = int(sys.argv[1])
    balls = int(sys.argv[2])
    game = HandCricketGame(choice, balls)

    output_text = ft.Text("", style=BODY_STYLE, color=ft.colors.WHITE70, text_align=ft.TextAlign.LEFT)
    
    def update_output(text):
        output_text.value += text
        page.update()

    # Custom stream to redirect stdout
    class StdoutRedirect(io.StringIO):
        def write(self, text):
            update_output(text)

    stdout_redirect = StdoutRedirect()
    sys.stdout = stdout_redirect

    def start_game_thread(e):
        start_button.visible = False
        page.update()
        game.start_game()
        start_button.visible = True
        page.update()

    start_button = ft.ElevatedButton("Start Game", on_click=start_game_thread, style=BUTTON_STYLE)

    output_list = ft.ListView(
        [output_text],
        expand=1,
        auto_scroll=True
    )

    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("Hand Cricket Game", style=TITLE_STYLE, color=ft.colors.WHITE),
                ft.Container(
                    content=output_list,
                    padding=10,
                    bgcolor=ft.colors.BLUE_GREY_800,
                    border_radius=10,
                    expand=True,
                    height=400,
                    width=600,
                ),
                start_button
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20),
            padding=20,
            alignment=ft.alignment.center,
            expand=True,
        )
    )

    # Restore stdout when the page is dismounted
    page.on_disconnect = lambda _: setattr(sys, 'stdout', sys.__stdout__)

if __name__ == "__main__":
    ft.app(target=main)