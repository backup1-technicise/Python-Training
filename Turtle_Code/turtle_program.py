import turtle
def draw_different_shapes():
    window = turtle.Screen()        # Get the window to draw rectangle
    window._bgcolor("green")        # Set the background color as green
    turtle_pen1 = turtle.Turtle()    # Grab the turtle to draw rectangle.
    turtle_pen2 = turtle.Turtle()    # Grab the turtle to draw circle.
    turtle_pen3 = turtle.Turtle()    # Grab the turtle to draw triangle.
    
                        # Drawing a rectangle
    turtle_pen1.shape("square")     # Set the turtle shape as 'classic'
    turtle_pen1.speed(1)             # Set the turtle movement as 'slowest' animation
    turtle_pen1.color("red", "blue") # Set the turtle color as 'blue' and pen color as 'red'
    for side in range(4):            # 4 sides of a rectangle
        turtle_pen1.forward(100)         # Movement of turtle 100 units towards front
        turtle_pen1.right(90)            # Rotation of turtle 90 degree from current position

                        # Drawing a circle
    turtle_pen2.shape("circle")
    turtle_pen2.color("pink", "yellow")
    turtle_pen2.speed(2)
    turtle_pen2.circle(100)

                        # Drawing a triangle
    turtle_pen3.shape("turtle")
    turtle_pen3.color("black", "orange")
    turtle_pen3.speed(2)
    turtle_pen3.left(180)
    turtle_pen3.left(60)
    turtle_pen3.forward(100)
    turtle_pen3.left(90)
    turtle_pen3.forward(50)
    turtle_pen3.left(120)
    turtle_pen3.forward(111.803398875)
    window.exitonclick()            # Click to exit from drawing window

draw_different_shapes()
