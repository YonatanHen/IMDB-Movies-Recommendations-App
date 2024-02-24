'''
This function isolates the data of the movie to title, and year
'''
def manipulateMovieData(data):
    if ' in ' in data:
        #rsplit splits the data by the last ' in '
        splited_data = data.rsplit(' in ', 1)
        # if ',' in splited_data[0]:
        #     actors = list(map(lambda player_name: player_name.strip(), splited_data[0].replace(' and ', ' ').split(',')))
        # else:
        #     actors = list(map(lambda player_name: player_name.strip(), splited_data[0].split('and')))
        title_and_year = splited_data[1]
    else:
        title_and_year = data
        # actors = ""
    title = title_and_year[:-6].strip()
    year = title_and_year[-6:].replace('(', '').replace(')', '')
    
    return title, year
