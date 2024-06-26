try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

def parabola(x):
    y = x * x / 100
    return y


def draw_axes(canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, y_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvas.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals())


def plot(canvas, x, y):
    canvas.create_line(x, y, x + 1, y + 1, fill="red")


mainWindow = tkinter.Tk()
mainWindow.title("Parabola for y=x^2")

mainWindow.geometry("640x400")
canvas = tkinter.Canvas(mainWindow, width=640, height=400)
canvas.grid(row=0, column=0)

draw_axes(canvas)
for x in range(-100, 100):
    y = parabola(x)
    plot(canvas, x, -y)

mainWindow.mainloop()
