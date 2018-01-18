y = int(input("number"))

x = y // 2
if y < 2:
    print(y, "is not a number prime")
while x > 1:
    if y % x == 0:
        print(y, "is not a number prime")
        break
    x -= 1
else:
        print(y, 'is a number prime')
