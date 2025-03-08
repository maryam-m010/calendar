from tkinter import *
import calendar
def show_cal():
    new_root = Tk()
    new_root.config("white")


if __name__ == "__main__":
    root = Tk()
    root.config(background = "pink")
    root.title("calendar")
    root.geometry("400x400")
    l = Label(root, text = "Calendar",bg = "pink", fg = "white", font = ("Times", 35, "bold"))
    l.grid(row = 1, column = 2)

    a = Label(root, text = "Enter Year:", bg = "pink", fg = "white", font = ("Times", 20, "bold"))
    a.grid(row = 2, column = 1)

    b = Entry(root, width = 30)
    b.grid(row = 2, column = 2)

    s = Button(root, text = "Show Calendar", fg = "black", bg = "white")
    s.grid(row = 3, column = 2)

    m = Button(root, text = "Exit", fg = "black", bg = "white")
    m.grid(row = 4, column = 2)

    root.mainloop()
