# 3
# Określ specyfikację i zapisz za pomocą listy kroków, pseudojęzyka i schematu blokowego
# algorytm który, ma wczytywać z klawiatury dowolne dwie liczby. Zakładamy, że będą to liczby
# całkowite. Napisz algorytm który ma wyświetlić na ekranie monitora te liczby w kolejności
# rosnącej.

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

if a < b:
    print(a)
    print(b)
else:
    print(b)
    print(a)

input("\n\nAby zakończyć wciśnij Enter")
