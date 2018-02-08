from random import randint
from random import choice
from cal import eval
x = randint(0, 10)
y = randint(0, 10)
error = randint(-1, 1)
List = ["+", "+", "+", "+", "+", "+", "+", "-", "-", "-", "-", "-", "*", "*", "*", "/"]
op = choice(List)
display_result = eval(x, y, op) + error


print ("{0} {1} {2} = {3}".format(x, op, y, display_result))

answer = input("(Y/N)?").upper()
KQ = 0
if error == 0:
    if answer == "Y":
        KQ = "Yay"
    elif answer == "N":
        KQ = "You're wrong"
else:
    if answer == "N":
        KQ = "Yay"
    elif answer == "Y":
        KQ = "You're wrong"

print(KQ)
