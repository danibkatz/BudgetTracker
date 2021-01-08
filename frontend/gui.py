# GUI File - Frontend 
from tkinter import *
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


window = Tk()

# specify size of window.
window.geometry("500x600")

# Create text widget and specify size.
T = Text(window, height=5, width=52)

# Create label
l = Label(window, text="Fact of the Day")
l.config(font=("Courier", 14))

Fact = """A man can be arrested in 
Italy for wearing a skirt in public."""

# Create button for next text.
b1 = Button(window, text="Next", )

# Create an Exit button.
b2 = Button(window, text="Exit",
            command=window.destroy)

l.pack()
T.pack()
b1.pack()
b2.pack()

# Insert The Fact.
T.insert(END, Fact)

window.mainloop()