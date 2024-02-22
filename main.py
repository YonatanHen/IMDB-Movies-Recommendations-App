from tkinter import *
from tkinter import ttk
from src.scraper import Scraper
from PIL import Image, ImageTk
from src.constants import *
import requests
import io

table_data = None

def search_button_click():
    global table_data
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

    print(table_data)
    tree = ttk.Treeview(root)

    style = ttk.Style()
    style.configure("Treeview", rowheight=150)

    tree["columns"] = ("title", "year", "actors", "poster")

    tree.images = []

    tree.heading("title", text="Title")
    tree.heading("year", text="Year")
    tree.heading("actors", text="Main Actors")
    tree.heading("#0", text="Poster")

    tree.column("title", width=500)
    tree.column("year", width=50)
    tree.column("actors", width=1000)
    tree.column("#0", width=130)

    for movie in table_data:
        title = movie['title']
        year = movie['year']
        actors = ', '.join(movie['actors']) if movie['actors'] else 'N/A'

        #Fetching and resizing the image
        image_url = movie['picture_url']
        response = requests.get(image_url, stream=True, verify=False)
        image_data = response.content if response.status_code == 200 else b''
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((100, 150))
        photo = ImageTk.PhotoImage(image)

        tree.insert("", "end",values=(title, year, actors), image=photo)

        #GC prevention
        tree.images.append(photo)

    tree.grid(row=2, column=0, columnspan=10)

    title_var.set("")
    release_year_var.set(2024)
    genre_var.set("")
    actors_var.set("")

root = Tk()

# Create a full screen window
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()               
root.geometry("%dx%d" % (width, height))

title_var = StringVar()
release_year_var = IntVar(value=2024)
genre_var = StringVar()
actors_var = StringVar()

frm = ttk.Frame(root, padding=15)
frm.grid()

title_label = ttk.Label(frm, text = 'Title', font=('calibre',10, 'bold')).grid(column=0, row=1)
title_entry = ttk.Entry(frm,textvariable = title_var, font=('calibre',10,'normal')).grid(column=1, row=1)

release_year_label = ttk.Label(frm, text = 'Year', font=('calibre',10, 'bold')).grid(column=2, row=1)
release_year_label = ttk.Entry(frm,textvariable = release_year_var, font=('calibre',10,'normal')).grid(column=3, row=1)

genre_label = ttk.Label(frm, text = 'Genre', font=('calibre',10, 'bold')).grid(column=4, row=1)
genre_entry = ttk.Entry(frm,textvariable = genre_var, font=('calibre',10,'normal')).grid(column=5, row=1)

actor_label = ttk.Label(frm, text = 'Actor', font=('calibre',10, 'bold')).grid(column=6, row=1)
actor_entry = ttk.Entry(frm,textvariable = actors_var, font=('calibre',10,'normal')).grid(column=7, row=1)

scraper = Scraper()
search_btn = ttk.Button(frm, text="Search", command=search_button_click).grid(column=8, row=1)
quit_btn = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=9, row=1)

root.mainloop()