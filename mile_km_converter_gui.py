from tkinter import *


def button_click():
    label_mile = input_entry.get()
    label_km_value = float(label_mile) * 1.609
    label_km["text"] = round(label_km_value)


# Creating a new window and configurations
window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=200, height=100)

label = Label(text="is equal to")
label.grid(column=0, row=1)

input_entry = Entry()
input_entry.grid(column=1, row=0)

label_1 = Label(text="Miles")
label_1.grid(column=2, row=0)

label_km = Label(text="")
label_km.grid(column=1, row=1)

label2 = Label(text="Km")
label2.grid(column=2, row=1)

button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)

window.mainloop()
