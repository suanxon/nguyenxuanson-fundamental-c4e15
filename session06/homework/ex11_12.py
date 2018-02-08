def in_inside(x, y):
    if x[0] >= y[0] and x[0] <= (y[0] + y[2]) and x[1] >= y[1] and x[1] <= (y[1] + y[3]):
        print(True)
    else:
        print(False)
in_inside([200, 120], [140, 60, 100, 200])
