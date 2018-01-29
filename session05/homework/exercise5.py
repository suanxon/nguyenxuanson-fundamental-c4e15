rabbits = {
    'truong thanh': 1,
    'moi lon': 0,
    'moi de': 0
}
x = rabbits['truong thanh']
y = rabbits['moi lon']
z = rabbits['moi de']

for i in range(5):
    if i == 0:
        x = x
        y = y
        z = z
    else:
        y = z
        z = x
        x = x + y

    m = x + z
    print("Month {0}: {1} pair(s) of rabbit".format(i,m))
