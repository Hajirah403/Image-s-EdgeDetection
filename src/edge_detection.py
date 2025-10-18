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
        
        # Convert to grayscale (edge detection requires grayscale)
        if len(image.shape) == 3:
            # If colored image, convert BGR to grayscale
            self.gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            # If already grayscale, use as is
            self.gray = image
    
    
    def sobel(self, kernel_size=3, direction="both"):
        """
        Sobel edge detection algorithm.
        Uses gradient operators to find edges in the image.
        
        Args:
            kernel_size (int): Size of sobel kernel (3, 5, or 7)
            direction (str): Direction to detect edges
                - "x": Vertical edges only
                - "y": Horizontal edges only  
                - "both": All edges (combines x and y)
        
        Returns:
            numpy.ndarray: Edge detected image (grayscale)
        """
        
        if direction == "x":
            # Detect vertical edges (changes in X direction)
            edges = cv2.Sobel(self.gray, cv2.CV_64F, 1, 0, ksize=kernel_size)
        
        elif direction == "y":
            # Detect horizontal edges (changes in Y direction)
            edges = cv2.Sobel(self.gray, cv2.CV_64F, 0, 1, ksize=kernel_size)
        
        else:  # direction == "both"
            # Detect all edges by combining X and Y gradients
            sobel_x = cv2.Sobel(self.gray, cv2.CV_64F, 1, 0, ksize=kernel_size)
            sobel_y = cv2.Sobel(self.gray, cv2.CV_64F, 0, 1, ksize=kernel_size)
            # Calculate magnitude (combines both gradients)
            edges = cv2.magnitude(sobel_x, sobel_y)
        
        # Convert to displayable format (0-255)
        return cv2.convertScaleAbs(edges)
    
    
    def laplacian(self, kernel_size=1):
        """
        Laplacian edge detection algorithm.
        Uses second derivative to find edges. More sensitive than Sobel.
        
        Args:
            kernel_size (int): Size of Laplacian kernel (1, 3, or 5)
        
        Returns:
            numpy.ndarray: Edge detected image (grayscale)
        """
        
        # Apply Laplacian operator
        edges = cv2.Laplacian(self.gray, cv2.CV_64F, ksize=kernel_size)
        
        # Convert to displayable format (0-255)
        return cv2.convertScaleAbs(edges)
    
    
    def canny(self, lower_threshold=50, upper_threshold=150, 
              kernel_size=3, sigma=1.0):
        """
        Canny edge detection algorithm.
        Multi-stage algorithm: blur → gradient → non-max suppression → threshold
        
        Args:
            lower_threshold (int): Lower threshold (0-255)
                Edges weaker than this are discarded
            upper_threshold (int): Upper threshold (0-255)
                Edges stronger than this are kept
            kernel_size (int): Gaussian blur kernel size (3, 5, or 7)
            sigma (float): Gaussian blur intensity (0.1-3.0)
        
        Returns:
            numpy.ndarray: Edge detected image (binary - black and white)
        """
        
        # Step 1: Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(self.gray, (kernel_size, kernel_size), sigma)
        
        # Step 2: Apply Canny edge detection with thresholds
        edges = cv2.Canny(blurred, lower_threshold, upper_threshold)
        
        return edges