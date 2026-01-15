from math import sqrt
from turtle import forward, left, right, exitonclick, speed
from random import randint

def domecek(a):
    b = sqrt(2*(a**2))
    speed(100)
    forward(a)
    left(135) 
    forward(b) 
    right(135) 
    forward(a)
    left(120)
    forward(a)
    left(120) 
    forward(a)
    left(30)
    forward(a)
    left(135)
    forward(b)
    right(135)
    forward(a)

for i in range(5):
    domecek(randint(10, 150))
    right(360)

exitonclick()
