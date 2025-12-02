
from tree import Point, Node, Rectangle, Quadtree 
from PIL import Image
import math

# image compressor 

#QUAD_BOUNDARY = Rectangle(0, 0, 200, 200)   # largest boundary to contain the Quadtree
N_CAPACITY = 4      # max capacity of the Quadtree

class Pixel(object):
    """Stores information about the pixels of the image."""

    def __init__(self, color = [0, 0, 0], topLeft = Point(0, 0), bottomRight = Point(0, 0)):
        self.R = color[0]   # r-val
        self.G = color[1]   # g-val
        self.B = color[2]   # b-val
        self.topLeft = topLeft  # top left point of pixel
        self.bottomRight = bottomRight  # bottom right point of pixel


class Image(object):

    def __init__(self, image):
        self.image = image
        self.size = image.size




if __name__ == '__main__':

    image_path = ""
    img_width: int = 0
    img_height: int = 0

    try:
        image = Image.open(image_path)
        img_width, img_height = image.size
        print(f"Image {image_path} loaded successfully.")
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
    except Exception as e:
        print(f"An error occurred while opening the image: {e}")

    boundary = Rectangle(0, 0, img_width, img_height)

    quadtree = Quadtree.createQuad(boundary, N_CAPACITY, image)   # creates main quadtree object
    
