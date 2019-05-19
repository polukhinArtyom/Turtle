from turtle import * #импорт всех функций модуля (позваоляет не писать каждый
                        # раз turtle.color() и т.д.
color("white")
shape("turtle")
speed(10)
pensize(6)
Screen().bgcolor("turquoise")
# для того чтобы скрыть черепашку необходимо использовать функцию "hideturtle()"
def vshape(): #def (от define (определять) пользовательская функция
    right(25)
    forward(50)
    backward(50)
    left(50)
    forward(50)
    backward(50)
    right(25)
def snowflakeArm():
    for x in range(0,4):
        forward(30)
        vshape()
    backward(120)
def snowflake():
    for x in range(0,6):
        snowflakeArm()
        right(60)
snowflake() # Вызов функции
