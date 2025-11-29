
# quad tree implementation 

class Point:
    """All info on points being used for quadtree."""

    def __init__(self, x, y):
        self.x = x  # x-coord
        self.y = y  # y-coord

class Node:
    """Objects to be stored in the quadtree."""

    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf    # determines where/what the node is 
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Rectangle:
    """Information about the quadrant."""

    def __init__(self, x, y, width, height):
        # rectangle measurements 
        self.x = x  
        self.y = y  
        self.width = width
        self.height = height

        # boundary measurements
        self.left = x - width / 2
        self.right = x + width / 2
        self.top = y - height / 2
        self.bottom = y + height / 2

    def containsPoint(self, point):
        """Checks if quadtree contains a certain point."""
        return (self.left <= point.x <= self.right and self.top <= point.y <= self.bottom)


class Quadtree:
    """Quatree implementation."""

    def __init__(self, boundary, n):
        self.boundary: Rectangle = boundary
        self.n = n  # max number of points a node can hold before subdividing
        self.points = []
        self.divided = False    # if tree already subdivided

    def subdivide(self):
        """Subdivides the quadtree to search and create boundaries."""
        
        x, y, w, h = self.boundary.x, self.boundary.y, self.boundary.width, self.boundary.height
        halfw, halfh = w / 2, h / 2

        # create four 'child' boundaries that serve to evaluate the bounding box
        nw_boundary = Rectangle(x - halfw / 2, y - halfh / 2, halfw, halfh)
        ne_boundary = Rectangle(x + halfw / 2, y - halfh / 2, halfw, halfh)
        sw_boundary = Rectangle(x - halfw / 2, y + halfh / 2, halfw, halfh)
        se_boundary = Rectangle(x + halfw / 2, y + halfh / 2, halfw, halfh)

        # create four child quadtrees recursively until they cannot be subdivided anymore 
        self.northwest = Quadtree(nw_boundary, self.n)
        self.northeast = Quadtree(ne_boundary, self.n)
        self.southwest = Quadtree(sw_boundary, self.n)
        self.southeast = Quadtree(se_boundary, self.n)

        self.divided = True # sets subdivided as true 

    def insert(self, node):
        """Inserts a node into the quadtree."""
        if node is None:
            return
        

if __name__ == '__main__':

    center = Quadtree(Point(0, 0), Point(8, 8))
    a = Node(Point(1, 1), 1)
    b = Node(Point(2, 5), 2)
    c = Node(Point(7, 6), 3)

    

    




