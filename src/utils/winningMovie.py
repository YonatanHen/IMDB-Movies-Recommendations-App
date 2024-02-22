'''
This function receives the last results (based on the user input) and the history data.
Then add the movie's name to the history dictionary.
The function returns the movie that has been searched the most times.
For the first search, the algorithm returns a randomal value from the history dictionary, depends on the order in the dictionary.
'''
def find_winning_movie(results, history):
    for item in results:
        if item["title"] in history:
            history[item["title"]] += 1
        else:
            history[item["title"]] = 1
    print(history)
    return max(history, key=history.get)