from tkinter import messagebox
import tkinter as tk

tk = tk.Tk()

assets = eval(input("Enter your assets : "))
capital = eval(input("Enter your capital : "))
liabilities = eval(input("Enter your liabilities : "))

if sum(assets) == sum(capital) + sum(liabilities):
    def match_alert():
        messagebox.showinfo("Matched", "Accounting equation is matched")
    match_alert()
    print("Accounting equation is matched")
else:
    def not_match_alert():
        messagebox.showwarning("Not matched", "Accounting equation didn't matched")
    not_match_alert()
    print(f"Accounting equation is not matched")


