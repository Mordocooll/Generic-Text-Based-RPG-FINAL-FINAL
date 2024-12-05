from tkinter import *
from PIL import Image, ImageTk
import subprocess

root = Tk()
root.title("Username Input with Background")
root.geometry("1920x1080")  # Adjust to fit the background image

# Background image setup
bg_image = Image.open("end screen.png")  # Replace with your image file
bg_image = bg_image.resize((1920, 1080), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Canvas for the background image
canvas = Canvas(root, width=1920, height=1080)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

end_screen_lbl = Label(text = "You save the princess and with the kings permission\n you marry her and live a happy life", font = ('', 30))
end_screen_lbl.place(x = 500, y = 600)





root.mainloop()