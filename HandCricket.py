#This code is developed by Sambhram Satapathy
"""In the code you provided, the following object-oriented programming (OOP) concepts are used:

->Classes and Objects: The code defines a class HandCricketGame, 
which encapsulates the behavior and state of a hand cricket game. 
The game object created in the main function is an instance of this class.

->Constructor (__init__): The __init__ method is used to initialize the state of the HandCricketGame object by 
setting attributes such as self.choice and self.balls.

->Methods: The code defines various methods within the HandCricketGame class, 
such as play, toss, start_innings, User_1st_batting, 
User_1st_bowling, Computer_1st_batting, and Computer_1st_bowling.
 These methods encapsulate the functionality of the game and are called to perform specific tasks.

->Encapsulation: The attributes self.choice and self.balls are 
encapsulated within the HandCricketGame class, making them private to the class.
 Access to these attributes is controlled through methods.

->Abstraction: The methods in the class provide a high-level abstraction
 of the game's functionality. Users of the class interact with these methods 
 without needing to know the low-level details of how the game is implemented.
"""
import mediapipe as mp
import random
import cv2

class HandCricketGame:
    def __init__(self):
        self.choice = None
        self.balls = None

    def play(self):
        print("Welcome to the Game of Hand Cricket")
        print("Let's Begin with the Toss\n")
        
        while True:
            try:
                toss_result = int(input("Enter the toss value 0 for odd or 1 for even: "))
                if toss_result not in [0, 1]:
                    raise ValueError("Input must be 0 or 1")
                break
            except ValueError as e:
                print(e)
        self.toss(toss_result)

    def toss(self, toss_result):
        T1 = random.randint(1, 6)
        T2 = random.randint(1, 6)
        toss_sum = T1 + T2
        if toss_sum % 2 == 0:
            if toss_result == 1:
                print("You Won the toss! Congratulations, it's Even")
                while True:
                    try:
                        self.choice = int(input("Enter your choice, to bat choose 1 or to ball choose 2: "))
                        if self.choice not in [1, 2]:
                            raise ValueError("Input must be 1 or 2")
                        break
                    except ValueError as e:
                        print(e)
            else:
                print("Oh No! You lost the toss, it's Even")
                self.choice = random.randint(3, 4)
        else:
            if toss_result == 0:
                print("You Won the toss! Congratulations, it's Odd")
                while True:
                    try:
                        self.choice = int(input("Enter your choice, to bat choose 1 or to ball choose 2: "))
                        if self.choice not in [1, 2]:
                            raise ValueError("Input must be 1 or 2")
                        break
                    except ValueError as e:
                        print(e)
            else:
                print("Oh No! You lost the toss, it's Odd")
                self.choice = random.randint(3, 4)
        self.balls = int(input("Enter the number of balls you want to play in the game: "))
        
        self.start_innings(self.balls)

    def start_innings(self, balls):
        print("It's the start of the First Innings!")
        print("\n")
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
            print("\n")
            comp_num = random.randint(1, 6)
            player_num = detect_finger_count()
            print(f"The computer chose {comp_num}")
            print(f"You chose {player_num}")
            print("\n")
            if player_num == comp_num:
                print("Oh you lost wicket\n")
                break
            else:
                total_score_p += player_num
        print(f"You scored {total_score_p}")
        total_score_p += 1
        print("Your gave the target to chase:", total_score_p)
        print("\n")
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
        print("\n")
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
        print("\n")
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

def main():
    game = HandCricketGame()
    game.play()

if __name__ == "__main__":
    main()