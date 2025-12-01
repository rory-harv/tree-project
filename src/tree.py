
# quad tree implementation 

class Point:
    """All info on points being used for quadtree."""

    def __init__(self, x, y, data = None):
        self.x = x  # x-coord
        self.y = y  # y-coord
        self.data = data    # data stored within the point
    
    def getData(self):
        """Gets name/data of point inserted into the quadtree."""
        return self.data
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.data == other.data

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

    def subdivide(self) -> None:
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
            return False
        
        if not self.boundary.containsPoint(point):
            return False
        
        if len(self.points) < self.n:   # if larger than what the tree can hold 
            self.points.append(point)
            return True
        else:
            if not self.divided:    # if has not been subdivided 
                self.subdivide()

            if self.northwest.insert(point):
                return True
            elif self.northeast.insert(point):
                return True
            elif self.southwest.insert(point):
                return True
            elif self.southeast.insert(point):
                return True
            else:
                return False # does not occur if node's point is within the boundary
        
    def delete(self, point: Point) -> bool:
        """Deletes point from the quadtree."""
        if point is None:   # can't remove a non existent node
            return False

        if not self.boundary.containsPoint(point):  # can't remove a non existent node
            return False
        
        if not self.divided:    # if leaf node / not subdivided
            if point in self.points:    
                self.points.remove(point)   # deletes from list
                return True
            return False

        else:   # internal node / recursive calls
            deleted = False     # creates bool to determine if deleted yet
            if self.northwest.boundary.containsPoint(point):
                deleted = self.northwest.delete(point)

            elif self.northeast.boundary.containsPoint(point):
                deleted = self.northeast.delete(point)

            elif self.southwest.boundary.containsPoint(point):
                deleted = self.southwest.delete(point)

            elif self.southeast.boundary.containsPoint(point):
                deleted = self.southeast.delete(point)
        
            if deleted:
                self.merge() # merge if children are empty 
            return deleted
        
    def merge(self) -> None:
        """Checks if quadtree can merge after deletion."""

        if (not self.northwest.divided and not self.northeast.divided and not 
            self.southwest.divided and not self.southeast.divided):     # if nothing is subdivided

            total_points = (len(self.northwest.points) + len(self.northeast.points) +
                            len(self.southwest.points) + len(self.southeast.points))    # combined points
            
            if total_points <= self.n:  # if total number of points larger than what the quadtree can contain

                self.points.extend(self.northwest.points)   # appends directional points to quadtree points list
                self.points.extend(self.northeast.points)   # extend() unpacks the iterable and adds each of its individual elements to the end of the list it's called on
                self.points.extend(self.southwest.points)   # instead of append() which adds it as a single element
                self.points.extend(self.southeast.points)

                self.northwest = None # reset children nodes and mark all as not divided
                self.northeast = None
                self.southwest = None
                self.southeast = None
                self.divided = False

        

if __name__ == '__main__':

    center_boundary = Rectangle(0, 0, 200, 200) # creates broad boundary box for the tree to be contained within 
    quadtree = Quadtree(center_boundary, 4)  # n capacity (multiple of 4)

    # insert random points

    quadtree.insert(Point(100, 100, "a"))
    quadtree.insert(Point(10, 30, "b"))
    quadtree.insert(Point(75, 15, "c"))
    quadtree.insert(Point(0, 0, "d"))
    quadtree.insert(Point(50, 50, "e"))
    quadtree.delete(Point(10, 30, "b")) # deletes point a? - no

    for p in quadtree.points:   # checks if nodes properly inserted - yes 
        print(p.getData())

    


    

    




