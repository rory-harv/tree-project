from tree import Point, Node, Rectangle, Quadtree 
from PIL import Image
import math
import numpy as np

DOWNSAMPLE_FACTOR = 4   # constant factor to downsize image
MAX_POINTS = 50000  # constant number of max pixels/points to traverse from the image
THRESHOLD_VALUE = 20    # constant factor to determine image compression against the quality of the image

def build_quadtree(image_data, x: int, y: int, width: int, height: int, threshold: int) -> Node:
    """Recursive function that looks for homogeneity within the image and returns a leaf node."""
    region = image_data[y : y + height, x : x + width] # calculate color variance (sum of squared differences from mean)

    if np.std(region, axis=(0, 1)).max() < threshold or min(width, height) <= 1: # check for a small region or homogeneous
        avg_color = np.mean(region, axis=(0, 1)).astype(int)    # gathers average color from the focused region
        return Node(Point(x, y), width, height, color = avg_color)  # returns compressed node
    else:
        half_width = width // 2
        half_height = height // 2

        # recursively check child nodes of the image data by taking calculated width and height measurements
        # width and height measurements based on regional box boundaries per node 
        children = [build_quadtree(image_data, x, y, half_width, half_height, threshold),
            build_quadtree(image_data, x + half_width, y, width - half_width, half_height, threshold),
            build_quadtree(image_data, x, y + half_height, half_width, height - half_height, threshold),
            build_quadtree(image_data, x + half_width, y + half_height, width - half_width, height - half_height, threshold)]
        return Node(Point(x, y), width, height, children = children)    # returns compressed node with its children

def reconstruct_image(node: Node, output_image_array):
    """Recurisve function that traverses nodes in the quadtree and finds the node's color."""
    if node.color is not None:  # node is a leaf node
        output_image_array[node.val.y : node.val.y + node.height, node.val.x : node.val.x + node.width] = node.color
    else:  # node is an internal node
        for child in node.children:
            reconstruct_image(child, output_image_array)


if __name__ == '__main__':
    image_path = input("Please enter an image path name: ") # ex input: "images/plants.JPG"
    try:
        img = Image.open(image_path).convert("RGB")
    except:
        raise FileNotFoundError("File path could not be found.")

    if DOWNSAMPLE_FACTOR > 1:   # downsize the image to decrease runtime
        new_size = (img.width // DOWNSAMPLE_FACTOR, img.height // DOWNSAMPLE_FACTOR)
        img = img.resize(new_size, Image.LANCZOS)

    img_np = np.array(img) # for rgb color representation
    points = img_np.reshape(-1, 3)  # reshape pixels into an nx3 array --- n points & 3 color channels

    if len(points) > MAX_POINTS:    # downsize image to decrease runtime
        indices = np.random.choice(len(points), MAX_POINTS, replace = False)
        points = points[indices]


    threshold_value = int(input("Please enter a threshold value integer (higher int value results in increased compression): "))
    root_node = build_quadtree(img_np, 0, 0, img.width, img.height, threshold_value)

    compressed_img_array = np.zeros_like(img_np)
    reconstruct_image(root_node, compressed_img_array)

    compressed_img = Image.fromarray(compressed_img_array.astype(np.uint8))
    print()
    print(f"Compressed image filepath: {image_path}_compressed.png")
    print()
    print("Thank you for using our image compressor!")
    compressed_img.save(f"{image_path}_compressed.png")     # saves compressed image