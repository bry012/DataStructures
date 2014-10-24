# Data structure for a Hanoi disk.
class Disk:
    """ Represents a Hanoi disk. """
    def __init__(self, size, pole):
        self.size = size
        self.pole = pole

    def __str__(self):
        """ A string representation of a Disk object. """
        representation = "Disk:\n  Size: " + self.size + "\n  Pole: " + self.pole
        return representation
