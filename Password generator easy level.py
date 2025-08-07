import random
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!',',','-','_','+','=','@','#','$','%','^','&','*']
print("Welcome to the password generator")
letters_type=int(input("How many letters would u like in your password\n"))
numbers_type=int(input("How many numbers would u like in your password\n"))
symbols_type=int(input("How many symbols would u like in your password\n"))
password=""
for rand in range(0,letters_type):
    password=password+random.choice(letters)
for rand in range(0, numbers_type):
    password = password + random.choice(numbers)
for rand in range(0, symbols_type):
    password = password + random.choice(symbols)
print(password)






