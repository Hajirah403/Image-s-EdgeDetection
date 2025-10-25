"""
Edge Detection Module
Contains EdgeDetector class with 3 edge detection algorithms:
- Sobel: Detects edges using gradient operators
- Laplacian: Detects edges using second derivative
- Canny: Multi-stage edge detection algorithm
"""

import cv2
import numpy as np


class EdgeDetector:
    """
    Class to perform edge detection on images using different algorithms.
    """
    
    def __init__(self, image):
        """
        Initialize EdgeDetector with an image.
        
        Args:
            image: Input image (OpenCV format - BGR)
        """
        self.image = image
        
        if len(image.shape) == 3:
            self.gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            self.gray = image
    
    
    def sobel(self, kernel_size=3, direction="both"):
        """
        Sobel edge detection algorithm.
        
        Args:
            kernel_size (int): Size of sobel kernel (3, 5, 7, 9)
            direction (str): Direction to detect edges (x, y, both)
        
        Returns:
            numpy.ndarray: Edge detected image
        """
        
        if direction == "x":
            edges = cv2.Sobel(self.gray, cv2.CV_64F, 1, 0, ksize=kernel_size)
        elif direction == "y":
            edges = cv2.Sobel(self.gray, cv2.CV_64F, 0, 1, ksize=kernel_size)
        else:
            sobel_x = cv2.Sobel(self.gray, cv2.CV_64F, 1, 0, ksize=kernel_size)
            sobel_y = cv2.Sobel(self.gray, cv2.CV_64F, 0, 1, ksize=kernel_size)
            edges = cv2.magnitude(sobel_x, sobel_y)
        
        return cv2.convertScaleAbs(edges)
    
    
    def laplacian(self, kernel_size=1):
        """
        Laplacian edge detection algorithm.
        
        Args:
            kernel_size (int): Size of Laplacian kernel (1, 3, 5, 7)
        
        Returns:
            numpy.ndarray: Edge detected image
        """
        
        edges = cv2.Laplacian(self.gray, cv2.CV_64F, ksize=kernel_size)
        return cv2.convertScaleAbs(edges)
    
    
    def canny(self, lower_threshold=50, upper_threshold=150, 
              kernel_size=3, sigma=1.0):
        """
        Canny edge detection algorithm.
        
        Args:
            lower_threshold (int): Lower threshold (0-255)
            upper_threshold (int): Upper threshold (0-255)
            kernel_size (int): Gaussian blur kernel size (3, 5, 7, 9)
            sigma (float): Gaussian blur intensity (0.1-5.0)
        
        Returns:
            numpy.ndarray: Edge detected image
        """
        
        blurred = cv2.GaussianBlur(self.gray, (kernel_size, kernel_size), sigma)
        edges = cv2.Canny(blurred, lower_threshold, upper_threshold)
        
        return edges