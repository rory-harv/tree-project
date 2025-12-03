from tree import Point, Node, Rectangle, Quadtree 
from PIL import Image
import math
import numpy as np

DOWNSAMPLE_FACTOR = 4   # constant factor to downsize image
MAX_POINTS = 50000  # constant number of max pixels/points to traverse from the image

# class QuadNode:
#     def __init__(self, x, y, width, height, color = None, children = None):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.color = color  # average color if leaf node
#         self.children = children  # List of 4 child QuadNodes

def build_quadtree(image_data, x, y, width, height, threshold):
    region = image_data[y : y + height, x : x + width]
    # Calculate color variance (e.g., sum of squared differences from mean)
    # For simplicity, let's assume a basic check for homogeneity
    if np.std(region) < threshold or min(width, height) <= 1: # Base case: small region or homogeneous
        avg_color = np.mean(region, axis=(0, 1)).astype(int)
        return Node(Point(x, y), width, height, color = avg_color)
    else:
        half_width = width // 2
        half_height = height // 2
        children = [build_quadtree(image_data, x, y, half_width, half_height, threshold),
            build_quadtree(image_data, x + half_width, y, width - half_width, half_height, threshold),
            build_quadtree(image_data, x, y + half_height, half_width, height - half_height, threshold),
            build_quadtree(image_data, x + half_width, y + half_height, width - half_width, height - half_height, threshold)]
        return Node(Point(x, y), width, height, children = children)

def reconstruct_image(node: Node, output_image_array):
    if node.color is not None:  # Leaf node
        output_image_array[node.val.y : node.val.y + node.height, node.val.x : node.val.x + node.width] = node.color
    else:  # Internal node
        for child in node.children:
            reconstruct_image(child, output_image_array)

# Main compression process
image_path = "src/plants.JPG"
img = Image.open(image_path).convert("RGB")

if DOWNSAMPLE_FACTOR > 1:   # downsize the image to decrease runtime
    new_size = (img.width // DOWNSAMPLE_FACTOR, img.height // DOWNSAMPLE_FACTOR)
    img = img.resize(new_size, Image.LANCZOS)

    img_np = np.array(img) / 255.0 # normalize for open3d color representation
    points = img_np.reshape(-1, 3)  # reshape pixels into an nx3 array --- n points & 3 color channels

    if len(points) > MAX_POINTS:    # downsizeimage to decrease runtime
        indices = np.random.choice(len(points), MAX_POINTS, replace = False)
        points = points[indices]

threshold_value = 20 # Adjust this for desired compression vs. quality
root_node = build_quadtree(img_np, 0, 0, img.width, img.height, threshold_value)

compressed_img_array = np.zeros_like(img_np)
reconstruct_image(root_node, compressed_img_array)

compressed_img = Image.fromarray(compressed_img_array.astype(np.uint8))
compressed_img.save("compressed_image_quadtree.png")