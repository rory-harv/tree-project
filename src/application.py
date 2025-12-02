
from tree import Point, Node, Rectangle, Quadtree 

# image compressor 

QUAD_BOUNDARY = Rectangle(0, 0, 200, 200)   # largest boundary to contain the Quadtree
N_CAPACITY = 4      # max capacity of the Quadtree

class Pixel(object):
    """Stores information about the pixels of the image."""

    def __init__(self, color = [0, 0, 0], topLeft = Point(0, 0), bottomRight = Point(0, 0)):
        self.R = color[0]   # r-val
        self.G = color[1]   # g-val
        self.B = color[2]   # b-val
        self.topLeft = topLeft  # top left point of pixel
        self.bottomRight = bottomRight  # top right point of pixel

class Image(object):
    """Stores information about the image imported."""
    
    def __init__(self, path: str, size: int):
        self.path = path
        self.size = size





if __name__ == '__main__':

    quadtree = Quadtree.createQuad(QUAD_BOUNDARY, N_CAPACITY)   # creates main quadtree object
    #topLeft = Point(QUAD_BOUNDARY.left, QUAD_BOUNDARY.top)      # gets topleft for pixel init
    #bottomRight = Point(QUAD_BOUNDARY.right, QUAD_BOUNDARY.bottom)  # gets bottomright for pixel init
