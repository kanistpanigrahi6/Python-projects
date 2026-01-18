print("WELCOME TO THE PIZZA ORDER")
size=input("type the size u want. s for small,m for medium and l for large \n")
pepperoni=input("If u want to pepperoni type y for yes and n for no \n")
extra_cheese=input("Do u want extra cheese type y for yes and n for no \n")
bill=0
if size=="s":
    bill += 15
elif size == "m":
    bill+=20
elif size=="l":
    bill+=25
else:
    print("u type the wrong key")
if pepperoni=="y":
    if size=="s":
        bill+=2
    else:
        bill+=3
if extra_cheese=="y":
    bill+=1
print(f"total bill is ${bill} ")
