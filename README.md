# tree-project

Team: Rory Harvey

Project Title: Photo Editor
What tree did you implement?: Quadtrees

What does your application do?: 
This photo editor takes in images presented by the user, and utlizes the quadtree data structure to either compress said images into a new format. 

Who would use this and why?:
Photographers may find this tool useful when storing a bulk amount of digital photographs that must vary in size for delivery or transferring. 

Installation & Setup
PIL Python library and numpy library required for execution. 
When the application file is run, the user will be requested to input a file path into the terminal for the image they are looking to compress. All test images are stored in the "images" folder, so the input should be in the format of "images/filename.JPG". 
From there, the user will be prompted to input a "threshold value". This value determines the level of compression that is applied to the inputted image. A higher threshold value results in a more compressed image (quality decreases). A "happy medium" seems to be around 10-20 --- where the image is clearly compressed, however, image details remain present. 
Run the application like a standard python file. When prompted, enter your image file path, and a threshold value for compression. Then, the compressed version of your image will be saved within the same folder with "_compressed.png" at the end. 

Usage Guide

Example commands:

1. Input:
    Please enter an image path name: images/plants.JPG
    Please enter a threshold value integer: 20
1. Output: 
![alt text](C:\Users\victo\Downloads\Git-it-Win-ia32\tree-project\images\plants.JPG_compressed.png)

2. Input: 
    Please enter an image path name: images/plants.JPG
    Please enter a threshold value integer: 20
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