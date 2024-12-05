from tkinter import *
from PIL import Image, ImageTk
import subprocess

#window setup
root = Tk()
root.title("Username Input with Background")
root.geometry("1920x1080")  

# Background image setup
bg_image = Image.open("file.png")  
bg_image = bg_image.resize((1920, 1080), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

# Canvas for the background image
canvas = Canvas(root, width=1920, height=1080)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")


# This will add windows to the list of frames
frames = []

#This function clears the windows in the frame to open up new frames
def clearFrames():
    #for every element that is added to the frame
    for elements in frames:
        #delete all the elements in the frame
        canvas.delete(elements)
    #it is now an empty list
    frames.clear()

def fight3():
# Launch monster fight 4.py and close the current window
    subprocess.Popen(["python", "monster fight Boss.py"])  # Runs game.py
    root.destroy()  # Close the meny.py window


def open_frame9():
    clearFrames()
   
    global text8  
    
    
    theNext8= Button(root, text="Next", font=("Times", 15), command=fight3)
    theNextWindow8 = canvas.create_window(950, 950, anchor="nw", window=theNext8)
    
    
    frames.append(theNextWindow8)
   
    story8 = [
                "You escape and the goblins lead you to the cave’s exit, staring as you leave toward the castle,",
"Night falls as you reflect on your exhausting journey, but you press on,",
"Finally reaching the castle's base, you find survivors who cheer your arrival,",
"They believe only you can slay the dragon and save the princess,",
"Gathering supplies, you prepare for the final battle,",
"Inside the castle, the dragon awakens as you draw your sword,",
"The moment is now; it's time to slay the dragon,",
                ]
    
    textDisplay = "\n".join(story8)
    text8 = canvas.create_text(675, 475,text=textDisplay, anchor="center", font=("Times", 22), fill="white")
    frames.append(text8)    
    
    




open_frame9()
root.mainloop()
