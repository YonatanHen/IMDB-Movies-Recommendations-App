from tkinter import ttk
from .createMovieEntry import create_movie_entry


def create_table(root, table_data, winning_movie):
    """
    The function creates the table of movies that fetched from the scraping outputs.
    @param table_data: The manipulated list of movies that created by the title_scraper (under the Scraper class).
    @param winning_movie: The name of the recommended movie for the recent search.
    """

    tree = ttk.Treeview(root)

    style = ttk.Style()
    style.configure("Treeview", rowheight=150, font=("calibre", 18))
    style.configure("Treeview.Heading", font=("calibre", 14, "bold"))

    tree["columns"] = ("title", "year")

    tree.images = []

    tree.heading("#0", text="Poster")
    tree.heading("#1", text="Title")
    tree.heading("#2", text="Year")

    tree.column("#0", width=150)
    tree.column("#1", width=500)
    tree.column("#2", width=100)

    create_movie_entry(tree, winning_movie, True)

    for movie in table_data:
        create_movie_entry(tree, movie, False)

    tree.grid(row=2, column=0)
