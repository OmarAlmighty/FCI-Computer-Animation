from random import randrange
from tkinter import *
#from winsound import *

# Create the main window
window = Tk()

# Create a canvas for drawing
cnvs = Canvas(window, width=600, height=600)
cnvs.pack()

# Initial parameters for the circles
cx = 300  # Center x-coordinate
cy = 300  # Center y-coordinate
r = 20  # Initial radius
stroke_size = 20  # Initial stroke size
counter = 0  # Counter for the loop

# Loop to create animated circles
while counter < 180:
    # Generate a random fill color
    fill_color = '#%02x%02x%02x' % (randrange(256), randrange(256), randrange(256))

    # Draw the circle on the canvas
    cnvs.create_oval(cx - r, cy - r, cx + r, cy + r, fill=fill_color, width=stroke_size, tags="c")

    # Update the canvas and wait briefly
    cnvs.after(50)
    cnvs.update()

    # Increase the radius and decrease the stroke size
    r += 2
    stroke_size -= 0.09

    # Delete the previous circle
    cnvs.delete("c")

    # Increment the counter
    counter += 1

# Load frames for the GIF animation
frame_count = 20
frames = [PhotoImage(file="exp.gif", format="gif -index %i" % i) for i in range(frame_count)]


def update(ind):
    # Update the displayed frame for the GIF
    frame = frames[ind]
    ind += 1
    if ind == frame_count:
        ind = 0  # Loop back to the first frame

    # Play sound asynchronously
    #PlaySound("exp_snd.wav", SND_ASYNC)

    # Update the label with the new frame
    label.configure(image=frame)

    # Schedule the next update
    window.after(100, update, ind)


# Create a label to display the GIF
label = Label(window)
label.place(x=200, y=200)

# Start the GIF animation
window.after(0, update, 0)

# Run the main loop
window.mainloop()
