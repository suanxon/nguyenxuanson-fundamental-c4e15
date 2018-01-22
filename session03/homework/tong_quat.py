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
        s = x
        x = (s + l) //2
    elif n == "l":
        l = x
        x = ( s + l) //2
