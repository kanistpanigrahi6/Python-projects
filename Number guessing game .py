import random
from ascii import ascii_art
print(ascii_art)
rand=random.randint(1,100)
print(rand)
print("Welcome to the number guessing game")
print("Im a thinking of a number b/w 1 to 100")
difficulty=input("Choose a difficulty .Type 'Easy' or 'Hard'\n").lower()



def easy_level():
    while True:
        if difficulty =="easy":
            print("you have 10 attempts to remaining to guess the number.")
            for i in range(1,11):
                attempts_easy=10-i+1
                guess = int(input(f"Make a guess  u have {attempts_easy} attempts remaining :"))
                if guess < rand :
                    print("Too low !!")
                elif guess >rand:
                    print("Too high !!")
                else:
                    print(f"The guessing number was{rand} out of {i} times :")
                    break
            else:
                print("Game over no more chances..")

            break
        elif difficulty=="hard":
            print("you have 3 attempts to remaining to guess the number.")
            for i in range(1, 4):
                attempts_hard = 3 - i + 1
                guess_hard = int(input(f"Make a guess  u have {attempts_hard} attempts remaining: "))
                if guess_hard < rand:
                    print("Too low !!")
                elif guess_hard > rand:
                    print("Too high !!")
                else:
                    print(f"The guessing number was {rand} out of {i} times:")
                    break
            else:
                print("Game over no more chances..")

            break
easy_level()
#                                                    

                                                                #########################################
                                                                #                                       #
                                                                #         GUESS THE NUMBER GAME         #
                                                                #                                       #
                                                                #########################################
                                                                #                                       #
                                                                #   Welcome to the ultimate challenge!  #
                                                                #   Think of a number and make a guess! #
                                                                #   Will you be the champion today?     #
                                                                #                                       #
                                                                #########################################
                                                                             #  _______
                                                                             # |       |
                                                                             # | THINK |
                                                                             # |_______|
                                                                             #     ||










