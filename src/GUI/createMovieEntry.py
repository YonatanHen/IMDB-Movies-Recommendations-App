import requests
import io
from PIL import Image, ImageTk
from src.constants import WINNER

requests.packages.urllib3.disable_warnings()

'''
The function creates an entry for a movie in the movies table.
'''
def create_movie_entry(tree,movie_data,is_winner):
    title = movie_data['title'] + ' (Recommended)' if is_winner else movie_data['title']
    year = movie_data['year']

    #Fetching and resizing the image
    image_url = movie_data['picture_url']
    response = requests.get(image_url, stream=True, verify=False)
    image_data = response.content if response.status_code == 200 else b''
    image = Image.open(io.BytesIO(image_data))
    image = image.resize((100, 150))
    photo = ImageTk.PhotoImage(image)

    tag = WINNER if is_winner else ""

    tree.insert("", "end", image=photo, values=(title, year), tags=(tag, ))

    #Garbage Collector prevention
    tree.images.append(photo)

    if is_winner:
        tree.tag_configure(WINNER, background="gold")
    