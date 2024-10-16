from tkinter import *

# Create the main window
window = Tk()
window.title("BouncingBall")
width = 400
height = 300

# Create a canvas
cnvs = Canvas(window, bg="white", width=width, height=height)
cnvs.pack()

# Create a circle
circle_radius = 20
x = circle_radius
y = height // 2

dx = 2  # Change in x (speed)
dy = 2  # Change in y

# Draw the circle
circle = cnvs.create_oval(x - circle_radius, y - circle_radius,
                          x + circle_radius, y + circle_radius,
                          fill="blue")


def animate():
    global x, dx, y, dy
    # Move the circle
    cnvs.move(circle, dx, dy)
    x += dx
    y += dy

    # Bounce off the edges
    if x + circle_radius >= width or x - circle_radius <= 0:
        dx = -dx  # Reverse direction

    # Bounce off the edges
    if y + circle_radius >= height or y - circle_radius <= 0:
        dy = -dy  # Reverse direction

    # Schedule the next frame
    window.after(20, animate)


# Start the animation
animate()

# Start the Tkinter event loop
window.mainloop()
