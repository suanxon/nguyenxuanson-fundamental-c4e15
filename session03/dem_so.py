n = int(input("Enter a number:"))

count = 0
while count <100:
    if n < 10**count and n >= 10**(count - 1):
        print(count)
        break
    count += 1
