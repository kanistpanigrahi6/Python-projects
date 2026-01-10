import random
rock= '''
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper=''' 
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)1
'''
game=[rock,paper,scissors]
print("RULES FOR THIS GAME :")
print("Rock crushes Scissors (Rock wins)")
print("Scissors cuts Paper (Scissors wins)")
print("Paper covers Rock (Paper wins))\n")

user=int(input("Which type of number u want ? type 0 for rock,1 for paper,2 for scissor\n"))
print("You choose:")
if user>=0 and user<=2:
    print(game[user])

computer=random.randint(0,2)
print("computer choose:")
print(game[computer])

if user>=3 and user<0:
    print("You typed an invalid number.you lose")
elif user==0 and computer ==2:
    print("You win")
elif computer==0 and user==2:
    print("you lose!")
elif computer > user:
    print("You lose!")
elif user > computer:
    print("you win")
elif user==computer:
    print("Its draw")

