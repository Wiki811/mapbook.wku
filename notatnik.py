def wyswietl_napis(zmienna_1:str)->None:
    '''
    funkcja do wyświetlania napisu przez użytkownika
    :param zmienna_1:
    :return:
    '''
    print('cos')
    print(zmienna_1)

wyswietl_napis(zmienna_1='okulary')

while True:
    print('0 - zakończ program')
    print('1 - wyświetl napis')

    choose=input('wybierz opcję: ')
    if choose =='0':
        break
    if choose == '1':
        tmp_data=input('podaj słowo: ')
        wyswietl_napis(zmienna_1=tmp_data)

