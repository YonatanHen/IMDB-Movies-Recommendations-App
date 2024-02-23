from tkinter import ttk
from .createMovieEntry import create_movie_entry

'''
The function creates the table of movies that fetched from the scraping outputs.
'''
def create_table(root, table_data,winning_movie):
    print(f'\n\nwinning movie is {winning_movie}\n\n')
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

    create_movie_entry(tree, winning_movie, True)

    for movie in table_data:
        create_movie_entry(tree, movie, False)

    tree.grid(row=2, column=0, columnspan=10)
