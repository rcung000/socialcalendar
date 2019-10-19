import tkinter as tk
from tkinter import ttk

from tkcalendar import Calendar, DateEntry

def mainCal():
    def print_sel():
        print(cal.selection_get())

    top = tk.Toplevel(root)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1", year=2019, month=10, day=19)
    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()

root = tk.Tk()
s = ttk.Style(root)
s.theme_use('clam')

ttk.Button(root, text='Calendar', command=mainCal).pack(padx=10, pady=10)

root.mainloop()