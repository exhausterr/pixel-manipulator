import cv2
import numpy as np 
from tkinter import filedialog, Tk, Button, Label

def encrypt_image(image):
    height, width, _ = image.shape
    encrypted_image = np.copy(image)
    for i in range(height):
        for j in range(width):
            encrypted_image[i, j] = image[height - 1 - i, width - 1 - j]
    return encrypted_image

def decrypt_image(image):
    return encrypt_image(image)

def load_image():
    file_path  = filedialog.askopenfilename()
    image = cv2.imread(file_path)
    return image  

def save_image(image):
    file_path = filedialog.asksaveasfilename(defaultextension=".png")
    cv2.imwrite(file_path, image) 

def encrypt():
    image = load_image()
    encrypted = encrypt_image(image)
    save_image(encrypted)

def decrypt():
    image = load_image()
    decrypted = decrypt_image(image)
    save_image(decrypted)


root = Tk()
root.title("Image Encryption Tool")

encrypt_button = Button(root, text="Encrypt image", command=encrypt)
encrypt_button.pack()

decrypt_button = Button(root, text="Decrypt Image", command=decrypt)
decrypt_button.pack()

label = Label(root, text="Select and image to encrypt or decrypt.")
label.pack()

root.mainloop()
