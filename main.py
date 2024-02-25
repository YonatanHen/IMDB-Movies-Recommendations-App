from tkinter import ttk, Tk, messagebox, StringVar
import re
from src.scraper import Scraper
from src.utils.winningMovie import find_winning_movie
from src.GUI.createTable import create_table
from src.constants import (
    TITLE,
    RELEASE_YEAR,
    GENRE,
    ACTORS,
    GENRES_LIST,
    LABELS_STYLE,
    ENTRIES_STYLE,
)


table_data = None
search_history = {}
scraper = Scraper()


def search_button_click(root, title_var, release_year_var, genre_var, actors_var):
    """
    The function triggers the search based on the user's inputs.
    @param root: The TKinter root object.
    @param title_var: The text that the user typed for the title input.
    @param release_year_var: The text that the user typed for the year input.
    @param genre_var: The genre type that the user set for the genre input.
    @param actors_var: The text that the user typed for the actor/director input.
    """
    # Retrieve the values from the entry widgets
    title = title_var.get()
    release_year = release_year_var.get()
    genre = genre_var.get()
    actors = actors_var.get()

    table_data = scraper.title_scraper(
        {TITLE: title, RELEASE_YEAR: release_year, GENRE: genre, ACTORS: actors}
    )

    if table_data != []:
        winning_movie = find_winning_movie(table_data, search_history)
        create_table(root, table_data, winning_movie)
    else:
        messagebox.showwarning(
            "Warning!", "No results matching the parameters you specified."
        )


def clear_button_click(title_var, release_year_var, genre_var, actors_var):
    """
    The function clears user inputs
    @param title_var: The text that the user typed for the title input.
    @param release_year_var: The text that the user typed for the year input.
    @param genre_var: The genre type that the user set for the genre input.
    @param genre_var: The text that the user typed for the actor/director input.
    """
    title_var.set("")
    release_year_var.set("")
    genre_var.set("")
    actors_var.set("")


def main():
    root = Tk()

    root.title("IMDB Movie Recommendations")

    height = root.winfo_screenheight()
    root.geometry("%dx%d" % (1250, height))

    title_var = StringVar()
    release_year_var = StringVar()
    genre_var = StringVar()
    actors_var = StringVar()

    def validate_year_input(*args):
        """
        This function validates the year input, and deletes any characters which is not a digit.
        @param *args: callback function required arguments (i.e. var, index, mode).
        """
        year_val = release_year_var.get()
        if year_val and not year_val.isdigit():
            messagebox.showwarning(
                "Not Allowed!", "Only digits are allowed on the Year entry."
            )
            release_year_var.set(year_val[:-1])

    def validate_actors_input(*args):
        """
        This function validates the actors input, and deletes any characters the does not match the pattern.
        @param *args: callback function required arguments (i.e. var, index, mode).
        """
        actors_val = actors_var.get()
        pattern  = r"[!@#$%^&*()_+~?\"|\\[\]{}`']"
        if bool(re.search(pattern, actors_val)):
            messagebox.showwarning(
                "Not Allowed!",
                "You can only enter characters or digits (actors/directors name), multiple entries should be split by commas.",
            )
            actors_var.set(actors_val[:-1])

    release_year_var.trace_add("write", validate_year_input)
    actors_var.trace_add("write", validate_actors_input)

    frm = ttk.Frame(root, padding=15)
    frm.grid()

    ttk.Label(frm, text="Title:", font=LABELS_STYLE).grid(column=0, row=1)
    ttk.Entry(frm, textvariable=title_var, font=ENTRIES_STYLE).grid(column=1, row=1)

    ttk.Label(frm, text="Year:", font=LABELS_STYLE).grid(column=2, row=1)
    ttk.Entry(frm, textvariable=release_year_var, font=ENTRIES_STYLE).grid(
        column=3, row=1
    )

    ttk.Label(frm, text="Genre:", font=LABELS_STYLE).grid(column=4, row=1)
    ttk.Combobox(
        frm, state="readonly", values=GENRES_LIST, textvariable=genre_var
    ).grid(column=5, row=1)

    ttk.Label(frm, text="Actor/Director Name:", font=LABELS_STYLE).grid(column=6, row=1)
    ttk.Entry(frm, textvariable=actors_var, font=ENTRIES_STYLE).grid(column=7, row=1)

    ttk.Button(
        frm,
        text="Search",
        command=lambda: search_button_click(
            root, title_var, release_year_var, genre_var, actors_var
        ),
    ).grid(column=8, row=1)
    ttk.Button(
        frm,
        text="Clear All",
        command=lambda: clear_button_click(
            title_var, release_year_var, genre_var, actors_var
        ),
    ).grid(column=9, row=1)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=10, row=1)

    root.mainloop()


if __name__ == "__main__":
    main()
