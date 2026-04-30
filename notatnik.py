
users: list = [
    {'username': 'oliwia', 'location': 'Łódź', 'posts': 1,
     'usermessage': ['życzenia1', 'kocham legie1', 'sprzedam opla', 'kiwi']}, {'username': 'ola', 'location': 'Kraków', 'posts': 1,
     'usermessage': ['życzenia1', 'kocham legie1', 'sprzedam opla', 'kiwi']},
]

import folium
import requests
from bs4 import BeautifulSoup

def get_coordinates(location:str)->list:

    url=f'https://pl.wikipedia.org/wiki/{location}'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    response = requests.get(url, headers=headers)

    response_html=BeautifulSoup(response.text,'html.parser')
    response_html_latitude=float(response_html.select('.latitude')[1].text.replace(',','.'))
    response_html_longitude=float(response_html.select('.longitude')[1].text.replace(',','.'))
    return [response_html_latitude,response_html_longitude]


# for user in users:
#     print(get_coordinates(location=user['location']))

def get_mapa(users_data: list)->None:

    m = folium.Map([52, 21], zoom_start=12)
    for user in users_data:
        folium.Marker(
            location=get_coordinates(user['location']),
            tooltip="Click me!",
            popup="Mt. Hood Meadows",
            icon=folium.Icon(icon="cloud"),
        ).add_to(m)

    m.save('mapa.html')
