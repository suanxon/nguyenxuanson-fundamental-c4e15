print("Guess your numbergame")
print("Now think of a number from 0 to 100, then press 'Enter'")
print("All you have to do is to answer to my guess")
print("'c' if my guess is 'C'orrect")
print("'s' if my guess is 'S'maller tan your number")
print("'l' if my guess is 'Larger than your number'")
from random import randint
hi = 100
lo = 0

loop = True
while loop:
    mid = (lo + hi) // 2
    answer = input("Is {0} your number?".format(mid))
    if answer.lower() == 'c':
        print("I knew it")
        loop = False
    elif answer.lower() == 's':
        hi = mid
    elif answer.lower() == 'l':
        lo = mid
