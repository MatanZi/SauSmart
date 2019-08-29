from tkinter import *
from PIL import Image, ImageTk

root = Tk()
# Remove titlebar    
root.overrideredirect(1)
canvas = Canvas(root, width=150, height=250)
image = Image.open("Iot - Tank volume reader.jpg")
logo = ImageTk.PhotoImage(image)
# logo=PhotoImage(file="pngs/a.jpg)
canvas.create_image(10000, 10000, image=logo)  # Change 0, 0 to whichever coordinates you need
root.mainloop()