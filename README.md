# tree-project

Team: Rory Harvey

Project Title: Photo Editor
What tree did you implement?: Quadtrees

What does your application do?: 
This photo editor takes in images presented by the user, and utlizes the quadtree data structure to either compress or decompress said images into a new format. 

Who would use this and why?:
Photographers may find this tool useful when storing a bulk amount of digital photographs that must vary in size for delivery or transferring. 

Installation & Setup
Prerequisites (Python version, libraries, etc.)
Step-by-step setup instructions
How to run the application
Usage Guide
How to use your application
Example commands or interactions
Expected input/output
Screenshots/Demos
At least 3 screenshots showing your application in action
Annotate what we're looking at if it's not obvious
Tree Implementation Details
Brief explanation of how your tree works
Time/space complexity of key operations
Any interesting implementation choices
Evolution of the Interface

- Return type for insert changed from None to bool in order to determine if the insert can occur or not, rather than simply inserting it regardless.
- inBoundary became containsPoint to better understand which points are already contained in the quadtree.
- Rectangle and Point classes introduced to help Quadtree construction and searching/traversing. 



What changed from your initial design?
Why did you need those changes?
What did you learn from this iterative process?
Challenges & Solutions
What was hard?
How did you solve tough problems?
Future Enhancements
What would you add with more time?