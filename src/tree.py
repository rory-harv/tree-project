
# quad tree implementation 

class Point:
    """All info on points being used for quadtree."""

    def __init__(self, x, y):
        self.x = x  # x-coord
        self.y = y  # y-coord

class Node:
    """Objects to be stored in the quadtree."""

    def __init__(self, pos, data):
        self.pos = pos  # position
        self.data = data    # data 

class Quadtree:
    """Quatree implementation."""


