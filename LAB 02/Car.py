from tkinter import *


class MainGUI:
    def __init__(self):
        window = Tk()
        self.canvas = Canvas(window, width=600, height=250, bg="white")
        self.canvas.bind("<Up>", self.incSpeed)
        self.canvas.bind("<Down>", self.decSpeed)
        self.canvas.pack()
        self.car = PhotoImage(file="car1.gif")
        self.car = self.car.zoom(2)  # with 250, I ended up running out of memory
        # self.car = self.car.subsample(60) #mechanically, here it is adjusted to 32 instead of 320
        x = 0
        self.canvas.create_image(x, 125, image=self.car, tags="car")
        self.canvas.focus_set()
        self.dx = 10
        while True:
            self.canvas.move("car", self.dx, 0)
            self.canvas.after(100)
            self.canvas.update()
            if x < 600 + 65:
                x += self.dx
            else:
                x = 0
                self.canvas.delete("car")
                self.canvas.create_image(x, 125, image=self.car, tags="car")

        window.mainloop()

    def incSpeed(self, event):
        if self.dx < 40:
            self.dx += 5

    def decSpeed(self, event):
        if self.dx > 5:
            self.dx -= 5


MainGUI()
