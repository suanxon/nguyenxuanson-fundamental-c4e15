menu = ['Thit cho', 'Thit meo', 'Com rang', 'Pho']
print("hi there, here you favorite thinsg so far")

for index, item in enumerate(menu):
    print("{0} . {1} ".format(index +1, item))

n = int(input("Loai mon nao?"))
menu.pop(n-1)
for index, item in enumerate(menu):
    print("{0} . {1} ".format(index +1, item))
n = input("Loai mon nao?")
menu.remove(n)
for index, item in enumerate(menu):
    print("{0} . {1} ".format(index +1, item))
