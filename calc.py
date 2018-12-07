#Project
#Christian, Mo, Jeremy
from tkinter import*
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("SKT Scientific Calculator") # name of the calculator
root.configure(background = "indian red") #tkinter color chart
root.resizable(width =False,height =False) #won't let user adjust the width/height of the calculator
root.geometry("480x568+0+0") #the size of the Calculator

calc = Frame(root)
calc.grid()

class Calc():
    def __init__(self):
        self.total =0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
                self.current = firstnum + secondnum
            self.display(self.current)

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

added_value = Calc()

#ENTER NUMBER / RESULTS DISPLAY
txtDisplay  = Entry(calc, font=('arial',20,'bold'), bg = "indian red", bd =30, width=28, justify=RIGHT)
txtDisplay.grid(row=0,column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")
#BUTTONS
numberpad = "789456123"
i =0
btn = []
for j in range(2,5): #3,4,5
    for k in range(3): #1,2,3
        btn.append(Button(calc, width =6, height=2, font=('arial',20,'bold'), bd =4, text = numberpad[i]))
        btn[i].grid(row=j, column =k, pady = 1)
        btn[i]["command"] = lambda x = numberpad [i]: added_value.numberEnter(x)
        i += 1
#===========BUTTONS FOR STANDARD================#
btnClear = Button(calc, text=chr(67), width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=1, column=0, pady=1)
btnClear = Button(calc, text=chr(67) + chr(69), width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=1, column=1, pady=1)
btnSq = Button(calc, text="√", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=1, column=2, pady=1)
btnAdd = Button(calc, text="+", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=1, column=3, pady=1)
btnSub = Button(calc, text="-", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=2, column=3, pady=1)
btnMult = Button(calc, text="*", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=3, column=3, pady=1)
btnDiv = Button(calc, text=chr(247), width=6, height=2, font=('arial',20,'bold') , bd=4,   #this is division, we used character instead of the division "/" sign"
            bg ="indian red").grid(row=4, column=3, pady=1)

btnZero = Button(calc, text="0", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=5, column=0, pady=1)
btnDot = Button(calc, text=".", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=5, column=1, pady=1)
btnPM = Button(calc, text=chr(177), width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=5, column=2, pady=1)
btnEquals = Button(calc, text="=", width=6, height=2, font=('arial',20,'bold') , bd=4,
                        bg ="indian red").grid(row=5, column=3, pady=1)

#=========BUTTON FOR SCIENTIFIC ==============#
btnPi = Button(calc, text="n", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=1, column=4, pady=1)
btnCos = Button(calc, text="cos", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=1, column=5, pady=1)
btntan = Button(calc, text="tan", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=1, column=6, pady=1)
btnsin = Button(calc, text="sin", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=1, column=7, pady=1)
#==
btn2Pi = Button(calc, text="2n", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=2, column=4, pady=1)
btnCosh = Button(calc, text="cosh", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=2, column=5, pady=1)
btntanh = Button(calc, text="tanh", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=2, column=6, pady=1)
btnsinh = Button(calc, text="sinh", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=2, column=7, pady=1)
#==
btnlog = Button(calc, text="log", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=3, column=4, pady=1)
btnExp = Button(calc, text="Exp", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=3, column=5, pady=1)
btnMod = Button(calc, text="Mod", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=3, column=6, pady=1)
btnE = Button(calc, text="e", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=3, column=7, pady=1)
#==
btnlog2 = Button(calc, text="log2", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=4, column=4, pady=1)
btndeg = Button(calc, text="deg", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=4, column=5, pady=1)
btncosh = Button(calc, text="acosh", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=4, column=6, pady=1)
btnasinh = Button(calc, text="asinh", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=4, column=7, pady=1)
#==
btnlog10 = Button(calc, text="log10", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=5, column=4, pady=1)
btnCos = Button(calc, text="log1p", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=5, column=5, pady=1)
btnexpm1 = Button(calc, text="expm1", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=5, column=6, pady=1)
btngamma = Button(calc, text="1gamma", width=6, height=2, font=('arial',20,'bold') , bd=4,
            bg ="indian red").grid(row=5, column=7, pady=1)

lblDisplay =Label(calc, text= "SKT Scientific Calculator",font=('arial',30,'bold'), justify=CENTER)
lblDisplay.grid(row = 0, column = 4, columnspan = 4)

#=================MENU=================#
# menu bar , lets the user pick what calculator they want to use
def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Scientific():
    root.resizable(width =False,height =False) #won't let user adjust the width/height of the calculator
    root.geometry("994x568+0+0") #the size of the Calculator

def Standard():
    root.resizable(width =False,height =False) #won't let user adjust the width/height of the calculator
    root.geometry("480x568+0+0") #the size of the Calculator

menubar = Menu(calc) #puts menu inside Frame
filemenu = Menu(menubar, tearoff = 0) #puts menubar inside
menubar.add_cascade(label = "File", menu =filemenu)
filemenu.add_command(label = "Standard", command = Standard) #name of the first half of Calculator
filemenu.add_command(label = "Scientific", command = Scientific) #name of the second half of Calculator
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit) #exits

editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu =editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")

helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Help", menu =helpmenu)
helpmenu.add_command(label = "View Help")


root.configure(menu=menubar)
root.mainloop()


#for plotter, pick how many iteration, every calculation is put into list
#for
