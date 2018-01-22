Shop = ["T-Shirt", "Sweater"]
while True:
    n = input("Welcome to our shop, what do you want(C, R, U, D)?")
    if n == "R":
        print("Our items:", end = " ")
        print(*Shop, sep = ", ")

    elif n == "C":
        new_item = input("Enter new item:")
        Shop.append(new_item)
        print("Our items:", end = " ")
        print(*Shop, sep = ", ")

    elif n == "U":
        x = int(input("Update position?"))
        if x <= len(Shop):
            new = input("New item?")
            Shop[x - 1] = new
            print("Our items:", end = " ")
            print(*Shop, sep = ", ")
        else:
            print("Item slot is emty")

    elif n == "D":
        y = int(input("Delete position?"))
        if y <= len(Shop):
            Shop.pop(y-1)
            print("Our items:", end = " ")
            print(*Shop, sep = ", ")
        else:
            print("Item slot is emty")
    else:
        break
