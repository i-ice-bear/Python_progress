import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import Button

tk = tk.Tk()


def tkinter_variables():
    message_box = messagebox.showinfo("System error", "Your main file of system is corrupted. Please format your "
                                                      "computer now. Otherwise i will fuck your ass 😜")


B = Button(tk, text="Hello", command=tkinter_variables)
B.place(relx=0.5, rely=0.5, anchor=CENTER)

tk.mainloop()
