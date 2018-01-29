number = [7, 5, 10, 8, 200, 30]
n = int(input("Enter a number:"))

if n in number:     # 1 for
    print("Found")
    found_index = number.index(n)
    print("Index: ", found_index)
else:
    print("Not found")
