from tkinter import *
from tkinter import ttk
from src.scraper import Scraper
from src.utils.winningMovie import find_winning_movie
from src.constants import *
from src.GUI.createTable import create_table

table_data = None
search_history = {}
scraper = Scraper()

def search_button_click():
    # Retrieve the values from the entry widgets
    title = title_var.get()
    release_year = release_year_var.get()
    genre = genre_var.get()
    actors = actors_var.get()
    
    table_data = scraper.title_scraper({
        TITLE: title,
        RELEASE_YEAR: release_year,
        GENRES: genre,
        ACTORS: actors
    })

    winning_movie = find_winning_movie(table_data,search_history)

    create_table(root,table_data,winning_movie)

def clear_button_click():
    title_var.set("")
    release_year_var.set("")
    genre_var.set("")
    actors_var.set("")

root = Tk()


# Create a full screen window
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()               
root.geometry("%dx%d" % (width, height))

title_var = StringVar()
release_year_var = StringVar()
genre_var = StringVar()
actors_var = StringVar()

frm = ttk.Frame(root, padding=15)
frm.grid()

title_label = ttk.Label(frm, text = 'Title:', font=('calibre',10, 'bold')).grid(column=0, row=1)
title_entry = ttk.Entry(frm,textvariable = title_var, font=('calibre',10,'normal')).grid(column=1, row=1)

release_year_label = ttk.Label(frm, text = 'Year:', font=('calibre',10, 'bold')).grid(column=2, row=1)
release_year_label = ttk.Entry(frm,textvariable = release_year_var, font=('calibre',10,'normal')).grid(column=3, row=1)

genre_label = ttk.Label(frm, text = 'Genre:', font=('calibre',10, 'bold')).grid(column=4, row=1)
genre_entry = ttk.Combobox(
    frm,
    state="readonly",
    values=GENRES_LIST,
    textvariable=genre_var
).grid(column=5, row=1)
#genre_entry = ttk.Entry(frm,textvariable = genre_var, font=('calibre',10,'normal')).grid(column=5, row=1)

actor_label = ttk.Label(frm, text = 'Actor/Director Name:', font=('calibre',10, 'bold')).grid(column=6, row=1)
actor_entry = ttk.Entry(frm,textvariable = actors_var, font=('calibre',10,'normal')).grid(column=7, row=1)

search_btn = ttk.Button(frm, text="Search", command=search_button_click).grid(column=8, row=1)
clear_btn = ttk.Button(frm, text="Clear All", command=clear_button_click).grid(column=9, row=1)
quit_btn = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=10, row=1)

root.mainloop()