from tkinter import *


def button_click():
    print("I got clicked.!")
    # .get() will provide the value of the entry field.
    my_label["text"] = input_entry.get()


window = Tk()
window.title("First GUI program")
window.minsize(width=500, height=300)
# To add some padding
window.config(padx=20, pady=20)


# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# Pack is needed to write the label to the screen, pack will  automatically print the object
# my_label.pack()
# Place will print the object at (x, y) provided
# my_label.place(x=0, y=0)
# Grid will print the object at relative grids and is useful
my_label.grid(column=0, row=0)


# Entry
input_entry = Entry()
input_entry.grid(column=0, row=1)


# Button
button = Button(text="Click Me", command=button_click)
button.grid(column=0, row=2)


window.mainloop()
