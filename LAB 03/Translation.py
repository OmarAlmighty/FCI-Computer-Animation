from tkinter import *

def translate(cx, cy, T):
    tcx = cx + T[0]
    tcy = cy + T[1]
    return tcx, tcy

window = Tk()
cnvs = Canvas(window, width=500, height=500)
cnvs.pack()
cx = 250; cy = 250
width = 100; height = 200
x1 = cx - (width / 2)
y1 = cy - (height / 2)
x2 = cx + (width / 2)
y2 = cy - (height / 2)
x3 = cx + (width / 2)
y3 = cy + (height / 2)
x4 = cx - (width / 2)
y4 = cy + (height / 2)
cnvs.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, tags="p1")

endx = 200; endy = 80
tx = 5; ty = 5
while tx < endx or ty < endy:
    tcx, tcy = translate(cx, cy, (tx, ty))

    x1 = tcx - (width / 2)
    y1 = tcy - (height / 2)
    x2 = tcx + (width / 2)
    y2 = tcy - (height / 2)
    x3 = tcx + (width / 2)
    y3 = tcy + (height / 2)
    x4 = tcx - (width / 2)
    y4 = tcy + (height / 2)
    cnvs.delete("p1")
    cnvs.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, tags="p1")
    cnvs.after(100)
    cnvs.update()

    if tx < endx:
        tx += 5
    if ty < endy:
        ty += 5

window.mainloop()
