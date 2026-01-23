import cv2
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def generate_coloring_page(input_path, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    img = cv2.imread(input_path)
    if img is None:
        raise ValueError(f"Could not read input image: {input_path}")

    # Resize
    h, w = img.shape[:2]
    scale = 1200 / max(h, w)
    img = cv2.resize(img, None, fx=scale, fy=scale)

    # Grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Light blur
    blur = cv2.GaussianBlur(gray, (15, 15), 0)

    # Edge detection
    edges = cv2.Canny(blur, 20, 50)

    # 🔑 THICKEN EDGES FIRST (edges are white here)
    kernel = np.ones((2, 2), np.uint8)
    thick_edges = cv2.dilate(edges, kernel, iterations=1)

    # 🔑 NOW invert → black lines on white
    coloring_page = cv2.bitwise_not(thick_edges)

    success = cv2.imwrite(output_path, coloring_page)
    if not success:
        raise RuntimeError("Failed to save output image")

    return output_path


if __name__ == "__main__":
    input_image = os.path.join(BASE_DIR, "test_input", "sample.jpg")
    output_image = os.path.join(BASE_DIR, "test_output", "coloring.png")

    generate_coloring_page(input_image, output_image)
    print("Coloring page generated at:", output_image)
