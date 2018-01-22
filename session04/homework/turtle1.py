Color = ["red", "blue", "brown", "yellow", "grey"]
from turtle import*
shape("turtle")
speed(10)
l = len(Color)

for i in range(3, l+3):
    color(Color[i - 3])
    for j in range(i):
        forward(100)
        left(360/i)


mainloop()
