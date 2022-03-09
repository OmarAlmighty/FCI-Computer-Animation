from tkinter import *

class ControlAnimation:
    def __init__(self):
        window = Tk()
        window.title("Control Animation Demo")
        self.width = 250
        self.height = 50
        self.canvas = Canvas(window, bg="white", width=self.width, height=self.height) #bg="black"
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        bt_stop = Button(frame, text="Stop", command=self.stop)
        bt_stop.pack(side=LEFT)

        bt_resume = Button(frame, text="Resume", command=self.resume)
        bt_resume.pack(side=LEFT)

        bt_faster = Button(frame, text="Faster", command=self.faster)
        bt_faster.pack(side=LEFT)

        bt_slower = Button(frame, text="Slower", command=self.slower)
        bt_slower.pack(side=LEFT)

        self.x = 0
        self.sleepTime = 100
        self.canvas.create_text(self.x, 30, text="Message Moving?", tags="text") #fill="white"

        self.dx = 3
        self.isStop = False
        self.animate()

        window.mainloop()
    def stop(self):
        self.isStop = True
    def resume(self):
        self.isStop = False
        self.animate()
    def faster(self):
        if self.sleepTime > 5:
            self.sleepTime -= 20
    def slower(self):
        self.sleepTime += 20
    def animate(self):
        while not self.isStop:
            self.canvas.move("text", self.dx, 0)
            self.canvas.after(self.sleepTime)
            self.canvas.update()
            if self.x < self.width:
                self.x += self.dx
            else:
                self.x = 0
                self.canvas.delete("text")
                self.canvas.create_text(self.x, 30, text="Message Moving?", tags="text")

ControlAnimation()