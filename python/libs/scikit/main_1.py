import numpy as np
import tkinter as tk
import time
from tkinter import messagebox

current_fix_tick = time.time()


def provide_data():
    current_time = time.asctime(time.localtime(time.time()))
    print(current_time)
    messagebox.showwarning("Time", current_time)


print(f"Current file is : {__name__}")

if __name__ == "__main__":
    print(__name__)
