from random import *

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(1, 100)
    y = randint(1, 100)
    op = choice(["+", "-", "*", "/"])
    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == '*':
        result = x * y
    elif op == "/":
        result = x / y
    error = randint(-1, 5)
    display_result = result + error
    return [x, y, op, display_result]
def check_answer(x, y, op, dispay_result, user_choice):
    if dispay_result == x + y and user_choice == True or dispay_result != x + y and user_choice == False:
        return True
    else:
        return False
