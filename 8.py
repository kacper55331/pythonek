# 8
# Określ specyfikację i zapisz za pomocą listy kroków, pseudojęzyka i schematu blokowego
# algorytm wyznaczający Największy Wspólny Dzielnik dwóch liczb (NWD)

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

while a != b:
    if a < b:
        c = a
        a = b
        b = c
    else:
        a -= b
print("Największy Wspólny Dzielnik dwóch liczb: ", a)

input("\n\nAby zakończyć wciśnij Enter")

