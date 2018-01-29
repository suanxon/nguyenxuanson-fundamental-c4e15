#person = ["Tuan anh", 22, 2, "Hanoi", "Moc chau", 5, 4, "Maria", "Ping pong"]

# person = {}
# print(person)

person = {
    #key  : value
    "name" : "Tuan Anh",
    "age" : 22,
    "sex" : "male"
}
#print(person)
if 'age2' in person:
    print(person['age2'])
# chi hien values:
for v in person.values():
    print(v)
#chi hien key:
for k in person:
    print(k)
#hien ca 2:
for key, value in person.items():
    print(key, value)
#update va creat nhu nhau:
person['age'] = 23 # viet +=1 cung duoc
