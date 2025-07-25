print("Welcome to the roller coster ")
Height=int(input("What is ur height in cm.?\n"))
bill=0
if Height >= 120:
    print("Allow to the rollercoster")
    age=int(input("Tell me ur age:\n"))
    if age<=12:
        bill=5
        print("child tickets should pay $5")
    elif age<=18:
        bill=7
        print("youth tickets should pay $7")
    elif age>=45 and age<=55:
        print("Everything is going to be ok .you can free ride")
    else:
        bill=12
        print("Adult tickets Shold pay $12")
    photo=input("Do u want a photo.. Tap y for YES and tap n for no")
    if photo == "y":
        bill+=3
    print(f"Total bill is ${bill}")
else:
    print("Doesn't allow to th rollercoster ")