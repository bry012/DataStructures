#######################################
# Project 3: Fractals
# Koch Snowflake
#
# 10/19/2014
#
# point_helpers.py
#--------------------------------------
# Defines functions for manipulating
## 2-dimensional coordinates.
#######################################

import math

def diff(begin, end):
    """ Calculates the difference between the x,y coordinates of two points. """
    x_diff = end[0] - begin[0]
    y_diff = end[1] - begin[1]

    return (x_diff, y_diff)

def split(begin, end, n=2):
    """ Calculates 'n' equidistant points between 'begin' and 'end'. """
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Koch Snowflake
    ##
    # See project file for a description of this function.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Delete this line:
    x_diff,y_diff = diff(begin,end)
    x_inc = x_diff/float(n+1)
    y_inc = y_diff/float(n+1)
    coords = [[begin[0]+x_inc, begin[1]+y_inc]]
    for x in range(n-1):
        coords.append([coords[x][0]+x_inc, coords[x][1]+y_inc])
    return coords
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def dist(begin, end):
    """ Calculates the distance between two points. """
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Koch Snowflake
    ##
    # See project file for a description of this function.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    return ((begin[0] - end[0])**2 + (begin[1]-end[1])**2)**(1/2)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def pythag(a=None, b=None, c=None):
    """ Calculates the unknown side of a right triangle. """
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Koch Snowflake
    ##
    # See project file for a description of this function.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if a == None:
        return (c**2 - b**2)**(1/2)

    elif b == None:
        return (c**2 - a**2)**(1/2)

    elif c == None:
        return (a**2 + b**2)**(1/2)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def triangulate(a, b):
    """ Calculates the third point of an equilateral triangle. """
    # Find the distance between the equidistant points.
    distance = dist(a, b)
    # Find the height of the equilateral triangle.
    height = pythag(a=distance/2, c=distance)

    # Find the difference between their x,y components.
    x_diff, y_diff = diff(a, b)

    # Calculate the angle between these two points.
    angle = math.atan2(y_diff, x_diff)

    # Initially, 'x' is a value between the x-coordinates of 'a' and 'b'.
    x = (a[0] + b[0]) / 2
    # However, the angle between 'a' and 'b' will change.
    ## 'x' must be shifted based on this angle.
    x -= height * (math.sin(angle))
    # Initially, 'y' is a value between the y-coordinates of 'a' and 'b'.
    y = (a[1] + b[1]) / 2

    # However, the angle between 'a' and 'b' will change.
    ## 'y' must be shifted based on this angle.
    y += height * (math.cos(angle))

    return [x, y]

def main():
    points = split([0,0],[99,0],2)
    for index in range(len(points) - 1):
        print(triangulate(points[index], points[index + 1]))

if __name__ == "__main__":
    main()
