from tkinter import *


def calculate_mile():
    km = float(miles_entry.get()) * 1.609
    equal_label.config(text=km)


window = Tk()
window.title("Mile to Kilo Converter")
window.config(padx=20, pady=20)

miles_entry = Entry(width=10)
miles_entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

km_label = Label(text="is equal to")
km_label.grid(row=1, column=0)

equal_label = Label(text="0")
equal_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

calculate_button = Button(text="Calculate", command=calculate_mile)
calculate_button.grid(row=2, column=1)

window.mainloop()
