import streamlit as st
import cv2
import numpy as np
from PIL import Image
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
from edge_detection import EdgeDetector

# Page config
st.set_page_config(page_title="Edge Detection", layout="wide")

st.title("🔍 Interactive Edge Detection UI")

# Sidebar for controls
with st.sidebar:
    st.header("Upload Image")
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png", "bmp"])
    
    st.header("Algorithm")
    algorithm = st.radio("Select Algorithm:", ["Sobel", "Laplacian", "Canny"])
    
    st.header("Parameters")
    
    if algorithm == "Sobel":
        kernel = st.slider("Kernel Size:", 1, 3, 1)
        kernel_size = kernel * 2 + 1
        direction = st.selectbox("Direction:", ["x", "y", "both"])
    
    elif algorithm == "Laplacian":
        kernel = st.slider("Kernel Size:", 1, 3, 1)
        kernel_size = kernel * 2 - 1 if kernel > 1 else 1
    
    elif algorithm == "Canny":
        lower = st.slider("Lower Threshold:", 0, 255, 50)
        upper = st.slider("Upper Threshold:", 0, 255, 150)
        kernel = st.slider("Kernel Size:", 1, 3, 1)
        kernel_size = kernel * 2 + 1
        sigma = st.slider("Sigma:", 0.1, 3.0, 1.0)

# Main content
if uploaded_file is not None:
    # Load image
    image_bytes = uploaded_file.read()
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Create detector
    detector = EdgeDetector(img)
    
    # Process based on algorithm
    if algorithm == "Sobel":
        edges = detector.sobel(kernel_size, direction)
    elif algorithm == "Laplacian":
        edges = detector.laplacian(kernel_size)
    else:  # Canny
        edges = detector.canny(lower, upper, kernel_size, sigma)
    
    # Display side-by-side
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Input Image")
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        st.image(img_rgb, use_column_width=True)
    
    with col2:
        st.subheader(f"Output - {algorithm}")
        st.image(edges, use_column_width=True)

else:
    st.info("👈 Upload an image to start")