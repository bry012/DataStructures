#######################################
# Project 3: Fractals
# Koch Snowflake
#
# 10/19/2014
#
# snowflake.py
#--------------------------------------
# Draws a single Koch snowflake.
#######################################

import turtle

from point_helpers import split,triangulate

def koch(points, degree):
    """ Recursively generates Koch curves from line segments. """
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Exercise 1
    ##
    # Base case: degree == 0
    # Else: recurse on 'expanded' points, minus one degree
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Delete these lines:
    if degree == 0:
        return points
    else:
        return koch(expand(points), degree - 1)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def expand(points):
    """ Expands line segments into Koch curves. """
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Exercise 1
    ##
    # Base case: len(points) == 2
    # Else: recurse on first two points; recurse on rest
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Delete this line:
    if len(points) == 2:
        a,b = split(points[0], points[1])
        c = triangulate(a,b)
        return [points[0],a,c,b,points[1]]
    else:
        return expand(points[0:2])+expand(points[1:])
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def draw(sheldon, points):
    """ Draw the Koch Snowflake! """
    sheldon.pd()
    for point in points:
        sheldon.goto(point[0], point[1])
    sheldon.pu()

def randomColor():
    """ Generate a color from random RGB components. """
    from random import randint

    # Create a dictionary of random RGB components.
    color = { "r" : randint(0, 255)/255.,
              "g" : randint(0, 255)/255.,
              "b" : randint(0, 255)/255. }

    return color

def drawSnowflake(sheldon, start, DEGREE):


    # Place turtle at starting point.
    sheldon.pu()
    sheldon.goto(start)
    sheldon.pd()

    # Define the top portion of the triangle.
    begin = [start[0], start[1]]
    end = [-start[0], start[1]]
    top = koch([begin, end], DEGREE)

    # Calculate a random color to fill the Koch Snowflake.
    color = randomColor()
    sheldon.fillcolor(color["r"], color["g"], color["b"])
    sheldon.begin_fill()

    # Draw top of the triangle.
    draw(sheldon, top)
    begin = end
    end = triangulate(end, start)
    top = koch([begin, end], DEGREE)
    draw(sheldon,top)

    start = begin
    begin = end
    end = triangulate(end,start)
    top = koch([begin, end], DEGREE)
    draw(sheldon,top)
    sheldon.end_fill()

def main(start):
    """ Begins the calculation and drawing of a Koch snowflake. """
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Exercise 1
    ##
    # Calculate a Koch curve of at least 3 degrees.
    # Draw the resulting points.
    # Create a Koch snowflake from three, triangulated Koch curves.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # Initialize a 'start' point for the Koch curve.

    # Specify how many iterations should be performed.
    DEGREE = 3
    # Instantiate a turtle object.
    sheldon = turtle.Turtle()
    sheldon.speed(1000)

    # Retrieve the window the turtle will use for drawing.
    screen = sheldon.getscreen()
    screen.title("Koch Curve: " + str(DEGREE) + "°")
    screen.reset()

    for x in range(6):
        drawSnowflake(sheldon,start ,DEGREE)
        start = [start[0]*0.75,start[1]*0.75]
    screen.exitonclick()

if __name__ == "__main__":
   main([-450, 250])
   pass
