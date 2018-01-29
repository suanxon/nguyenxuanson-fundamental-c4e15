numbers = [1, 6, 8, 1 ,2, 1, 5 ,6]
n = int(input("Enter a number?"))
dict_numbers = {}
for x in numbers:
    if x in dict_numbers:
        dict_numbers[x] += 1
    else:
        dict_numbers[x] = 1
# print(d)
for key, value in dict_numbers.items():
    if n == key:
        m = value
        print("{0} appears {1} times in my list".format(n, m))
        break
else:
    print("Not found")
