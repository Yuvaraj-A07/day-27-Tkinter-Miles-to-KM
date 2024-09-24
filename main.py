from tkinter import *

window = Tk()
window.title("Mile to Km converter")
window.minsize(400, 200)


# calculate

def calculate():
    value = enter.get()
    cal = round(int(value) * 1.609344)
    calculation.config(text=cal)


# input
enter = Entry()
enter.grid(column=1, row=0)

# miles label
label = Label(text="Miles", font=("Arial", 12, "normal"))
label.grid(column=2, row=0)

# is equal to label
is_equal_to = Label(text="is equal to", font=("Arial", 12, "normal"))
is_equal_to.grid(column=0, row=1)

# calculation label

calculation = Label(text=0, font=("Arial", 12, "normal"))
calculation.grid(column=1, row=1)

# km label
label = Label(text="Km", font=("Arial", 12, "normal"))
label.grid(column=2, row=1)

# calculate button

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
