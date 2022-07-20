"""This is a calculator program"""
# add
def add(n1,n2): return n1 + n2
 #subtract
def subtract(n1,n2):
    return n1-n2
 #mutliply
def multiply(n1,n2):
    return n1*n2
 #divide
def divide(n1,n2):
    return n1/n2
operations = {"+": add,"-":subtract,"*":multiply,"/":divide}
def calculator():
    num1 = float(input("What is the first number?: "))
    for symbols in operations:
        print(symbols)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the second number?: "))
        calculate = operations[operation_symbol]
        answer = calculate(num1,num2)
        print(f" {num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculation with {answer}, or type'n' to start new calculation") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()