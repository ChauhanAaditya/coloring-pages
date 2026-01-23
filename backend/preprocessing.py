import cv2
import numpy as np

def generate_coloring_page(image_path, output_path):
    img = cv2.imread(image_path)

    # Resize
    h, w = img.shape[:2]
    scale = 1200 / max(h, w)
    img = cv2.resize(img, None, fx=scale, fy=scale)

    # Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Noise reduction
    blur = cv2.bilateralFilter(gray, 9, 75, 75)

    # Edge detection
    edges = cv2.Canny(blur, 50, 150)

    # Invert
    inverted = cv2.bitwise_not(edges)

    # Threshold
    _, binary = cv2.threshold(inverted, 200, 255, cv2.THRESH_BINARY)

    # Thicken lines
    kernel = np.ones((2, 2), np.uint8)
    result = cv2.dilate(binary, kernel, iterations=1)

    cv2.imwrite(output_path, result)