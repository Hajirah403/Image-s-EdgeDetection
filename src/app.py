"""
Interactive Edge Detection Web Application
Built with Streamlit for visual experimentation with edge detection algorithms.

Features:
- Upload and display images (JPG, PNG, BMP)
- Real-time edge detection with 3 algorithms
- Adjustable parameters for each algorithm
- Side-by-side display of input and output
"""

import streamlit as st
import cv2
import numpy as np
import sys
from pathlib import Path

# Import our edge detection module
sys.path.append(str(Path(__file__).parent))
from edge_detection import EdgeDetector


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Edge Detection Pro",
    page_icon="🔍",
    layout="wide"
)

# Page title
st.title("🔍 Interactive Edge Detection UI")


# ============================================================
# SIDEBAR - UPLOAD IMAGE
# ============================================================

st.sidebar.header("📤 Upload Image")
uploaded_file = st.sidebar.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png", "bmp"],
    help="Supported formats: JPG, PNG, BMP"
)


# ============================================================
# SIDEBAR - ALGORITHM SELECTION
# ============================================================

st.sidebar.header("🎯 Select Algorithm")
algorithm = st.sidebar.radio(
    "Choose an algorithm:",
    ["Sobel", "Laplacian", "Canny"],
    help="Different algorithms detect edges differently"
)


# ============================================================
# SIDEBAR - ALGORITHM PARAMETERS
# ============================================================

st.sidebar.header("⚙️ Parameters")

# Sobel parameters
if algorithm == "Sobel":
    kernel = st.sidebar.slider("Kernel Size", 1, 3, 1, help="Affects edge sensitivity")
    kernel_size = kernel * 2 + 1  # Convert 1,2,3 to 3,5,7
    
    direction = st.sidebar.selectbox(
        "Edge Direction",
        ["x", "y", "both"],
        help="x=vertical edges, y=horizontal edges, both=all edges"
    )

# Laplacian parameters
elif algorithm == "Laplacian":
    kernel = st.sidebar.slider("Kernel Size", 1, 3, 1)
    kernel_size = kernel * 2 - 1 if kernel > 1 else 1  # Convert 1,2,3 to 1,3,5

# Canny parameters
elif algorithm == "Canny":
    lower = st.sidebar.slider("Lower Threshold", 0, 255, 50, 
                              help="Edges below this are discarded")
    upper = st.sidebar.slider("Upper Threshold", 0, 255, 150,
                              help="Edges above this are kept")
    kernel = st.sidebar.slider("Kernel Size", 1, 3, 1)
    kernel_size = kernel * 2 + 1
    sigma = st.sidebar.slider("Sigma", 0.1, 3.0, 1.0, step=0.1,
                             help="Blur intensity")


# ============================================================
# MAIN CONTENT - PROCESS AND DISPLAY
# ============================================================

if uploaded_file is not None:
    # Load image from uploaded file
    image_bytes = uploaded_file.read()
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Create EdgeDetector object
    detector = EdgeDetector(img)
    
    # Apply selected algorithm with current parameters
    if algorithm == "Sobel":
        edges = detector.sobel(kernel_size, direction)
    elif algorithm == "Laplacian":
        edges = detector.laplacian(kernel_size)
    else:  # Canny
        edges = detector.canny(lower, upper, kernel_size, sigma)
    
    
    # Display input and output side-by-side
    col1, col2 = st.columns(2)
    
    # Left column: Original image
    with col1:
        st.subheader("📷 Input Image")
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        st.image(img_rgb, use_column_width=True)
        
        # Show image information
        height, width = img.shape[:2]
        st.info(f"Size: {width}×{height} px | Format: {uploaded_file.name.split('.')[-1].upper()}")
    
    # Right column: Edge detected image
    with col2:
        st.subheader(f"✨ Output - {algorithm} Detection")
        st.image(edges, use_column_width=True, clamp=True)
        
        # Show edge detection statistics
        edge_pixels = np.count_nonzero(edges)
        total_pixels = edges.shape[0] * edges.shape[1]
        percentage = (edge_pixels / total_pixels) * 100
        st.success(f"Edges Detected: {percentage:.1f}% of image")

else:
    # Welcome message when no image uploaded
    st.info("👈 Upload an image to get started")