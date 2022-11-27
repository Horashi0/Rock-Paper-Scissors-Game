import random
import math
import time
bot_score = []
user_score = []
choice = int(
    input("Welcome to my rock paper scissors game. How many rounds do you want? "))
time.sleep(0.8)
rounds = (choice / 2) + 1
round_up = math.floor(rounds)
print("You need to win", round_up, "rounds to win the game ")
time.sleep(0.8)


def main():
    bot_score = []
    user_score = []
    loopkiller = False
    while loopkiller == False:
        user_input = int(input("Choose Rock(1) Paper(2) or Scissors(3) "))
        time.sleep(0.8)
        number = random.randint(1, 3)

        if user_input > 3:
            print("Invalid input. Please try again ")
            main()

        user_score_calculated = sum(user_score)
        bot_score_calculated = sum(bot_score)

        if number == 1 and user_input == 1:
            print("Haha you both chose rock. Please try again! ")
            user_score_calculated = sum(user_score)
            bot_score_calculated = sum(bot_score)
            time.sleep(0.8)
            print(
                f"The score is: Bot:{bot_score_calculated}, User:{user_score_calculated}")
            time.sleep(0.8)

        if number == 1 and user_input == 2:
            print("Nice! The bot chose rock! ")
            time.sleep(0.8)
            user_score.append(+1)
            print("+1 to user score ")
            user_score_calculated = sum(user_score)
            bot_score_calculated = sum(bot_score)
            time.sleep(0.8)
            print(
                f"The score is: Bot:{bot_score_calculated}, User:{user_score_calculated}")
            time.sleep(0.8)

        if number == 1 and user_input == 3:
            print("Oh no, the bot chose rock! ")
            time.sleep(0.8)
            bot_score.append(1)
            print("+1 to bot score ")
            user_score_calculated = sum(user_score)
            bot_score_calculated = sum(bot_score)
            time.sleep(0.8)
            print(
                f"The score is: Bot:{bot_score_calculated}, User:{user_score_calculated}")
            time.sleep(0.8)

        if number == 2 and user_input == 1:
            print("Oh no, the bot chose paper! ")
            time.sleep(0.8)
            bot_score.append(1)
            print("+1 to bot score ")
            user_score_calculated = sum(user_score)
            bot_score_calculated = sum(bot_score)
            time.sleep(0.8)
            print(
                f"The score is: Bot:{bot_score_calculated}, User:{user_score_calculated}")
            time.sleep(0.8)

        if number == 2 and user_input == 2:
            print("Haha you both chose paper. Please try again!")
            user_score_calculated = sum(user_score)
            bot_score_calculated = sum(bot_score)
            time.sleep(0.8)
            print(
                f"The score is: Bot:{bot_score_calculated}, User:{user_score_calculated}")
            time.sleep(0.8)

        if number == 2 and user_input == 3:
            print("Nice! the bot chose paper! ")
            time.sleep(0.8)
            user_score.append(+1)
            print("+1 to user score ")
            user_score_calculated = sum(user_score)
            bot_score_calculated = sum(bot_score)
            time.sleep(0.8)
            print(
                f"The score is: Bot:{bot_score_calculated}, User:{user_score_calculated}")
            time.sleep(0.8)

        if number == 3 and user_input == 1:
            print("Nice! The bot chose scissors! ")
            time.sleep(0.8)
            user_score.append(+1)
            print("+1 to user score ")
            user_score_calculated = sum(user_score)
            bot_score_calculated = sum(bot_score)
            time.sleep(0.8)
            print(
                f"The score is: Bot:{bot_score_calculated}, User:{user_score_calculated}")
            time.sleep(0.8)

        if number == 3 and user_input == 2:
            print("Oh no, the bot chose scissors!")
            time.sleep(0.8)
            bot_score.append(+1)
            print("+1 to bot score")
            user_score_calculated = sum(user_score)
            bot_score_calculated = sum(bot_score)
            time.sleep(0.8)
            print(
                f"The score is: Bot:{bot_score_calculated}, User:{user_score_calculated}")
            time.sleep(0.8)

        if number == 3 and user_input == 3:
            print("Haha you both chose scissors. Please try again!")
            user_score_calculated = sum(user_score)
            bot_score_calculated = sum(bot_score)
            time.sleep(0.8)
            print(
                f"The score is: Bot:{bot_score_calculated}, User:{user_score_calculated}")
            time.sleep(0.8)

        user_score_calculated = sum(user_score)
        bot_score_calculated = sum(bot_score)

        if round_up == user_score_calculated:
            print("Well done! You won! ")

            loopkiller = True

        if round_up == bot_score_calculated:
            print("Oh no! The bot beat you. Better luck next time! ")
            loopkiller = True


main()
