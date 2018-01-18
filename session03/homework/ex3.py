print("Guess your numbergame")
print("Now think of a number from 0 to 100, then press 'Enter'")
print("All you have to do is to answer to my guess")
print("'c' if my guess is 'C'orrect")
print("'s' if my guess is 'S'maller tan your number")
print("'l' if my guess is 'Larger than your number'")
from random import randint
l = 100
s = 0
x = randint(s,l)

while True:
    n = input("Is " + str(x) + " your number?")
    if n == "c":
        print("I knew it")
        break
    elif n == "s":
        s = x + 1
        x = randint(s, l)
    elif n == "l":
        l = x - 1
        x = randint(s, l)
