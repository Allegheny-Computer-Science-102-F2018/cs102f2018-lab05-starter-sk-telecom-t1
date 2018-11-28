from tkinter import*
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("SKT Scientific Calculator") # name of the calculator
root.configure(background = "indian red") #tkinter color chart
root.resizable(width =False,height =False) #won't let user adjust the width/height of the calculator
root.geometry("480x567+0+0") #the size of the Calculator

calc = Frame(root)
calc.grid()
# menu bar , lets the user pick what calculator they want to use
menubar = Menu(calc) #puts menu inside Frame
filemenu = Menu(menubar, tearoff = 0) #puts menubar inside
menubar.add_cascade(label = "File", menu =filemenu)
filemenu.add_command(label = "Standard") #name of the first half of Calculator
filemenu.add_command(label = "Scientific") #name of the second half of Calculator
filemenu.add_separator()
filemenu.add_command(label = "Exit") #exits

root.configure(menu=menubar)
root.mainloop()
