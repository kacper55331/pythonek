#! /usr/bin/env python3
# -*- coding: utf-8 -*-

rodzaj_umowy = input("Podaj rodzaj umowy. Jeśli jest to umowa o pracę wprowadź 'umowa o prace', jeśli na zlecenie wprowadź 'zlecenie': ")

if rodzaj_umowy == 'umowa o prace':
    kwota_brutto = float(input("Podaj kwotę brutto: "))
    skladka_emerytalna = kwota_brutto * 0.0976
    skladka_rentowa = kwota_brutto * 0.015
    skladka_chorobowa = kwota_brutto * 0.0245
    suma_skladek = skladka_emerytalna + skladka_chorobowa + skladka_rentowa
    podstawa_skladki_zdrowotnej = kwota_brutto - suma_skladek
    skladka_zdrowotna_do_zaplaty = podstawa_skladki_zdrowotnej * 0.09
    skladka_zdrowotna_do_odliczenia = podstawa_skladki_zdrowotnej * 0.075
    koszty_uzyskania_przychodu = 111.25
    podstawa_obliczenia_zaliczki_pit = round(kwota_brutto - suma_skladek - koszty_uzyskania_przychodu)
    zaliczka_na_pit = round(podstawa_obliczenia_zaliczki_pit * 0.18 - 46.33 - skladka_zdrowotna_do_odliczenia)
    wynagrodzenie_netto = round(kwota_brutto - suma_skladek - skladka_zdrowotna_do_zaplaty - zaliczka_na_pit, 2)
    podatek_do_zaplaty = round(kwota_brutto - wynagrodzenie_netto)
    print("Twoje wynagrodzenie netto wynosi: ", wynagrodzenie_netto, "zł")
    print("Podatek do zapłaty wynosi : ", podatek_do_zaplaty, "zł")
elif rodzaj_umowy == 'zlecenie':
    podstawa_zlecenia = float(input("Podaj kwotę zlecenia: "))
    skladki_na_ubezpieczenia = podstawa_zlecenia * 0.1371
    podstawa_na_ubezpieczenie_zdrowotne = podstawa_zlecenia - skladki_na_ubezpieczenia
    skladka_na_ubezpieczenie_zdrowotne_dziewiec_procent = podstawa_na_ubezpieczenie_zdrowotne * 0.09
    skladka_na_ubezpieczenie_zdrowotne_siedem_procent = podstawa_na_ubezpieczenie_zdrowotne * 0.0775
    koszty_uzyskania_przychodu = (podstawa_zlecenia - skladki_na_ubezpieczenia) * 0.2
    podstawa_opodatkowania = round(podstawa_zlecenia - (koszty_uzyskania_przychodu + skladki_na_ubezpieczenia))
    zaliczka_na_podatek = podstawa_opodatkowania * 0.18
    zaliczka_na_podatek_do_przekazania_do_urzedu = round(zaliczka_na_podatek - skladka_na_ubezpieczenie_zdrowotne_siedem_procent)
    do_zaplaty_zleceniobiorcy = round(podstawa_zlecenia - (
            skladki_na_ubezpieczenia +
            skladka_na_ubezpieczenie_zdrowotne_dziewiec_procent +
            zaliczka_na_podatek_do_przekazania_do_urzedu
    ), 2)
    podatek_do_zaplaty = round(podstawa_zlecenia - do_zaplaty_zleceniobiorcy)
    print("Twoje wynagrodzenie wynosi: ", do_zaplaty_zleceniobiorcy, "zł")
    print("Podatek do zapłaty wynosi: ", podatek_do_zaplaty, "zł")
else:
    print("Niepoprawny rodzaj umowy!")
