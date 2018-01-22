favs = ['death note', 'netflix', 'teaching']

print("Hi there, here you favorite things so far ")
print(*favs, sep = ", " )

new_fav = input("Name one thing your want to add?")
favs.append(new_fav)

print(*favs, sep = ", ")  #separator
