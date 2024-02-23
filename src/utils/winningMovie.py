'''
This function receives the last results (based on the user input) and the history data.
Then add the movie's name to the history dictionary.
The function returns the movie that has been searched the most times and also present in the last search results.
For the first search, the algorithm returns a randomal value from the history dictionary, depends on the order in the dictionary.
'''
def find_winning_movie(results, history):
    results_history_intersection = {}
    for item in results:
        title = item["title"]
        if title in history:
            history[title] += 1
        else:
            history[title] = 1
        results_history_intersection[title] = history[title]
    
    return max(results_history_intersection, key=results_history_intersection.get)