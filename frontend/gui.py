# GUI File - Frontend 
from tkinter import *
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import *


def sel():
   selection = "option " + str(var.get())
   l3.config(text = selection)


window = Tk()

# specify size of window.
window.geometry("1000x500")

# Create text widgets
t1= Text(window, height=1, width=20)
t1.grid(row=3,column=1)
t1.insert(END, "Name")

t2= Text(window, height=1, width=20)
t2.grid(row=3,column=2)
t2.insert(END, "mo/da/year")

t3= Text(window, height=1, width=20)
t3.grid(row=4,column=1)
t3.insert(END, "Projected")

t4= Text(window, height=1, width=20)
t4.grid(row=4,column=2)
t4.insert(END, "Actual")

# Create Radio Buttons
var = IntVar()
rb1 = Radiobutton(window, text="Income", variable=var, command=sel, value=1)
rb1.grid(row=5, column=1)

rb2 = Radiobutton(window, text="Expense", variable=var, command=sel, value=2)
rb2.grid(row=5, column=2)

# Create labels
l1 = Label(window, text="BudgetTracker")
l1.grid(row=1, column=5)
l1.config(font=("Times New Roman", 14))

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
l2 = Label(window, text=dt_string)
l2.grid(row=1, column=8)
l2.config(font=("Times New Roman", 14))

l3 = Label(window)
l3.grid(row=8, column=8)
l3.config(font=("Times New Roman", 14))

# Create Scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=6, column=2)

sb2 = Scrollbar(window)
sb2.grid(row=7, column=2)

# Create Lists
li1 = Listbox(window, yscrollcommand = sb1.set )
li1.grid(row=6, column=1)

li2 = Listbox(window, yscrollcommand = sb2.set )
li2.grid(row=7, column=1)

# Create buttons
b1 = Button(window, text="View List")
b1.grid(row=3, column=3)

b2 = Button(window, text="Search")
b2.grid(row=4, column=3)

b3 = Button(window, text="Add")
b3.grid(row=5, column=3)

b4 = Button(window, text="Update")
b4.grid(row=6, column=3)

b5 = Button(window, text="Delete")
b5.grid(row=7, column=3)

b6 = Button(window, text="Export")
b6.grid(row=8,column=5)

b7 = Button(window, text="Exit", command=window.destroy)
b7.grid(row=8,column=6)



window.mainloop()