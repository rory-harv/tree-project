
# quad tree implementation 

class Point:
    """All info on points being used for quadtree."""

    def __init__(self, x, y, data: str = None):
        self.x = x  # x-coord
        self.y = y  # y-coord
        self.data = data
    
    def getData(self):
        """Gets name/data of point inserted into the quadtree."""
        return self.data

class Node:
    """Objects to be stored in the quadtree."""

    def __init__(self, val: Point, isLeaf: bool, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf    # determines where/what the node is 
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Rectangle:
    """Information about the quadrant and boundaries."""

    def __init__(self, x: int, y: int, width: int, height: int):
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

    def containsPoint(self, point: Point):
        """Checks if quadtree contains a certain point."""
        return (self.left <= point.x <= self.right and self.top <= point.y <= self.bottom)


class Quadtree:
    """Quatree implementation."""

    def __init__(self, boundary: Rectangle, n):
        self.boundary = boundary
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

    def insert(self, point: Point) -> bool:
        """Inserts a node's point into the quadtree."""
        if point is None:
            return
        
        if not self.boundary.containsPoint(point):
            return 
        
        if len(self.points) < self.n:   # if larger than what the tree can hold 
            self.points.append(point)
            return True
        else:
            if not self.divided:    # if has not been subdivided 
                self.subdivide()

            if self.northwest.insert(point):
                return True
            if self.northeast.insert(point):
                return True
            if self.southwest.insert(point):
                return True
            if self.southeast.insert(point):
                return True
            
            return False # does not occur if node's point is within the boundary
        

        

if __name__ == '__main__':

    center_boundary = Rectangle(0, 0, 200, 200)
    quadtree = Quadtree(center_boundary, 4)  # n of 4 points per node

    # insert random points

    quadtree.insert(Point(100, 100, "a"))
    quadtree.insert(Point(10, 30, "b"))
    quadtree.insert(Point(75, 15, "c"))
    quadtree.insert(Point(0, 0, "d"))
    quadtree.insert(Point(50, 50, "e"))

    for p in quadtree.points:   # checks if nodes properly inserted - yes
        print(p.getData())

    


    

    




