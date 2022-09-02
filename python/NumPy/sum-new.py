import tkinter as tk
from tkinter import messagebox
tk = tk.Tk()

assets = eval(input("Enter assets : "))
liabilities = eval(input("Enter liabilities : "))
capital = eval(input("Enter capital : "))

if sum(assets) == sum(capital) + sum(liabilities):
    def infoFunction():
        messageOutput = "Accounting equation matched"
        messagebox.showinfo("Accounting equation", messageOutput)
    infoFunction()
    print("Matched")
else:
    def alertFunction():
        messageOutput = "Accounting equation didn't matched"
        messagebox.showerror("Accounting equation", messageOutput)
    alertFunction()
    print("Didn't Matched")

