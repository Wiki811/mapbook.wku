from mapbook_wku.model import users
from mapbook_wku.controller import read_data, add_user

def add_user(users_data: list) -> None:
    name = input('podaj imie: ')
    location = input('podaj lokalizację: ')
    posts = int(input('podaj liczbę postów: '))
    usermessage = ['']
    users_data.append({'username': name, 'location': location, 'posts': posts,
                       'usermessage': usermessage}, )


while True:
    print('0 - zakończ program')
    print('1 - wyświetl znajomych')
    print('2 - dodaj znajomego')

    choose = input('wybierz opcję: ')
    if choose == '0':
        break
    if choose == '1':
        read_data(users[1:])
    if choose == '2':
        add_user(users)
