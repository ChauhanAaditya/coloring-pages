# 🎨 Image to Coloring Sheet Web App

A free and open-source web application that converts uploaded images into clean, printable coloring sheets using computer vision techniques.

Users can upload any photo and instantly receive a black-and-white line-art version suitable for coloring and printing.

---

## ✨ Features

- Upload an image and generate a coloring sheet
- Clean outline extraction using OpenCV
- Noise reduction and line thickening for better coloring experience
- Print-friendly black & white output
- Fully offline image processing
- Simple web-based interface
- Free and open source

---

## 🧠 How It Works

The application processes images using a computer vision pipeline:

1. Image upload via browser
2. Resize and normalize image
3. Convert to grayscale
4. Noise reduction using bilateral filtering
5. Edge detection (Canny)
6. Invert colors for white background
7. Thresholding to remove gray artifacts
8. Morphological operations to thicken lines
9. Output as a coloring sheet image

---

## 🛠️ Tech Stack

**Backend**
- Python
- FastAPI
- OpenCV
- NumPy

**Frontend**
- HTML
- CSS
- JavaScript

---

## 📁 Project Structure

