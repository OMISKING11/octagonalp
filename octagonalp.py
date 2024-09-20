import turtle as t
import random

# Set up the screen
win = t.Screen()
win.bgcolor("black")
colours = "red", "yellow", "blue", "green", "pink", 
"purple", "violet"

# Create a turtle
t = t.Turtle()
t.speed(0)
t.pensize(10)

# Function to draw an octagon
def draw_octagon(t, size):
    for _ in range(8):
        colour = random.choice(colours)
        t.pencolor(colour)
        t.forward(size)
        t.right(45)

# Function to generate a random color
# def random_color():
#     return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# Draw the octagonal pattern
def op():
    for _ in range(8):
        t.penup()
        t.pendown()
        colour = random.choice(colours)
        t.pencolor(colour)
        draw_octagon(t, 50)
        t.right(45)

t.goto(0, 0)
op()
t.penup()
t.goto(-200,-200)
t.pendown()
op()
t.penup()
t.goto(200,-200)
t.pendown()
op()
t.penup()
t.goto(200,200)
t.pendown()
op()
t.penup()
t.goto(-200,200)
t.pendown()
op()
t.hideturtle()
win.mainloop()