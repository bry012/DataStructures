# Solves the "Tower of Hanoi" Puzzle.
import turtle
from disk import Disk
import time
# Count level of recursion; index of moved disk.
count = 0
# Number of disks to use.
num_disks = 3
# Initialize all disks to be on "A"
disks = [Disk(i, "A") for i in range(num_disks, 0, -1)]

sheldon = turtle.Turtle()


def moveTower(height, fromPole, toPole, withPole):
    """ Recursively solve the Tower of Hanoi puzzle. """
    global count

    if height >= 1:
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # Exercise 1
        ##
        # Use global variable to keep track of recursion depth.
        #   'count' += 1 before calling 'moveTower'
        #   'count' -= 1 after calling 'moveTower'
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        count += 1
        moveTower(height-1, fromPole, withPole, toPole)
        count -= 1
        moveDisk(fromPole, toPole)
        count += 1
        moveTower(height-1, withPole, toPole, fromPole)
        count -= 1


def moveDisk(fp, tp):
    """ Moves a disk from one pole to another. """
    print("moving disk from", fp, "to", tp)
    # turtle.writetext("hello")
    sheldon.pu()
    sheldon.goto(-175, -80)
    sheldon.color("black")
    sheldon.write(
        "moving disk from" +
        str(fp) +
        "to" +
        str(tp),
        font=(
            "Arial",
            "20",
            "bold"))
    sheldon.pd()

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Exercise 1
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # The global 'count' variable represents the index of
    # the current moving 'disk' in the list of 'disks'.
    #
    # Change the 'pole' of the 'disk' at that index to 'tp'.
    # As a sanity check, the disk at that index will be
    # on a 'pole' equal to 'fp'.
    #
    # Have the 'turtle' write text to the canvas indicating
    # what disk was moved, what pole it came from, and
    # what pole it is going to.
    #
    # Draw the results.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    currentDisk = disks[count]
    currentDisk.pole = tp
    draw()


def draw():
    """ Draws the state of the puzzle. """
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Exercise 1
    ##
    # Draw the poles.
    # Draw the disks.
    # Wait for three seconds.
    # Clear the screen.
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    _draw_poles()
    _draw_disks()

    time.sleep(1)
    sheldon.screen.clear()


def _draw_poles():
    """ Draws the Hanoi poles. """
    pole_height = 200
    pole_space = 300

    # Set pen size and color.
    sheldon.pensize("50")
    sheldon.color("brown")

    # Print a label, go to first pole's bottom.
    sheldon.pu()
    sheldon.goto(-pole_space-8, -60)
    sheldon.color("black")
    sheldon.write("A", font=("Arial", "20", "normal"))
    sheldon.color("brown")
    sheldon.goto(-pole_space, 0)
    sheldon.pd()

    # Draw first pole from bottom to top.
    sheldon.left(90)
    sheldon.forward(pole_height)

    # Go to second pole's top.
    sheldon.pu()
    sheldon.goto(0, pole_height)
    sheldon.pd()

    # Draw second pole from top to bottom.
    sheldon.right(180)
    sheldon.forward(pole_height)

    # Print labels, go to third pole's bottom.
    sheldon.pu()
    sheldon.goto(-8, -60)
    sheldon.color("black")
    sheldon.write("B", font=("Arial", "20", "normal"))
    sheldon.goto(pole_space-8, -60)
    sheldon.write("C", font=("Arial", "20", "normal"))
    sheldon.color("brown")
    sheldon.goto(pole_space, 0)
    sheldon.pd()

    # Draw third pole from bottom to top.
    sheldon.right(180)
    sheldon.forward(pole_height)

    # Re-align turtle.
    sheldon.right(90)


def _draw_disks():
    """ Draws the Hanoi disks. """
    # Find the disks contained on each pole.
    A_disks = [disk for disk in disks if disk.pole == "A"]
    B_disks = [disk for disk in disks if disk.pole == "B"]
    C_disks = [disk for disk in disks if disk.pole == "C"]

    # Draw 'A' disks.
    for i in range(len(A_disks)):
        disk = A_disks[i]
        disk.length = 75 * disk.size

        sheldon.pu()
        sheldon.goto(-300-(disk.length/2), 30 * i)
        sheldon.pd()

        _draw_disk(disk)

    # Draw 'B' disks.
    for i in range(len(B_disks)):
        disk = B_disks[i]
        disk.length = 75 * disk.size

        sheldon.pu()
        sheldon.goto(-(disk.length/2), 30 * i)
        sheldon.pd()

        _draw_disk(disk)

    # Draw 'C' disks.
    for i in range(len(C_disks)):
        disk = C_disks[i]
        disk.length = 75 * disk.size

        sheldon.pu()
        sheldon.goto(300-(disk.length/2), 30 * i)
        sheldon.pd()

        _draw_disk(disk)


def _draw_disk(disk):
    """ Draw a single disk. """
    sheldon.pensize(25)

    # Write label.
    sheldon.pu()
    sheldon.goto(sheldon.xcor() - 35, sheldon.ycor() - 16)
    sheldon.color("black")
    sheldon.write(str(disk.size), font=("Arial", "20", "bold"))
    sheldon.goto(sheldon.xcor() + 35, sheldon.ycor() + 16)
    sheldon.pd()

    # Change color based on disk size.
    if disk.size == 1:
        sheldon.color("red")
    elif disk.size == 2:
        sheldon.color("blue")
    elif disk.size == 3:
        sheldon.color("green")

    # Draw disk.
    sheldon.forward(disk.length)


def main():
    # Create a new Turtle object.
    sheldon.speed(10)

    # Go to the start position.
    sheldon.pu()
    sheldon.goto(-400, 0)
    sheldon.pd()

    # Get the screen used for drawing.
    screen = sheldon.getscreen()

    # Draw the initial state of the board.
    draw()

    # Move disks onto poles.
    moveTower(num_disks, "A", "C", "B")

    # Close the screen when it is clicked.
    screen.exitonclick()

if __name__ == "__main__":
    main()
dofjd
doifj
d
