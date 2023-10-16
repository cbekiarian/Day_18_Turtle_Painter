from turtle import Turtle, Screen,colormode
from random import randint

screen = Screen()
tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")
# tim.pensize(10)
screen.colormode(255)
def draw_shape():
    for i in range(3,11):
        screen.colormode(255)
        tim.pencolor(randint(0,254),randint(0,254),randint(0,254))
        for j in range(0,i):
            tim.forward(100)
            tim.right(360/i)

def random_walk ():
    while True:

        tim.pencolor(randint(0,255),randint(0,255),randint(0,255))
        tim.forward(10)
        kok = randint(0,3)

        if kok == 1:
            tim.right(90)
        elif kok == 2:
            tim.right(180)
        elif kok == 3:
            tim.left(90)

def random_circle():


    for m in range(0,100):
        tim.pencolor(randint(0,255),randint(0,255),randint(0,255))
        tim.circle(100)
        tim.right(360/100)




random_circle()

screen.exitonclick()