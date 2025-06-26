import cv2
import numpy as np
from tkinter import filedialog, Tk, Button, Label, messagebox

def load_image():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return None
    image = cv2.imread(file_path)
    return image

def save_image(image):
    if image is None:
        messagebox.showerror("Error", "No image to save.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    if file_path:
        cv2.imwrite(file_path, image)
        messagebox.showinfo("Saved", f"Image saved to {file_path}")

def apply_grayscale():
    image = load_image()
    if image is not None:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        save_image(gray)

def apply_blur():
    image = load_image()
    if image is not None:
        blurred = cv2.GaussianBlur(image, (15, 15), 0)
        save_image(blurred)

def encrypt_image(image):
    height, width = image.shape[:2]
    return image[::-1, ::-1]

def encrypt():
    image = load_image()
    if image is not None:
        encrypted = encrypt_image(image)
        save_image(encrypted)

def decrypt():
    image = load_image()
    if image is not None:
        decrypted = encrypt_image(image)
        save_image(decrypted)

# GUI
root = Tk()
root.title("Pixel Manipulator")

Label(root, text="Choose an operation:").pack(pady=5)

Button(root, text="Grayscale", command=apply_grayscale).pack(pady=2)
Button(root, text="Blur", command=apply_blur).pack(pady=2)
Button(root, text="Encrypt (Flip)", command=encrypt).pack(pady=2)
Button(root, text="Decrypt", command=decrypt).pack(pady=2)

root.mainloop()
