print("Hi there, here you favorite things so far")
print("*" * 60)
favs =['death note', 'netflix', 'teaching']
print (*favs, sep = ", ")

print("*" * 60)

# position = 1
# for item in favs:
#
#     #print(position, ".", item)
#     print("{0}.{1}".format(position, item))
#     position += 1

# for index, fav in enumerate(favs):   # may tu hieu index la stt va fav la item trong list
#     print("{0}- {1}".format(index + 1, fav))

print(*enumerate(favs))   # dau * buoc phai hien het phan tu
