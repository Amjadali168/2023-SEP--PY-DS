from turtle import *

# make square
# fd(100)
# lt(90)
# fd(100)
# lt(90)
# fd(100)
# lt(90)
# fd(100)
# lt(90)
# hideturtle()
# mainloop()

# using range fuction we can also make this square
# for i in range(4):
#     fd(100)
#     lt(90)
# hideturtle()
# mainloop()


# pentagon

# speed('slowest')
# for i in range(5):
#     fd(100) 
#     lt(360/5)

# hideturtle()
# mainloop()


# to draw stair like structure
speed('fastest')
penup()
goto(-200,-200)
pendown()
for i in range(15):
    fd(20)
    lt(90)
    fd(20)
    rt(90)
hideturtle()
mainloop()