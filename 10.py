# 10
# Określ specyfikację i zapisz za pomocą listy kroków, pseudojęzyka i schematu blokowego
# algorytm sprawdzający czy podana liczba jest liczbą pierwszą

a = int(input("Podaj a: "))
jest = bool(True)

if a < 2:
    jest = False

i = int(2)
while i * i <= a:
    if a % i == 0:
        jest = False
    i += 1

if jest:
    print("Liczba jest liczbą pierwszą")
else:
    print("Liczba nie jest liczbą pierwszą")

input("\n\nAby zakończyć wciśnij Enter")
