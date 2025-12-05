# tree-project

Team: Rory Harvey

Project Title: Photo Compressor
What tree did you implement?: Quadtrees

What does your application do?: 
This photo editor takes in images presented by the user, and utlizes the quadtree data structure to either compress said images into a new format. 

Who would use this and why?:
Photographers may find this tool useful when storing a bulk amount of digital photographs that must vary in size for delivery or transferring. 

Installation & Setup:
PIL Python library and numpy library required for execution. 
When the application file is run, the user will be requested to input a file path into the terminal for the image they are looking to compress. All test images are stored in the "images" folder, so the input should be in the format of "images/filename.JPG". 
From there, the user will be prompted to input a "threshold value". This value determines the level of compression that is applied to the inputted image. A higher threshold value results in a more compressed image (quality decreases). A "happy medium" seems to be around 10-20 --- where the image is clearly compressed, however, image details remain present. 
Run the application like a standard python file. When prompted, enter your image file path, and a threshold value for compression. Then, the compressed version of your image will be saved within the same folder with "_compressed.png" at the end. 

Usage Guide:
Example commands & Screenshots/Demos:

1. Input:
    Please enter an image path name: images/plants.JPG
    Please enter a threshold value integer: 20
1. Output: 
![alt text](C:\Users\victo\Downloads\Git-it-Win-ia32\tree-project\images\plants.JPG_compressed.png)

-> This output reflects a compressed image with a medium-compression.

2. Input: 
    Please enter an image path name: images/dog.JPG
    Please enter a threshold value integer: 10
2. Ouput:
![alt text](C:\Users\victo\Downloads\Git-it-Win-ia32\tree-project\images\dog.JPG_compressed.png)

-> This output reflects a compressed image with a low-compression.

3. Input:
    Please enter an image path name: images/spiral.PNG
    Please enter a threshold value integer: 35
3. Output:
![alt text](C:\Users\victo\Downloads\Git-it-Win-ia32\tree-project\images\spiral.PNG_compressed.png)

-> This output reflects a compressed image with a higher-compression.


Tree Implementation Details:
Quadtrees work by taking 2D space and breaking up the space recursively into 4 quadrants. Each quadrant of 2D space contains nodes, that can also be broken down further into new quadrants within the quadrants. This containment of nodes is especially helpful in 2D game management of space, as well as tracking collisions, and for non-game development, image compression. 

Time/space complexity of key operations:

    def reconstruct_image(node: Node, output_image_array):
        Time Complexity: O(n) - for loop traverses through child nodes
        Space Complexity: O(n) - dependent on the number of nodes in the quadtree
    
    def build_quadtree(image_data, x: int, y: int, width: int, height: int, threshold: int):
        Time Complexity: O(n * p) - n is number of nodes and p is number of pixels that the function must traverse recursively. 
        Space Complexity: O(n * p) - dependent on the number of nodes and tree depth, as well as the number of pixels that are being traversed recursively. 

Any interesting implementation choices:
In a lot of my research about quadtrees and image compression, I noticed that recursion is very important. It helps traverse the quadtree thoroughly without visiting nodes multiple times, and messing up the search. That's why I settled on using recursive functions to build the image compression program; it seemed the most consistent in nature, and the most efficient, as well, in terms of decreasing time and space complexities. When I initially went into coding the image compression application, I kept trying to sort out a bunch of functions that would call each other, but I found it was easiest to keep track of variables and node information by just using two primary recursive functions. 

Evolution of the Interface:
- Return type for insert changed from None to bool in order to determine if the insert can occur or not, rather than simply inserting it regardless.
- inBoundary became containsPoint to better understand which points are already contained in the quadtree.
- Rectangle and Point classes introduced to help Quadtree construction and searching/traversing. 
- Node class editited to properly store data for image compression over a more simple expression of storing nodes and their information. 
- Downsizing images inspired by one of my previous octree implementations in order to decrease runtimes on my laptop for the program (optional). 

Challenges & Solutions:
- Restarted entire application twice. Initially, was trying to build everything from scratch, realized I needed to do much more research. I then was attempting to find similarities between different recommended strategies to find a common ground, but got confused with my own code, and started from the beginning again. Made a thorough plan before implementation, and firmly decided on two set libraries to guide me through the process (PIL and numpy). Researched a lot on numpy for conversions and reconstructing arrays. 
- Mathematical operations required the most intensive research. Figuring out the proper measurements for the regional boundary boxes in the build_quadtree() recursive function was the hardest, by far. Eventually I came across resources that helped me visualize the math behind the recursion, and it made it easier for me to understand why the child nodes are broken down with various width and height half measurements (each served as half of the regional box, breaking down the region into four quandrants around a central pixel to help find color averages and child nodes).

Future Enhancements:
I really want to get down to the bottom of why my compressor turns my images sideways when they are saved. It's a weird bug, but I would want to spend some more time getting to know my code better and debug to understand the breakdown process of reconstructing at an odd angle.
In terms of scale, I would want to look at creating a decompressor, as well. 
