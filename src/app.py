"""
Interactive Edge Detection Web Application
Enhanced with creative UI, animations, and better user experience
"""

import streamlit as st
import cv2
import numpy as np
import sys
from pathlib import Path

# Import edge detection module
sys.path.append(str(Path(__file__).parent))
from edge_detection import EdgeDetector


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Edge Detection Studio",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for creative styling
st.markdown("""
    <style>
    /* Title styling with animation */
    .title-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        margin-bottom: 2rem;
        animation: fadeIn 1s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .title-text {
        color: white;
        font-size: 3em;
        font-weight: bold;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .subtitle-text {
        color: #f0f0f0;
        font-size: 1.2em;
        margin-top: 0.5rem;
    }
    
    /* Section headers */
    .section-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin: 20px 0 15px 0;
        font-size: 1.3em;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Info boxes with hover effect */
    .info-box {
        background: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 15px 0;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .info-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.2);
    }
    
    /* Progress bar */
    .progress-container {
        background: #f0f0f0;
        border-radius: 10px;
        padding: 5px;
        margin: 20px 0;
    }
    
    .progress-bar {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        height: 20px;
        border-radius: 10px;
        transition: width 0.5s ease;
    }
    </style>
""", unsafe_allow_html=True)

# Animated title
st.markdown("""
    <div class="title-container">
        <h1 class="title-text">🎨 Edge Detection Studio</h1>
        <p class="subtitle-text">Transform images with powerful edge detection algorithms</p>
    </div>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR - CREATIVE DESIGN
# ============================================================

st.sidebar.markdown('<div class="section-header">📤 Upload Your Image</div>', unsafe_allow_html=True)

uploaded_file = st.sidebar.file_uploader(
    "Drag and drop or browse",
    type=["jpg", "jpeg", "png", "bmp"],
    help="Supported: JPG, PNG, BMP • Max 5MB"
)

if uploaded_file:
    st.sidebar.success("✅ Image loaded successfully!")
    file_size = len(uploaded_file.getvalue()) / 1024
    st.sidebar.info(f"📊 File size: {file_size:.2f} KB")

st.sidebar.markdown('<div class="section-header">🎯 Choose Algorithm</div>', unsafe_allow_html=True)

# Algorithm selection with emojis
algo_options = {
    "🔷 Sobel": "Sobel",
    "🔶 Laplacian": "Laplacian",
    "🔸 Canny": "Canny"
}

selected_algo = st.sidebar.radio(
    "Select edge detection method:",
    list(algo_options.keys()),
    help="Each algorithm has unique characteristics"
)

algorithm = algo_options[selected_algo]

# Algorithm info expander
with st.sidebar.expander("ℹ️ About this algorithm"):
    if algorithm == "Sobel":
        st.write("**Fast & Efficient**")
        st.write("✓ Gradient-based detection")
        st.write("✓ Good for general use")
        st.write("✓ Adjustable direction")
    elif algorithm == "Laplacian":
        st.write("**Sensitive & Detailed**")
        st.write("✓ Second derivative method")
        st.write("✓ Finds fine edges")
        st.write("✓ Good for textures")
    else:
        st.write("**Most Accurate**")
        st.write("✓ Multi-stage process")
        st.write("✓ Precise control")
        st.write("✓ Best quality")

st.sidebar.markdown('<div class="section-header">⚙️ Adjust Parameters</div>', unsafe_allow_html=True)


# ============================================================
# PARAMETERS WITH CREATIVE CONTROLS (4 KERNEL OPTIONS)
# ============================================================

if algorithm == "Sobel":
    st.sidebar.write("🔧 **Kernel Size**")
    kernel_options = [3, 5, 7, 9]
    kernel_size = st.sidebar.select_slider(
        "Smoothing level",
        options=kernel_options,
        value=3,
        help="Larger = more smoothing"
    )
    
    st.sidebar.write("🧭 **Edge Direction**")
    direction = st.sidebar.selectbox(
        "Select direction",
        ["x", "y", "both"],
        index=2,
        help="x=vertical, y=horizontal, both=all"
    )

elif algorithm == "Laplacian":
    st.sidebar.write("🔧 **Kernel Size**")
    kernel_options = [1, 3, 5, 7]
    kernel_size = st.sidebar.select_slider(
        "Detail level",
        options=kernel_options,
        value=3,
        help="Larger = finer details"
    )

else:  # Canny
    st.sidebar.write("🎚️ **Threshold Settings**")
    
    col1, col2 = st.sidebar.columns(2)
    with col1:
        lower = st.slider(
            "Lower",
            0, 255, 50, 5,
            help="Minimum edge strength"
        )
    with col2:
        upper = st.slider(
            "Upper",
            0, 255, 150, 5,
            help="Maximum edge strength"
        )
    
    # Visual threshold indicator
    threshold_range = upper - lower
    st.sidebar.markdown(f"""
        <div class="progress-container">
            <div class="progress-bar" style="width: {(threshold_range/255)*100}%"></div>
        </div>
        <p style="text-align: center; color: #667eea; font-weight: bold;">
            Range: {threshold_range}
        </p>
    """, unsafe_allow_html=True)
    
    st.sidebar.write("🔧 **Blur Settings**")
    kernel_options = [3, 5, 7, 9]
    kernel_size = st.sidebar.select_slider(
        "Kernel size",
        options=kernel_options,
        value=3
    )
    
    sigma = st.sidebar.slider(
        "Blur intensity (Sigma)",
        0.1, 5.0, 1.0, 0.2,
        help="Higher = more blur"
    )


# ============================================================
# MAIN CONTENT - PROCESSING & DISPLAY
# ============================================================

if uploaded_file is not None:
    # Load and process image
    image_bytes = uploaded_file.read()
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Create detector
    detector = EdgeDetector(img)
    
    # Process with selected algorithm
    with st.spinner(f'🎨 Applying {algorithm} edge detection...'):
        if algorithm == "Sobel":
            edges = detector.sobel(kernel_size, direction)
        elif algorithm == "Laplacian":
            edges = detector.laplacian(kernel_size)
        else:
            edges = detector.canny(lower, upper, kernel_size, sigma)
    
    # Display results
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="section-header">📷 Original Image</div>', unsafe_allow_html=True)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        st.image(img_rgb, use_container_width=True)
    
    with col2:
        st.markdown(f'<div class="section-header">✨ {algorithm} Detected Edges</div>', unsafe_allow_html=True)
        st.image(edges, use_container_width=True, clamp=True)
    
    # Parameters summary
    st.markdown("---")
    st.markdown('<div class="section-header">📊 Current Configuration</div>', unsafe_allow_html=True)
    
    metric_cols = st.columns(4)
    
    with metric_cols[0]:
        st.metric("🎯 Algorithm", algorithm)
    
    with metric_cols[1]:
        st.metric("🔧 Kernel Size", kernel_size)
    
    if algorithm == "Sobel":
        with metric_cols[2]:
            st.metric("🧭 Direction", direction.upper())
    elif algorithm == "Canny":
        with metric_cols[2]:
            st.metric("⬇️ Lower", lower)
        with metric_cols[3]:
            st.metric("⬆️ Upper", upper)
    
    # Download button
    st.markdown("---")
    col_download = st.columns([2, 1, 2])[1]
    with col_download:
        # Convert to bytes for download
        _, buffer = cv2.imencode('.png', edges)
        st.download_button(
            label="⬇️ Download Result",
            data=buffer.tobytes(),
            file_name=f"edge_{algorithm.lower()}_{uploaded_file.name}",
            mime="image/png",
            use_container_width=True
        )

else:
    # Welcome screen
    st.markdown("""
        <div style="text-align: center; padding: 50px 20px; background: linear-gradient(135deg, #FF6B6B 0%, #4ECDC4 100%); border-radius: 15px; margin: 50px auto; max-width: 600px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
            <h2 style="color: white; margin-bottom: 30px; text-shadow: 2px 2px 4px rgba(0,0,0,0.2);">👋 Welcome to Edge Detection Studio!</h2>
            <p style="font-size: 1.2em; color: white; line-height: 2; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">
                🎨 Upload an image to get started<br>
                🔍 Choose your algorithm<br>
                ⚙️ Adjust parameters in real-time<br>
                ✨ See instant results!
            </p>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: gray; padding: 20px; font-size: 0.9em;">
        <p>🎨 Edge Detection Studio | Powered by OpenCV & Streamlit</p>
    </div>
""", unsafe_allow_html=True)