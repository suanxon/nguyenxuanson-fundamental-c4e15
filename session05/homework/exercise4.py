
n = int(input("How many B bacterias?"))
m = int(input("How much time in minutes will we wait?"))

x = m//2
y = n * (2)**x
print("After {0} minutes, we would have {1} bacterias".format(m,y))
