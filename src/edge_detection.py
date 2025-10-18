import cv2
import numpy as np

class EdgeDetector:
    def __init__(self, image):
        self.image = image
        # Convert to grayscale
        if len(image.shape) == 3:
            self.gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            self.gray = image
    
    # Sobel edge detection
    def sobel(self, kernel_size=3, direction="both"):
        if direction == "x":
            edges = cv2.Sobel(self.gray, cv2.CV_64F, 1, 0, ksize=kernel_size)
        elif direction == "y":
            edges = cv2.Sobel(self.gray, cv2.CV_64F, 0, 1, ksize=kernel_size)
        else:  # both
            sobel_x = cv2.Sobel(self.gray, cv2.CV_64F, 1, 0, ksize=kernel_size)
            sobel_y = cv2.Sobel(self.gray, cv2.CV_64F, 0, 1, ksize=kernel_size)
            edges = cv2.magnitude(sobel_x, sobel_y)
        return cv2.convertScaleAbs(edges)
    
    # Laplacian edge detection
    def laplacian(self, kernel_size=1):
        edges = cv2.Laplacian(self.gray, cv2.CV_64F, ksize=kernel_size)
        return cv2.convertScaleAbs(edges)
    
    # Canny edge detection
    def canny(self, lower_threshold=50, upper_threshold=150, 
              kernel_size=3, sigma=1.0):
        blurred = cv2.GaussianBlur(self.gray, (kernel_size, kernel_size), sigma)
        edges = cv2.Canny(blurred, lower_threshold, upper_threshold)
        return edges