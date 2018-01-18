a = int(input("Row?"))
b = int(input("Column?"))

for i in range (a):
    if i % 2 == 0:
        for j in range(b):
            print("x * ", end = "")
    else:
        for j in range(b):
            print("* x ", end ="")

    print()
