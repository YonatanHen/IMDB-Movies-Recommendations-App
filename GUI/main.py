from tkinter import *
from tkinter import ttk

root = Tk()

# Create a full screen window
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()               
root.geometry("%dx%d" % (width, height))

title_var = StringVar()
year_var = IntVar(value=2024)
genre_var = StringVar()

frm = ttk.Frame(root, padding=15)
frm.grid()

title_label = ttk.Label(frm, text = 'Title', font=('calibre',10, 'bold')).grid(column=0, row=1)
title_entry = ttk.Entry(frm,textvariable = title_var, font=('calibre',10,'normal')).grid(column=1, row=1)

year_label = ttk.Label(frm, text = 'Year', font=('calibre',10, 'bold')).grid(column=2, row=1)
year_entry = ttk.Entry(frm,textvariable = year_var, font=('calibre',10,'normal')).grid(column=3, row=1)

genre_label = ttk.Label(frm, text = 'Genre', font=('calibre',10, 'bold')).grid(column=4, row=1)
genre_entry = ttk.Entry(frm,textvariable = genre_var, font=('calibre',10,'normal')).grid(column=5, row=1)

ttk.Button(frm, text="Search").grid(column=6, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=7, row=1)

root.mainloop()