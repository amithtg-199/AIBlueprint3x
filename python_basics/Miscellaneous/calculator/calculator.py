import logo
import os

def add(num1,num2): return num1+num2
def subtract(num1,num2): return num1-num2
def multiply(num1,num2): return num1*num2
def divide(num1,num2): return num1/num2

operations={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

operands=['+','-','*','/']

def calculator():
    print(logo.logo)
    num1=float(input("What's the first number?: "))

    is_continue=True
    while is_continue is True:
        for i in operations:
            print(i)
        oper_actions=input("Pick an operation: ")
        while oper_actions not in operands:
            oper_actions=input("Kindly chose above mentioned operations only: ")
        num2=float(input("What's the next number?: "))
        while oper_actions =="/" and num2==0:
            print("you cannot divide a number with 0")
            num2=float(input("Kindly re enter a proper value again!: "))
        calculated_output=operations[oper_actions]
        result=round(calculated_output(num1,num2),2)
        print(f"{num1} {oper_actions} {num2} = {result}")
        action=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        while action not in ["y","n"]:
            action=input("Kindly input only 'y' or 'n': ")
        if action=="y":
            num1=result
        else:
            is_continue=False
            os.system('cls')
            calculator()

calculator()


