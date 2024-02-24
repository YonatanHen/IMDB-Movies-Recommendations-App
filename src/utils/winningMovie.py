def find_winning_movie(results, history):
    """
    This function receives the last results (based on the user input) and the history data.
    Then add the movie's name to the history dictionary.
    The function returns the details of the movie that has been searched the most times and also present in the last search results.
    For the first search, the algorithm returns a randomal value from the history dictionary, depends on the order in the dictionary.
    @param results: The list of movies dicitionaries (called table_data on main.py)
    @param history: Dictionary that contines the movies that have been returned as keys and the number of their appearnces as the value.
    @return the winning movie dictionary.
    """
    results_history_intersection = {}
    for item in results:
        title = item["title"]
        if title in history:
            history[title] += 1
        else:
            history[title] = 1
        results_history_intersection[title] = history[title]

    winning_movie = max(
        results_history_intersection, key=results_history_intersection.get
    )

    for result in results:
        if result["title"] == winning_movie:
            winner = result
            results.remove(result)
            return winner

    return
