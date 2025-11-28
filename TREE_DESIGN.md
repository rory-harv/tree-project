
Rory Harvey

Tree Selection: Quadtree. 
I chose to work with Quadtrees because of their applications for data storage in 2D space/games. I also decided to do my student contributed lecture of octrees, so it felt fitting to evaluate quadtrees --- the basis of octrees. 

Use Cases: Image compression and searching 2D space. 
For image compression, similar to octrees, quadtrees are able to evaluate and search RGB colors that are contained within the tree data structure, and work to perform averages and compute compressed images that maintain similar color composition on a smaller scale. 

Properties: Hierarchial data structure. 
Quadtrees operate as a hierarchy, subdividing 2D space into quadrants at a time until there is no more data to store, making them highly adaptive and easier to search than other trees. Quadtrees utilize adaptive spatial partitioning and early termination to provide an average time complexity of O(log n) for point queries, insertion, and deletion, and a worst-case complexity of O(n).

Interface Design:

from typing import Protocol

class IQuad(Protocol):

    def insert(self, node) -> None:
    """Insert a word into the quadtree.
    Time: O(log n) - average - where n is the number of points in the quadtree
    Space: O(n) - average/worst - where n is the number of points
    """

    def search(self, p) -> int:
    """Find a point in the quadtree
    Time: O(log n) - average - where n is the number of points
    Space: O(n) - average - where n is the number of points
    """

    def inBoundary(self, p) -> bool:
    """Checks if the quadtree contains a certain point
    Time: O(log n) - average - where n is the number of points
    Space: O(n) - average - where n is the number of points
    """

    def delete(self, node) -> None:
    """Deletes node from the quadtree
    Time: O(log n) - average - where n is the number of points
    Space: Time: O(log n) + O(n) - average - where n is the number of points, plus the space required to store the quadtree nodes themselves 
    """






