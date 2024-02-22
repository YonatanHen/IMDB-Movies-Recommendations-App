'''
This function isolates the data of the movie to title, players, and year
'''
def manipulateMovieData(data):
    if 'in' in data:
        splited_data = data.split(' in ')
        if ',' in splited_data[0]:
            players = list(map(lambda player_name: player_name.strip(), splited_data[0].replace(' and ', ' ').split(',')))
        else:
            players = list(map(lambda player_name: player_name.strip(), splited_data[0].split('and')))
        title_and_year = splited_data[1]
    else:
        title_and_year = data
        players = ""
    title = title_and_year[:-6].strip()
    year = title_and_year[-6:].replace('(', '').replace(')', '')
    
    return players, title, year
