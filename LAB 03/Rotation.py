from tkinter import *
from math import *


def rotate(cx, cy, lt, rt, rb, lb, theta):
    # Convert degrees to radians
    angle = radians(theta)

    # shift the points to the origin (0,0)
    x1 = lt[0] - cx
    y1 = lt[1] - cy
    x2 = rt[0] - cx
    y2 = rt[1] - cy
    x3 = rb[0] - cx
    y3 = rb[1] - cy
    x4 = lb[0] - cx
    y4 = lb[1] - cy

    # Rotate the vertices
    rx1 = cx + ((x1 * cos(angle)) - (y1 * sin(angle)))
    ry1 = cy + ((x1 * sin(angle)) + (y1 * cos(angle)))

    rx2 = cx + ((x2 * cos(angle)) - (y2 * sin(angle)))
    ry2 = cy + ((x2 * sin(angle)) + (y2 * cos(angle)))

    rx3 = cx + ((x3 * cos(angle)) - (y3 * sin(angle)))
    ry3 = cy + ((x3 * sin(angle)) + (y3 * cos(angle)))

    rx4 = cx + ((x4 * cos(angle)) - (y4 * sin(angle)))
    ry4 = cy + ((x4 * sin(angle)) + (y4 * cos(angle)))

    print("%.1f" % (rx1), "%.1f" % (ry1), "%.1f" % (rx2), "%.1f" % (ry2), "%.1f"
          % (rx3), "%.1f" % (ry3), "%.1f" % (rx4), "%.1f" % (ry4))

    return rx1, ry1, rx2, ry2, rx3, ry3, rx4, ry4


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
print("%.1f" % (x1), "%.1f" % (y1), "%.1f" % (x2), "%.1f" % (y2), "%.1f" % (x3),
      "%.1f" % (y3), "%.1f" % (x4), "%.1f" % (y4))

# rx1, ry1, rx2, ry2, rx3, ry3, rx4, ry4 = rotate(cx, cy, (x1, y1), (x2, y2), (x3, y3), (x4, y4), 60)

cnvs.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, tags="p1")
ang = -5
while True:
    rx1, ry1, rx2, ry2, rx3, ry3, rx4, ry4 = rotate(cx, cy, (x1, y1), (x2, y2), (x3, y3), (x4, y4), ang)

    cnvs.delete("p1")
    cnvs.create_polygon(rx1, ry1, rx2, ry2, rx3, ry3, rx4, ry4, tags="p1")
    cnvs.after(50)
    cnvs.update()
    ang -= 5

window.mainloop()
