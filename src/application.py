
from tree import Point, Node, Rectangle, Quadtree 
from PIL import Image
import math
import numpy as np

# image compressor 

#QUAD_BOUNDARY = Rectangle(0, 0, 200, 200)   # largest boundary to contain the Quadtree
N_CAPACITY = 100      # max capacity of the Quadtree


class Pixel:
    """Stores information about the pixels of the image."""

    def __init__(self, color, point):
        self.R = color[0]   # r-val
        self.G = color[1]   # g-val
        self.B = color[2]   # b-val
        self.point = point  # point coords


class Img:
    """Stores information and functions for constructing the image's quadtree."""

    def __init__(self, width, height):
        self.width: int = width  # image width
        self.height: int = height    # image height      

    def constructOGQuad(width: int, height: int, image) -> Quadtree:
        """Constructs the original basis of the quadtree for the image."""
        boundary = Rectangle(0, 0, width, height)   # creates boundary box for image

        quadtree: Quadtree = Quadtree.createQuad(boundary, N_CAPACITY)    # creates quadtree for image

        for i in range(width):
            for j in range(height):     # loops through all points/pixels of the image
                x_coord: int = i
                y_coord: int = j
                pixel_color = image.getpixel((x_coord, y_coord))    # gets tuple of RGB values
                quadtree.insert(Pixel(pixel_color, Point(x_coord, y_coord))) # appends pixel as a node in the quadtree

        return quadtree

    def displayImage(quadtree: Quadtree, image_data, width: int, height: int):
        """Displays new compressed quadtree image."""

        for node in quadtree.points:
            x_coord = node.x
            y_coord = node.y
            region = image_data[y_coord : y_coord + height, x_coord : x_coord + width]
            Img.calculateHomogeneity(region, x_coord, y_coord, width, height)

        
    def isHomogeneous(self, region, threshold) -> bool:
        """Checks to see if the standard deviation of colors is low."""
        return np.std(region) < threshold
    
    def calculateHomogeneity(self, region, x: int, y: int, width: int, height: int):
        """Calculates the homogenity metric of the colors of the region."""
        if N_CAPACITY == 0 or self.isHomogeneous(region, N_CAPACITY):
            self.average_color = np.mean(region, axis=(0, 1)).astype(int)
        else:
            half_width = width // 2
            half_height = height // 2
            
            self.children.append(Node(Point(x, y), half_width, half_height, image_data, max_depth - 1, threshold))
            self.children.append(Node(Point(x + half_width, y), width - half_width, half_height, image_data, max_depth - 1, threshold))
            self.children.append(Node(Point(x, y + half_height), half_width, height - half_height, image_data, max_depth - 1, threshold))
            self.children.append(Node(Point(x + half_width, y + half_height), width - half_width, height - half_height, image_data, max_depth - 1, threshold))





if __name__ == '__main__':

    image_path = ""     # gather image path
    img_width: int = 0  # initialize boundary size
    img_height: int = 0

    try:
        image = Image.open(image_path)     # opens image and converts into an object
        image_data = Image.open(image_path).convert("RGB")  # gets rgb version of pixels of image
        img_width, img_height = image.size     # finds image size boundaries
        print(f"Image {image_path} loaded successfully.")
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
    except Exception as e:
        print(f"An error occurred while opening the image: {e}")

    #boundary = Rectangle(0, 0, img_width, img_height)   # initilize boundary box for image

    image_quad = Img.constructOGQuad(img_width, img_height, image, image_data)   # creates main quadtree object
    Img.displayImage(image_quad, image_data, img_width, img_height)
