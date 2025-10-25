# 🎨 Interactive Edge Detection Studio

A professional web application for visual experimentation with edge detection algorithms: Sobel, Laplacian, and Canny.

## ✨ Features

- 📤 **Upload images** (JPG, PNG, BMP formats)
- 🎯 **Three edge detection algorithms** with real-time parameter adjustment
- 🖼️ **Side-by-side display** of original and processed images
- 📊 **Current configuration display** showing active parameters
- ⬇️ **Download results** as PNG files
- 🎨 **Modern, animated UI** with gradient designs
- ⚡ **Real-time processing** with instant visual feedback


## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/Hajirah403/Image-s-EdgeDetection.git
cd Image-s-EdgeDetection
```

### 2. Create virtual environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🎮 How to Run

```bash
streamlit run src/app.py
```

The application will open automatically in your browser at `http://localhost:8501`

---

## 📖 How to Use

1. **Upload an image** - Click "Browse files" in the sidebar or drag & drop
2. **Select algorithm** - Choose from Sobel, Laplacian, or Canny
3. **Adjust parameters** - Use sliders and controls to fine-tune detection
4. **View results** - Compare original and edge-detected images side-by-side
5. **Download** - Save the processed image using the download button

---

## 🔬 Algorithms

### 🔷 Sobel Edge Detection
Detects edges using gradient operators (first derivative method)

**Parameters:**
- **Kernel Size**: `3, 5, 7, 9` (larger = more smoothing)
- **Direction**: `x`, `y`, or `both` (edge orientation)

**Best for:** General-purpose edge detection, gradient analysis

---

### 🔶 Laplacian Edge Detection
Uses second derivative to find edges with high sensitivity

**Parameters:**
- **Kernel Size**: `1, 3, 5, 7` (larger = finer details)

**Best for:** Fine textures, detailed edges, blob detection

---

### 🔸 Canny Edge Detection
Multi-stage algorithm with Gaussian blur and double thresholding

**Parameters:**
- **Lower Threshold**: `0-255` (minimum edge strength)
- **Upper Threshold**: `0-255` (maximum edge strength)
- **Kernel Size**: `3, 5, 7, 9` (Gaussian blur kernel)
- **Sigma**: `0.1-5.0` (blur intensity)

**Best for:** Most accurate edge detection, precise control

---

## 📁 Project Structure

```
Image-s-EdgeDetection/
├── src/
│   ├── app.py                    # Streamlit web interface
│   └── edge_detection.py         # Edge detection algorithms
├── screenshots/                   # Application screenshots
│   ├── welcome.png
│   ├── sobel.png
│   ├── laplacian.png
│   └── canny.png
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git ignore configuration
└── README.md                     # Documentation (this file)
```

---

## 💻 Code Overview

### `edge_detection.py`
Contains the `EdgeDetector` class with three main methods:

- **`sobel(kernel_size, direction)`** - Sobel edge detection
- **`laplacian(kernel_size)`** - Laplacian edge detection
- **`canny(lower, upper, kernel_size, sigma)`** - Canny edge detection

Each method is well-documented with parameters and return values.

### `app.py`
Streamlit web interface featuring:

- 🎨 Animated gradient UI with modern design
- 📊 Real-time parameter controls
- 🖼️ Side-by-side image comparison
- 📈 Configuration metrics display
- ⬇️ Download functionality for processed images

---

## 📋 Requirements

- **Python**: 3.9 or higher
- **opencv-python**: 4.8.1.78
- **numpy**: 1.24.3
- **streamlit**: 1.28.1
- **pillow**: 10.0.0

All dependencies are listed in `requirements.txt`
