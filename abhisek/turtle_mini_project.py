import turtle
def Circle_using_Rectangles():
    window = turtle.Screen()        # Get the window to draw shape
    window._bgcolor("black")          # Set the background color as black
    
    turtle_pen = turtle.Turtle()    # Grab the turtle to draw my name in short form
    turtle_pen_flower = turtle.Turtle() # Grab the turtle to draw a flower
    
    # Write the short form of my name
    turtle_pen.shape("turtle")     # Set the turtle shape as 'classic'
    turtle_pen.speed(1)             # Set the turtle movement as 'Average' animation
    turtle_pen.color("green", "blue") # Set the turtle color as 'blue' and pen color as 'green'
    ''' Set the turtle at certain co-ordinate before draw any shape '''
    turtle_pen.penup()
    turtle_pen.goto(-300, 0)
    turtle_pen.pendown()
    ''' For the first initial of my name A '''
    turtle_pen.left(60)
    turtle_pen.forward(200)
    turtle_pen.right(120)
    turtle_pen.forward(120)
    turtle_pen.right(120)
    turtle_pen.forward(120)
    turtle_pen.right(180)
    turtle_pen.penup()
    turtle_pen.forward(120)
    turtle_pen.pendown()
    turtle_pen.right(60)
    turtle_pen.forward(80)
    turtle_pen.left(60)
    ''' For the separator (o) '''
    turtle_pen.penup()
    turtle_pen.forward(20)
    turtle_pen.pendown()
    turtle_pen.circle(5)
    ''' For the second initial of my name R '''
    turtle_pen.penup()
    turtle_pen.forward(20)
    turtle_pen.pendown()
    turtle_pen.left(90)
    turtle_pen.forward(180)
    turtle_pen.right(90)
    turtle_pen.forward(90)
    turtle_pen.right(90)
    turtle_pen.forward(90)
    turtle_pen.right(90)
    turtle_pen.forward(90)
    turtle_pen.left(135)
    turtle_pen.forward(140)

    # Draw a flower
    turtle_pen.penup()
    turtle_pen.goto(300,0)  # Space between shapes
    turtle_pen.pendown()
    turtle_pen_flower = turtle_pen

    turtle_pen_flower.shape("turtle")     # Set the turtle shape as 'turtle'
    turtle_pen_flower.speed(6)             # Set the turtle movement as 'Average' animation
    turtle_pen_flower.color("yellow", "blue") # Set the turtle color as 'blue' and pen color as 'green'
    
    max_rotation = 360
    shift_per_rotation = 5
    no_of_rotation = (max_rotation / shift_per_rotation)
    for rotation in range(1, no_of_rotation + 1) :           
        for side in range(1, 5):                       # 4 sides of a rhombus
            if side % 2 != 0: 
                turtle_pen_flower.forward(100)                 # Movement of turtle 100 units towards front
                turtle_pen_flower.left(40)                     # Rotation of turtle 40 degree towards left from current position
            else:
                turtle_pen_flower.forward(100)                 # Movement of turtle 100 units towards front
                turtle_pen_flower.left(140)                     # Rotation of turtle 40 degree towards left from current position
        #if rotation != no_of_rotation:
        turtle_pen_flower.right(shift_per_rotation)        # Rotation of turtle with degree (shift_per_rotation) from current position to right
            
    #turtle_pen_flower.left(50)
    #turtle_pen_flower.forward(200)
    window.exitonclick()            # Click to exit from drawing window

Circle_using_Rectangles()
