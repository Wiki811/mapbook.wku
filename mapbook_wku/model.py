users: list = [
    {'username': 'oliwia', 'location': 'łódź', 'posts': 1,
     'usermessage': ['życzenia1', 'kocham legie1', 'sprzedam opla', 'kiwi']},
    {'username': 'paweł', 'location': 'ostróda', 'posts': 2,
     'usermessage': ['życzenia2' 'kocham legie2', 'sprzedam opla', 'kiwi']},
    {'username': 'eliza', 'location': 'radom', 'posts': 3, 'usermessage': ['życzenia3' 'kocham legie3']},
    {'username': 'filip', 'location': 'dęblin', 'posts': 4,
     'usermessage': ['życzenia3' 'kocham legie4', 'sprzedam opla', 'kiwi']},
]
def add_user(users_data:list)->None:
    print(users)
    name=input('podaj imie: ')
    location=input('podaj lokalizację: ')
    posts=int(input('podaj liczbę postów: '))
    usermessage=[]
    users.append( {'username': name , 'location': location, 'posts': posts,
         'usermessage': usermessage},)
    print(users)
add_user(users)

