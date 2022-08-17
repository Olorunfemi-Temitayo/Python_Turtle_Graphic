from turtle import Turtle

laura = Turtle()

laura.color('red')
laura.shape('turtle')
laura.penup()
laura.goto(-160, 100)
laura.pendown()

rik = Turtle()

rik.color('blue')
rik.shape('turtle')
rik.penup()
rik.goto(-160, 70)
rik.pendown()

lauren = Turtle()

lauren.color('green')
lauren.shape('turtle')
lauren.penup()
lauren.goto(-160, 40)
lauren.pendown()

carrie = Turtle()

carrie.color('purple')
carrie.shape('turtle')
carrie.penup()
carrie.goto(-160, 10)
carrie.pendown()


from random import randint

for movement in range(100):
    laura.forward(randint(1, 5))
    rik.forward(randint(1, 5))
    lauren.forward(randint(1, 5))
    carrie.forward(randint(1, 5))
input("Press Enter to Close")









