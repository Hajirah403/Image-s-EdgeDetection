# Interactive Edge Detection Studio

A web application for visual experimentation with edge detection algorithms: Sobel, Laplacian, and Canny. Built with Streamlit and OpenCV.

## Features

- Upload images (JPG, PNG, BMP formats)
- Three edge detection algorithms with real-time parameter adjustment
- Side-by-side display of original and processed images
- Current configuration display showing active parameters
- Download processed results as PNG files
- Real-time processing with instant visual feedback

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/Hajirah403/Image-s-EdgeDetection.git
cd Image-s-EdgeDetection
```

### 2. Create a virtual environment
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Running the Application

```bash
streamlit run src/app.py
```

The application opens automatically in your browser at `http://localhost:8501`.

## Usage

1. Upload an image via the sidebar
2. Select an algorithm: Sobel, Laplacian, or Canny
3. Adjust parameters using the provided sliders and controls
4. Compare the original and processed images side-by-side
5. Download the processed image if needed

## Algorithms

### Sobel Edge Detection
Detects edges using gradient operators (first derivative method).

**Parameters:**
- Kernel Size: 3, 5, 7, 9 (larger = more smoothing)
- Direction: x, y, or both (edge orientation)

Best for general-purpose edge detection and gradient analysis.

### Laplacian Edge Detection
Uses second derivative methods to detect edges with high sensitivity.

**Parameters:**
- Kernel Size: 1, 3, 5, 7 (larger = finer detail)

Best for fine textures, detailed edges, and blob detection.

### Canny Edge Detection
A multi-stage algorithm combining Gaussian blur and double thresholding.

**Parameters:**
- Lower Threshold: 0–255 (minimum edge strength)
- Upper Threshold: 0–255 (maximum edge strength)
- Kernel Size: 3, 5, 7, 9 (Gaussian blur kernel)
- Sigma: 0.1–5.0 (blur intensity)

Best for precise, accurate edge detection with fine control.

## Project Structure
Image-s-EdgeDetection/
├── src/
│ ├── app.py # Streamlit web interface
│ └── edge_detection.py # Edge detection algorithms
├── screenshots/
│ ├── welcome.png
│ ├── sobel.png
│ ├── laplacian.png
│ └── canny.png
├── requirements.txt
├── .gitignore
└── README.md


## Code Overview

**edge_detection.py** contains the `EdgeDetector` class with three core methods:
- `sobel(kernel_size, direction)` — Sobel edge detection
- `laplacian(kernel_size)` — Laplacian edge detection
- `canny(lower, upper, kernel_size, sigma)` — Canny edge detection

**app.py** implements the Streamlit interface, including real-time parameter controls, side-by-side image comparison, configuration display, and download functionality.

## Requirements

- Python 3.9 or higher
- opencv-python 4.8.1.78
- numpy 1.24.3
- streamlit 1.28.1
- pillow 10.0.0

All dependencies are listed in `requirements.txt`.
