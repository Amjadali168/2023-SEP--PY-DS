from turtle import *

dis = [100, 200, 150, 50, 120]
ng1 = [90, 72, 144, 36, 60]

# dis = [100, 200, 350, 450, 520, 600, 608, 500]
# ng1 = [90, 72, 144, 36, 60, 65, 80, 130, 96]
for d, a in zip(dis, ng1):
    fd(d)
    lt(a)

hideturtle()
mainloop()