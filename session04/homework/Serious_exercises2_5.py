sheep = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hiep and these are my sheep sizes:")
print(sheep)
for i in range(3):
    print("MONTH {0}".format(i+1))
    print("One month has passed, now here is my flock")
    for i in range(7):
        x = sheep[i]
        sheep[i] = x + 50
    print(sheep)

    biggest = max(sheep)
    print("Now my biggest sheep has size {0} let's shear it".format(biggest))

    print("After shearing, here is my flock")
    sheep[sheep.index(max(sheep))] = 8
    print(sheep)
    print()
