from tkinter import *

a=Tk()
a.geometry("400x500")
a.title("CALCULATOR")

x=Entry(a, width=25, font=('Arial', 20))
x.grid(column=0, row=0, columnspan=4)

def click(value):
    current = x.get()
    x.delete(0, END)
    x.insert(0, str(current) + str(value))
def equal():
    try:
        result=eval(x.get())
        x.delete(0, END)
        x.insert(0, result)
    except:
        x.delete(0, END)
        x.insert(0, "Error")
def clear():
    x.delete(0, END)

Button(a, text="1", width=10, height=5,command=lambda: click(1)).grid(column=0, row=1)
Button(a, text="2", width=10, height=5,command=lambda: click(2)).grid(column=1, row=1)
Button(a, text="3", width=10, height=5,command=lambda: click(3)).grid(column=2, row=1)
Button(a, text="4", width=10, height=5,command=lambda: click(4)).grid(column=0, row=2)
Button(a, text="5", width=10, height=5,command=lambda: click(5)).grid(column=1, row=2)
Button(a, text="6", width=10, height=5,command=lambda: click(6)).grid(column=2, row=2)
Button(a, text="7", width=10, height=5,command=lambda: click(7)).grid(column=0, row=3)
Button(a, text="8", width=10, height=5,command=lambda: click(8)).grid(column=1, row=3)
Button(a, text="9", width=10, height=5,command=lambda: click(9)).grid(column=2, row=3)
Button(a, text="0", width=10, height=5,command=lambda: click(0)).grid(column=0, row=4)
Button(a, text="+", width=10, height=5,command=lambda: click("+")).grid(column=3, row=1)
Button(a, text="-", width=10, height=5,command=lambda: click("-")).grid(column=3, row=2)
Button(a, text="*", width=10, height=5,command=lambda: click("*")).grid(column=3, row=3)
Button(a, text="/", width=10, height=5,command=lambda: click("/")).grid(column=3, row=4)
Button(a, text="=", width=10, height=5,command=equal).grid(column=1, row=4)
Button(a, text="C", width=10, height=5,command=clear).grid(column=2, row=4)
a.mainloop()