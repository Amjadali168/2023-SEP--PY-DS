from turtle import *

speed('fast')
for i in range(6):
    fd(100)
    rt(60)
    for i in range(6):
        fd(50)
        rt(60)
    #rt(60)

hideturtle()
mainloop()