import Blocks

class Node(Blocks.Blocks):
    """A node is a floor block of our character."""
    def __init__(self, x, y):
        Blocks.__init__(x,y)
        