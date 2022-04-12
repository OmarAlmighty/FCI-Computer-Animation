from tkinter import *

def scale(lt, rt, rb, lb, S):
    sx1 = lt[0] * S[0]
    sy1 = lt[1] * S[1]
    sx2 = rt[0] * S[0]
    sy2 = rt[1] * S[1]
    sx3 = rb[0] * S[0]
    sy3 = rb[1] * S[1]
    sx4 = lb[0] * S[0]
    sy4 = lb[1] * S[1]
    return sx1, sy1, sx2, sy2, sx3, sy3, sx4, sy4


window = Tk()
cnvs = Canvas(window, width=500, height=500)
cnvs.pack()
cx = 250
cy = 250
width = 100
height = 200
x1 = cx - (width / 2)
y1 = cy - (height / 2)
x2 = cx + (width / 2)
y2 = cy - (height / 2)
x3 = cx + (width / 2)
y3 = cy + (height / 2)
x4 = cx - (width / 2)
y4 = cy + (height / 2)
cnvs.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, tags="p1")

sx1, sy1, sx2, sy2, sx3, sy3, sx4, sy4 = scale((x1, y1), (x2, y2), (x3, y3), (x4, y4), (1.01, 1.3))

endx = 1 + 3/100
endy = 1 + 3/100
sx = 1
sy = 1
while sx < endx or sy < endy:
    sx1, sy1, sx2, sy2, sx3, sy3, sx4, sy4 = scale((x1, y1), (x2, y2), (x3, y3), (x4, y4), (sx, sy))

    width = abs(sx1 - sx2)
    height = abs(sy1 - sy4)
    x1 = cx - (width / 2)
    y1 = cy - (height / 2)
    x2 = cx + (width / 2)
    y2 = cy - (height / 2)
    x3 = cx + (width / 2)
    y3 = cy + (height / 2)
    x4 = cx - (width / 2)
    y4 = cy + (height / 2)
    cnvs.delete("p1")
    cnvs.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, tags="p1")
    cnvs.after(100)
    cnvs.update()

    if sx < endx:
        sx += 0.001
    if sy < endy:
        sy += 0.001

    print(sx, sy)
window.mainloop()