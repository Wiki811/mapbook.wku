from tkinter import *

root = Tk()

root.title("MAPBOOK_WKU")
root.geometry("1024x760")


# FRAME
ramka_lista_obiektow = Frame(root)
ramka_formularz = Frame(root)
ramka_szczegoly_obiektow = Frame(root)

ramka_lista_obiektow.grid(row=0, column=0)
ramka_formularz.grid(row=0, column=1)
ramka_szczegoly_obiektow.grid(row=1, column=0, columnspan=2)

# RAMKA LISTA OBIEKTOW
Label_lista_obiektow = Label(ramka_lista_obiektow,text="Lista znajomych: ")
listbox_lista_obiektow =Listbox(ramka_lista_obiektow,)



button_pokaz_szczegoly_obiektow = Button(ramka_lista_obiektow,text="Pokaż szczegóły obiektów")
button_usun_obiekt = Button(ramka_lista_obiektow,text="Usuń")
button_edytuj_obiekt = Button(ramka_lista_obiektow,text="Edytuj obiekt")

Label_lista_obiektow.grid(row=0, column=0)
listbox_lista_obiektow.grid(row=1, column=0)
button_pokaz_szczegoly_obiektow.grid(row=2, column=0)
button_usun_obiekt.grid(row=2, column=1)
button_edytuj_obiekt.grid(row=2, column=2)

# RAMKA FORMULARZ

label_formularz = Label(ramka_formularz,text="Formularz: ")
label_imie = Label(ramka_formularz,text="imie: ")
label_nazwisko = Label(ramka_formularz,text="nazwisko: ")
label_liczba_postow = Label(ramka_formularz,text="liczba postow: ")
label_lokalizacja = Label(ramka_formularz,text="lokalizacja: ")

label_formularz.grid(row=0, column=0)
label_imie.grid(row=1, column=0)
label_nazwisko.grid(row=2, column=0)
label_liczba_postow.grid(row=3, column=0)
label_lokalizacja.grid(row=4, column=0)


entry_imie = Entry(ramka_formularz)
entry_nazwisko = Entry(ramka_formularz)
entry_liczba_postow = Entry(ramka_formularz)
entry_lokalizacja = Entry(ramka_formularz)

entry_imie.grid(row=1, column=1)
entry_nazwisko.grid(row=2, column=1)
entry_liczba_postow.grid(row=3, column=1)
entry_lokalizacja.grid(row=4, column=1)

button_dodaj_uzytkownika = Button(ramka_formularz,text="Dodaj użytkownika")
button_dodaj_uzytkownika.grid(row=5, column=0, columnspan=2)

# SZCZEGÓŁY OBIEKTU


label_szczegoly_obiektu = Label(ramka_szczegoly_obiektow, text="Szczegóły obiektów")
label_imie_szczegoly_obiektu = Label(ramka_szczegoly_obiektow, text="Imię: ")
label_imie_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektow, text="...")
label_nazwisko_szczegoly_obiektu = Label(ramka_szczegoly_obiektow, text="Nazwisko: ")
label_nazwisko_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektow, text="...")
label_liczba_postow_szczegoly_obiektu = Label(ramka_szczegoly_obiektow, text="Liczba Postow: ")
label_liczba_postow_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektow, text="...")
label_lokalizacja_szczegoly_obiektu = Label(ramka_szczegoly_obiektow, text="Lokalizacja: ")
label_lokalizacja_szczegoly_obiektu_wartosc = Label(ramka_szczegoly_obiektow, text="...")


label_szczegoly_obiektu.grid(row=0, column=0)
label_imie_szczegoly_obiektu.grid(row=1, column=0)
label_imie_szczegoly_obiektu_wartosc.grid(row=1, column=1)
label_nazwisko_szczegoly_obiektu.grid(row=1, column=2)
label_nazwisko_szczegoly_obiektu_wartosc.grid(row=1, column=3)
label_liczba_postow_szczegoly_obiektu.grid(row=1, column=4)
label_liczba_postow_szczegoly_obiektu_wartosc.grid(row=1, column=5)
label_lokalizacja_szczegoly_obiektu.grid(row=1, column=6)
label_lokalizacja_szczegoly_obiektu_wartosc.grid(row=1, column=7)




root.mainloop()