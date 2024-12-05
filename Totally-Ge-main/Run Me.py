from tkinter import *
from PIL import Image, ImageTk
import subprocess

def game_start():
# Launch story1.py and close runme.py window
    subprocess.Popen(["python", "story1.py"])  # Runs game.py
    root.destroy()  

#setting up window
root = Tk()
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight() 
# background image
bg_image = Image.open("castle.png") 
bg_image = bg_image.resize((screenwidth, screenheight), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create Canvas
canvas1 = Canvas(root, width=screenwidth, height=screenheight)
canvas1.pack(fill="both", expand=True)

# Display image
canvas1.create_image(0, 0, image=bg_photo, anchor="nw")

# Text
text = canvas1.create_text(screenwidth/2, screenheight/2.25, text="Generic Text Based RPG", fill="dark red", font=("Times", 30))
bbox = canvas1.bbox(text)
canvas1.create_rectangle(bbox, outline="black")

# Button that takes you to story 1
button1 = Button(root, text="Start", command=game_start)
button1_canvas = canvas1.create_window(screenwidth/2, screenheight/2, anchor="nw", window=button1)

root.mainloop()
