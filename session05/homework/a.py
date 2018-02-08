price = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3
}
stock = {
    "banana" : 0,
    "apple"  : 6,
    "orange" : 32,
    "pear"   :15
}
total = 0
Total = 0
for i in price:
    if i in stock:
        print(i)
        print("price :", price[i])
        print("stock:", stock[i])
        total = price[i] * stock[i]
        print(total)
        Total += price[i] * stock[i]
print("Total = ", Total)
