from random import randint
x = randint(1,100)

count = 0


while count < 7:
    n = int(input("Numer?"))
    if n > x:
        print("Big")
    elif n < x:
        print("Small")
    else:
        print("Bingo")
        break
    count += 1
