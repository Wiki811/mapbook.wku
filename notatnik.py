# moja_lista_na_sok=['banan','marchew','młotek']
# print(moja_lista_na_sok)
#
# moja_lista_na_sok.pop(2)
# print(moja_lista_na_sok)
#
#
# moja_lista_na_sok.remove('banan')
# print(moja_lista_na_sok)


users: list = [
    {'username': 'oliwia', 'location': 'łódź', 'posts': 1,
     'usermessage': ['życzenia1', 'kocham legie1', 'sprzedam opla', 'kiwi']},
    {'username': 'paweł', 'location': 'ostróda', 'posts': 2,
     'usermessage': ['życzenia2' 'kocham legie2', 'sprzedam opla', 'kiwi']},
    {'username': 'eliza', 'location': 'radom', 'posts': 3, 'usermessage': ['życzenia3' 'kocham legie3']},
    {'username': 'filip', 'location': 'dęblin', 'posts': 4,
     'usermessage': ['życzenia3' 'kocham legie4', 'sprzedam opla', 'kiwi']},
]
# print(users)
# users.remove({'username': 'oliwia', 'location': 'łódź', 'posts': 1,
#      'usermessage': ['życzenia1', 'kocham legie1', 'sprzedam opla', 'kiwi']})

def update_user(users_data: list)->None:
    name=input('podaj imię użytkownika do zmiany: ')

    for user in users_data:
        if user['username'] == name:
            user['username']=input('podaj nowe imię: ')
            user['location']=input('podaj nową lokalizację: ')
            user['posts']=int(input('podaj liczbę postów: '))
update_user(users)
print(users)

