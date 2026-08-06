import tkinter as tk
import time
from PIL import Image , ImageTk

# Main Application Window

root = tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("900x900")

#  List of Image Paths 

image_path = [
    r"C:\Users\admin\OneDrive\Pictures\cat1.jpeg",
    r"C:\Users\admin\OneDrive\Pictures\cat2.jpeg",
    r"C:\Users\admin\OneDrive\Pictures\cat3.jpeg",
    r"C:\Users\admin\OneDrive\Pictures\cat4.jpeg",
    r"C:\Users\admin\OneDrive\Pictures\cat5.jpeg",
    r"C:\Users\admin\OneDrive\Pictures\cat6.jpeg"

]

image_size = (700,700)
images = []

for path in image_path:
    img = Image.open(path)
    img = img.resize(image_size)
    images.append(img)

# convert PIL images into Tkinter compatible image

final_images = []

for img in images:
    photo  = ImageTk.PhotoImage(img)
    final_images.append(photo)

# Label widget to keep photo

image_label = tk.Label(root)
image_label.pack(pady=30)

# Slidshow Function

def start_slideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image=photo
        root.update()
        time.sleep(2)


# Button 

play_button = tk.Button (
    root,
    text=("Play the slideshow"),
    font=("Arial",17),
    command=start_slideshow
)

play_button.pack(pady=40)

root.mainloop()
