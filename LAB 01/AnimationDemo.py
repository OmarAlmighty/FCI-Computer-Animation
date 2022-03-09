from tkinter import *

window = Tk()
window.title("Animation Demo")

width = 250
cnvs = Canvas(window, bg="white", width = width, height=200)
cnvs.pack()

x = 0
y = 100
cnvs.create_text(x, y, text="Message moving", tags="text")

dx = 3
while True:
    cnvs.move("text", dx, 0)
    cnvs.after(100)
    cnvs.update()
    if x < width:
        x += dx
    else:
        x = 0
        cnvs.delete("text")
        cnvs.create_text(x, y, text= "Message moving", tags="text")

window.mainloop()