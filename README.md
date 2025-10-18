
# Interactive Edge Detection UI

A web application for visual experimentation with edge detection algorithms: Sobel, Laplacian, and Canny.

---

## Features

- Upload images (JPG, PNG, BMP)
- Three edge detection algorithms with real-time parameter adjustment
- Side-by-side display of original and processed images
- Image statistics and edge detection metrics
- Professional Streamlit web interface

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Hajirah403/Image-s-EdgeDetection.git
cd EdgeDetectionProject
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/Scripts/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## How to Run

```bash
streamlit run src/app.py
```

Open your browser at `http://localhost:8501`

---

## How to Use

1. Upload an image from the sidebar
2. Select an edge detection algorithm (Sobel, Laplacian, or Canny)
3. Adjust parameters with sliders to see real-time changes
4. Compare original and processed images side-by-side

---

## Algorithms

**Sobel Edge Detection**
- Detects edges using gradient operators
- Parameters: Kernel size (3, 5, 7, 9, 11, 13) and direction (x, y, both)

**Laplacian Edge Detection**
- Uses second derivative to find edges
- Parameter: Kernel size (1, 3, 5, 7, 9, 11)

**Canny Edge Detection**
- Multi-stage algorithm with Gaussian blur and thresholding
- Parameters: Lower threshold, upper threshold, kernel size, sigma

---

## Project Structure

```
EdgeDetectionProject/
├── src/
│   ├── app.py                    # Streamlit web interface
│   └── edge_detection.py         # Edge detection algorithms
├── requirements.txt              # Dependencies
├── .gitignore                    # Git configuration
└── README.md                     # This file
```

---

## Code Files

**edge_detection.py**
- EdgeDetector class with sobel(), laplacian(), and canny() methods
- Each method well-documented with parameters and return values

**app.py**
- Streamlit interface with image upload
- Real-time algorithm processing
- Parameter controls with sliders and dropdowns
- Side-by-side image display with statistics

---

## Requirements

- Python 3.9+
- opencv-python 4.8.1.78
- numpy 1.24.3
- streamlit 1.28.1
- pillow 10.0.0

---

