import turtle
# square
insanity_turtle = turtle.Turtle()
insanity_turtle.speed(0)


def square():
  insanity_turtle.forward(100)
  insanity_turtle.right(90)
  insanity_turtle.forward(100)
  insanity_turtle.right(90)
  insanity_turtle.forward(100)
  insanity_turtle.right(90)
  insanity_turtle.forward(100)

for count in range(4):
  square()

insanity_turtle.forward(200)

for count in range(4):
  square()
  
insanity_turtle.forward(100)

for count in range(2):
  square()


#Triangle

def triangle():
  insanity_turtle.forward(100)
  insanity_turtle.left(120)
  insanity_turtle.forward(100)
  insanity_turtle.left(120)
  insanity_turtle.forward(100)

for count in range(3):
  triangle()

insanity_turtle.forward(200)

for count in range(3):
  triangle()

insanity_turtle.hideturtle()