import turtle

def draw_circle(radius, color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_ear(radius, color):
    turtle.setheading(90)
    turtle.right(30)
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.circle(radius, 90)
        turtle.circle(radius / 2, 90)
    turtle.end_fill()

# Setup the screen
turtle.setup(800, 600)
turtle.speed('fastest')

# Move to starting position
turtle.penup()
turtle.goto(0, -100)  # Position to draw face
turtle.pendown()

# Draw face
draw_circle(150, 'lightblue')  # Assuming Doraemon has a light blue face

# Draw ears
turtle.penup()
turtle.goto(-70, 100)  # Position to draw left ear
turtle.pendown()
draw_ear(40, 'lightblue')

turtle.penup()
turtle.goto(70, 100)  # Position to draw right ear
turtle.pendown()
draw_ear(40, 'lightblue')

# Hide turtle and display window
turtle.hideturtle()
turtle.done()
