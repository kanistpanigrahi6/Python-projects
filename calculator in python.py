def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
def calculator():
    print('''
                                                                             _____________________
                                                                            |  _________________  |
                                                                            | |              0. | |
                                                                            | |_________________| |
                                                                            |  ___ ___ ___   ___  |
                                                                            | | 7 | 8 | 9 | | + | |
                                                                            | |___|___|___| |___| |
                                                                            | | 4 | 5 | 6 | | - | |
                                                                            | |___|___|___| |___| |
                                                                            | | 1 | 2 | 3 | | x | |
                                                                            | |___|___|___| |___| |
                                                                            | | . | 0 | = | | ÷ | |
                                                                            | |___|___|___| |___| |
                                                                            |_____________________|
    ''')
    should_continue=True
    num1=float(input("What is the first number:"))
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol=input("Pick an operation:")
        num2=float(input("What is the next number:"))
        result=operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        repeat=input(f"Type 'Y  to continue the calcuating with {result} or type 'N").lower()
        if repeat=="y":
            num1=result
        else:
            should_continue=False
            print("\n"*20)
            calculator()
calculator()
