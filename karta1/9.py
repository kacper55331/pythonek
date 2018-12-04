# 9
# Określ specyfikację i zapisz za pomocą listy kroków, pseudojęzyka i schematu blokowego
# algorytm wyznaczający Największą Wspólną Wielokrotność dwóch liczb (NWW)

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))

temp_a = a
temp_b = b

while a != b:
    if a < b:
        c = a
        a = b
        b = c
    else:
        a -= b
print("Największą Wspólną Wielokrotność dwóch liczb: ", temp_a*temp_b / a)

input("\n\nAby zakończyć wciśnij Enter")

