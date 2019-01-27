import os

slownik_wyrazow_obcych = {}
plik_do_zapisu = "slownik_wyrazow_obcych.txt"


def otworz_plik(plik):
    if os.path.isfile(plik_do_zapisu):
        with open(plik_do_zapisu, "r") as pliktxt:
            for line in pliktxt:
                t = line.split(":")
                wyraz_obcy = t[0]
                znaczenia = t[1].replace("\n", "")
                znaczenia = znaczenia.split(",")
                slownik_wyrazow_obcych[wyraz_obcy] = znaczenia
    return len(slownik_wyrazow_obcych)


def zapisz_do_pliku(slownik_wyrazow_obcych):
    pliktxt = open(plik_do_zapisu, "w")
    for wyraz_obcy in slownik_wyrazow_obcych:
        znaczenia = ",".join(slownik_wyrazow_obcych[wyraz_obcy])
        linia = ":".join([wyraz_obcy, znaczenia])
        pliktxt.write(linia)
    pliktxt.close()


def oczysc_wyraz(str):
    str = str.strip()
    str = str.lower()
    return str


def main(args):
    print("""Podaj dane w formacie:
    wyraz obcy: znaczenie1, znaczenie2
    Aby zakończyć wprowadz 'koniec'.
    """)

    nowy = False
    ileWyrazow = otworz_plik(plik_do_zapisu)
    print("Wpisów w bazie:", ileWyrazow)

    while True:
        dane = input("Podaj dane: ")
        t = dane.split(":")
        wyraz_obcy = t[0].strip().lower()
        if wyraz_obcy == 'koniec':
            break
        elif dane.count(":") == 1:
            if wyraz_obcy in slownik_wyrazow_obcych:
                print("Wyraz", wyraz_obcy, " istnieje w słowniku.")
                op = input("Zastąpić wpis (tak/nie)? ")
            if wyraz_obcy not in slownik_wyrazow_obcych or op == "tak":
                znaczenia = t[1].split(",")
                znaczenia = list(map(oczysc_wyraz, znaczenia))
                slownik_wyrazow_obcych[wyraz_obcy] = znaczenia
                nowy = True
        else:
            print("Błędny format!")

    if nowy:
        zapisz_do_pliku(slownik_wyrazow_obcych)

    print(slownik_wyrazow_obcych)

    print("=" * 50)
    print("{0: <15}{1: <40}".format("Wyraz obcy", "Znaczenia"))
    print("=" * 50)
    for wyraz_obcy in slownik_wyrazow_obcych:
        print("{0: <15}{1: <40}".format(wyraz_obcy, ",".join(slownik_wyrazow_obcych[wyraz_obcy])))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
