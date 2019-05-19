from turtle import * #импорт всех функций модуля (позваоляет не писать каждый
                        # раз turtle.color() и т.д.
import random
colours = ["blue", "purple", "cyan", "white", "yellow", "green", "orange"]
shape("turtle")
speed(10)
pensize(6)
Screen().bgcolor("turquoise")
# для того чтобы скрыть черепашку необходимо использовать функцию "hideturtle()"
def vshape(size): #def (от define (определять) пользовательская функция
    right(25)
    forward(size)
    backward(size)
    left(50)
    forward(size)
    backward(size)
    right(25)
def snowflakeArm(size):
    for x in range(0,4):
        forward(size)
        vshape(size)
    backward(size * 4)
def snowflake(size):
    for x in range(0,6):
        color(random.choice(colours))
        snowflakeArm(size)
        right(60)
for i in range(0,10):
    size = random.randint(5,30)
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    penup()
    goto(x,y)
    pendown()
    snowflake(size)
