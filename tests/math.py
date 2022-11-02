import math as math
import tkinter
from tkinter import messagebox

tk = tkinter.Tk()

radius_of_sphere = float(input("Enter the radius of sphere : "))
area_of_sphere = math.pi * radius_of_sphere * radius_of_sphere
volume_of_sphere = 4 * math.pi * math.pow(radius_of_sphere, 3)
messagebox.showwarning("Volume of sphere", volume_of_sphere)
messagebox.showinfo("Area of sphere", area_of_sphere)
