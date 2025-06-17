# Image Encryption Tool

A simple GUI-based tool built with Python to "encrypt" and "decrypt" images using a reversible image transformation.

## Features

- Load any image from your system.
- Encrypt the image by flipping it 180°.
- Decrypt the image (by flipping it again).
- Save the output image to your system.
- Simple graphical interface using Tkinter.

> ⚠️ Note: This is not real cryptographic encryption. It is a visual transformation used for learning purposes.

## How It Works

The encryption is done by flipping the image both vertically and horizontally. Applying the operation twice restores the original image.

## Technologies Used

- Python
- OpenCV (`cv2`)
- NumPy
- Tkinter (built-in)
