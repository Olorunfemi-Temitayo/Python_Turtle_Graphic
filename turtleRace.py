from turtle import Turtle

Gee = Turtle()

Gee.color('red')
Gee.shape('turtle')
Gee.penup()
Gee.goto(-160, 100)
Gee.pendown()

Tee = Turtle()

Tee.color('blue')
Tee.shape('turtle')
Tee.penup()
Tee.goto(-160, 70)
Tee.pendown()

Pee = Turtle()

Pee.color('green')
Pee.shape('turtle')
Pee.penup()
Pee.goto(-160, 40)
Pee.pendown()

Bee = Turtle()

Bee.color('purple')
Bee.shape('turtle')
Bee.penup()
Bee.goto(-160, 10)
Bee.pendown()


from random import randint

for movement in range(100):
    Gee.forward(randint(1, 5))
    Tee.forward(randint(1, 5))
    Pee.forward(randint(1, 5))
    Bee.forward(randint(1, 5))
input("Press Enter to Close")









