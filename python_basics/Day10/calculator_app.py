import art
import os

def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return  n1 - n2
def multiply(n1,n2):
    return  n1 * n2
def divide(n1,n2):
    return  round((n1 / n2),2)
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
    }
def calculator():
    print(art.logo)
    n1 = float(input("What is the first number?: "))
    result = 0
    cont_calc = True
    while cont_calc:
        for symbol in operations:
            print(symbol)
        select_opers = input("Pick an Operation from above: ")
        n2 = float(input("What is the other number?: "))
        result =  operations[select_opers](n1,n2)
        cont_req = input(f"Type 'y' to continue calculating with {n1} {select_opers} {n2} = {result}, or type 'n' to start a new calculation: ").lower()
        
        if cont_req == "y":
            n1 = result
        else:
            cont_calc = False
            os.system('cls')
            calculator()
calculator()


    