
from typing import Protocol

class IQuad(Protocol):

    def insert(self, node) -> None:
        """Insert a word into the quadtree"""
        pass

    def search(self, p) -> int:
        """Find a point in the quadtree"""
        pass

    def inBoundary(self, p) -> bool:
        """Checks if the quadtree contains a certain point"""
        pass

    def delete(self, node) -> None:
        """Deletes node from the quadtree"""
        pass