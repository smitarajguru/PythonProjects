from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

image_paths = [
    r"C:\Users\SMITA\OneDrive\Pictures\krishna\lord-krishna-new.jpg",
    r"C:\Users\SMITA\OneDrive\Pictures\krishna\c60dbcd73a453bb286c99817b3f1310f.jpg",
    r"C:\Users\SMITA\OneDrive\Pictures\krishna\628f5d4b4ef2fab3fcd43e3710343302.jpg"
]

image_size = (1080, 1080)

images = [
    Image.open(path).resize(image_size)
    for path in image_paths
]

photo_images = [
    ImageTk.PhotoImage(image)
    for image in images
]

label = tk.Label(root)
label.pack()

slideshow = cycle(photo_images)


def start_slideshow():
    for _ in range(len(photo_images)):
        photo_image = next(slideshow)
        label.config(image=photo_image)
        root.update()
        root.after(3000)


play_button = tk.Button(
    root,
    text="Play Slideshow",
    command=start_slideshow
)

play_button.pack()

root.mainloop()