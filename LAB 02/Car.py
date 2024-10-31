from tkinter import *

class MainGUI:
    def __init__(self):
        # Create the main window
        window = Tk()

        # Set dimensions for the canvas
        self.w = 600  # Width
        self.h = 250  # Height

        # Create a canvas for drawing
        self.canvas = Canvas(window, width=self.w, height=self.h, bg='white')

        # Bind keyboard events to increase and decrease speed
        self.canvas.bind("<Up>", self.incSpeed)
        self.canvas.bind("<Down>", self.decSpeed)

        # Pack the canvas into the window
        self.canvas.pack()

        # Load and scale the car image
        self.car = PhotoImage(file="car1.gif").zoom(2)

        # Initial x position of the car
        x = 0

        # Create the car image on the canvas
        self.canvas.create_image(x, self.h/2, image=self.car, tags="car")

        # Set focus to the canvas to capture key events
        self.canvas.focus_set()

        # Set initial speed and sleep time
        self.dx = 10  # Speed of the car
        self.sleep = 100  # Delay in milliseconds

        # Start the animation loop
        while True:
            # Move the car
            self.canvas.move("car", self.dx, 0)
            self.canvas.after(self.sleep)  # Wait before the next frame
            self.canvas.update()  # Update the canvas

            # Update x position or reset if it goes out of bounds
            if x < self.w + 65:
                x += self.dx
            else:
                x = 0  # Reset position
                self.canvas.delete("car")  # Remove old car image
                self.canvas.create_image(x, 125, image=self.car, tags="car")  # Create new car image

        # Start the Tkinter main loop
        window.mainloop()

    def incSpeed(self, event):
        # Increase the speed of the car, capped at 40
        if self.dx < 40:
            self.dx += 5

    def decSpeed(self, event):
        # Decrease the speed of the car, with a minimum speed of 5
        if self.dx > 5:
            self.dx -= 5


# Create an instance of the MainGUI class to run the application
MainGUI()
