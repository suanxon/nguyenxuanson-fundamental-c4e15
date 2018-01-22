Color = ["red", "blue", "brown", "yellow", "grey"]

from turtle import*
shape("turtle")
speed(0)

for i in Color:

    color(i)
    begin_fill()

    for i in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    forward(50)
    end_fill()

mainloop()
