import snowflake, turtle
def main(start, DEGREE):
    scaling_factor = 0.95
    num_nested = 6
    # Instantiate a turtle object.
    sheldon = turtle.Turtle()
    sheldon.speed(500)

    # Retrieve the window the turtle will use for drawing.
    screen = sheldon.getscreen()
    screen.title("Koch Curve: " + str(DEGREE) + "°")
    screen.reset()
    for x in range(num_nested):
        snowflake.drawSnowflake(sheldon,start ,DEGREE)
        start = [start[0]*scaling_factor,start[1]*scaling_factor]
    screen.exitonclick()

main([-450, 250], 3)

