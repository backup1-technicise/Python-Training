import turtle
def Circle_using_Rectangles():
    window = turtle.Screen()        # Get the window to draw rectangle
    window._bgcolor("red")          # Set the background color as red
    turtle_pen = turtle.Turtle()    # Grab the turtle to draw rectangle.
    
            # Drawing a Circle using multiple rectangles 
    turtle_pen.shape("turtle")     # Set the turtle shape as 'classic'
    turtle_pen.speed(6)             # Set the turtle movement as 'slowest' animation
    turtle_pen.color("yellow", "blue") # Set the turtle color as 'blue' and pen color as 'yellow'
    max_rotation = 360
    shift_per_rotation = 5
    for rotation in range(1, max_rotation / shift_per_rotation):           
        for side in range(4):                       # 4 sides of a rectangle
            turtle_pen.forward(100)                 # Movement of turtle 100 units towards front
            turtle_pen.right(90)                    # Rotation of turtle 90 degree from current position
        turtle_pen.right(shift_per_rotation)        # Rotation of turtle with degree (shift_per_rotation) from current position to right       
    window.exitonclick()                            # Click to exit from drawing window

Circle_using_Rectangles()
