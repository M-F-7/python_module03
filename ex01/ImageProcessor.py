import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class ImageProcessor:
    def __init__(self):
        pass

    def load(self, path):
        try:
            with Image.open(path) as img:
                img = img.convert('RGB')
                width, height = img.size
                rgb_values = []
                rgb_values = [img.getpixel((x, y)) for y in range(height) for x in range(width)]
                print(f"Loading image of dimensions {width} * {height}")
                tab_rgb_norm = np.array(rgb_values, dtype=np.float32) / 255.0
                return tab_rgb_norm
            
            if self.__img == None:
                raise FileNotFoundError("No such file or directory")
        except FileNotFoundError as e:
            print(f"Exception: FileNotFoundError {e}")     

    def display(self, array):
        # mlt.

