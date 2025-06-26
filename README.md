# 🖼️ Pixel Manipulator

A simple GUI-based tool built with Python that allows users to apply basic image effects and a reversible "encryption" using pixel transformations. Great for learning OpenCV and GUI development with Tkinter.

## ✨ Features

- 📂 Load any image from your system
- 🌑 Convert image to **Grayscale**
- 💨 Apply **Gaussian Blur** effect
- 🔄 **Encrypt** image by flipping pixels (visually distorts image)
- ⏪ **Decrypt** by flipping again (restores original)
- 💾 Save the processed image using a file dialog
- 🧠 Educational GUI made with Tkinter

> ⚠️ **Note:** The "encryption" here is purely visual and reversible — not secure or cryptographic. It's designed for learning purposes only.

---

## 🧠 How It Works

- **Grayscale:** Converts the image to black and white using OpenCV.
- **Blur:** Applies a softening Gaussian blur filter.
- **Encrypt (Flip):** Flips image both vertically and horizontally.
- **Decrypt:** Applies the same flip operation again to reverse it.

---

## 🛠️ Technologies Used

- Python 3
- [OpenCV (cv2)](https://opencv.org/)
- NumPy
- Tkinter (built-in Python GUI library)

---
