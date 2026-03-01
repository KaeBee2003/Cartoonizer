import cv2
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def read_img(filename):
    img = cv2.imread(filename)
    return img

def color_quantisation(img, k):
    data = np.float32(img).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)
    _, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    result = center[label.flatten()]
    result = result.reshape(img.shape)
    return result

def cartoonize_image():
    # Get file path and color count
    filepath = file_path.get()
    if not filepath:
        messagebox.showwarning("Input Error", "Please select an image file.")
        return
    
    try:
        k = int(color_count.get())
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid integer for colors.")
        return

    # Read and process image
    img = read_img(filepath)
    cartoon = color_quantisation(img, k)
    
    # Save as PNG
    output_path = os.path.splitext(filepath)[0] + "_cartoon.png"
    cv2.imwrite(output_path, cartoon)
    
    messagebox.showinfo("Done", f"Cartoonized image saved at: {output_path}")

def select_file():
    filename = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if filename:
        file_path.set(filename)

# Set up the UI
root = tk.Tk()
root.title("Image Cartoonizer")

# File selection
file_path = tk.StringVar()
tk.Label(root, text="Select Image:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=file_path, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_file).grid(row=0, column=2, padx=10, pady=10)

# Color count selection
tk.Label(root, text="Total Colors:").grid(row=1, column=0, padx=10, pady=10)
color_count = tk.StringVar(value="15")
tk.Entry(root, textvariable=color_count, width=10).grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Start button
tk.Button(root, text="Start Cartoonize", command=cartoonize_image).grid(row=2, column=0, columnspan=3, pady=20)

root.mainloop()
