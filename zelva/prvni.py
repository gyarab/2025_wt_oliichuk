from turtle import forward, left, exitonclick
from math import sqrt

def domecek(a): 
    c = a / sqrt(2)
    forward(a) 
    left(90) 
    forward(a)
    left(90) 
    forward(a) 
    left(90)
    forward(a) 
    left(90) 
    forward(a)  
    
domecek(50)
for i in range(10): 
    domecek(50) 

exitonclick()