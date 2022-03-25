from random import randrange
from tkinter import *
from winsound import *

window = Tk()
cnvs = Canvas(window, width=600, height=600)
cnvs.pack()

cx = 300; cy = 300; x0 = 20; y0 = 20; x1 = 20; y1 = 20

counter = 0
while counter < 180:
    fill_color = '#%02x%02x%02x' % (randrange(256), randrange(256), randrange(256))
    cnvs.create_oval(cx - x0, cy - y0, cx + x1, cy + y1, fill=fill_color, width=20, tags="c")
    cnvs.after(10)
    cnvs.update()
    fill_color = '#%02x%02x%02x' % (randrange(256), randrange(256), randrange(256))
    x0 += 2; y0 += 2; x1 += 2; y1 += 2
    cnvs.delete("c")
    cnvs.create_oval(cx - x0, cy - y0, cx + x1, cy + y1, width=20, fill=fill_color, tags="c")
    counter += 1

cnvs.delete("c")

frame_count = 12
frames = [PhotoImage(file='exp.gif', format='gif -index %i' % (i)) for i in range(frame_count)]


def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frame_count:
        ind = 0
    PlaySound("exp_snd.wav", SND_ASYNC)
    label.configure(image=frame)
    # window.after(100, update, ind)

label = Label(window)
label.place(x=200, y=200)
window.after(0, update, 0)

window.mainloop()
