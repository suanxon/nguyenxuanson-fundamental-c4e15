import random
champion = list("champion")
hexagon = list("hexagon")
bitcoin = list("bitcoin")
word = [champion, hexagon, bitcoin]

i = random.randint(0, len(word) -1)
n = word[i]
random.shuffle(n)
print(*n, end= " ")
print()
x = input("Your answer:")
if i == 0:
    if x == "champion":
        print("Hura")
    else:
        print(":(")
elif i == 1:
    if x == "hexagon":
        print("Hura")
    else:
        print(":(")
else:
    if x == "bitcoin":
        print("Hura")
    else:
        print(":(")
