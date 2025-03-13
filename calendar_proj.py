from tkinter import *
import calendar
def show_cal():
    new_root = Tk()
    new_root.config(background = "white")
    new_root.title("calendar")
    new_root.geometry("550x600")
    z = int(b.get())
    r = calendar.calendar(z)
    m = Label(new_root, text = r, font = "Consolas 10 bold")
    m.grid(row = 5, column = 1, padx = 20)
    new_root.mainloop()


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

    s = Button(root, text = "Show Calendar", fg = "black", bg = "white", command = show_cal)
    s.grid(row = 3, column = 2)

    m = Button(root, text = "Exit", fg = "black", bg = "white", command = exit)
    m.grid(row = 4, column = 2)

    root.mainloop()

