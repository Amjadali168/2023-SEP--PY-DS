from turtle import *

data = [2,3,4,5,6,7,8,9,9,10,11,12,90]

for val in data:
    fd(val)
    lt(360/6)
    # write(val)

    # fd(val)
    # lt(360/6)
    # circle(val, 180)

hideturtle()
mainloop()