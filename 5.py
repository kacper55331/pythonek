# 5
# Określ specyfikację i zapisz za pomocą listy kroków, pseudojęzyka i schematu blokowego
# algorytm który wyświetla na ekranie monitora tabliczkę mnożenia w następujący sposób:
# a. Zrealizuj problem za pomocą instrukcji DOPÓKI i POWTARZAJ.
# b. Wartość pierwszego czynnika w każdym działaniu wynosi 5
# c. Wartość drugiego czynnika w działaniu pierwszym ma wartość 3 a w każdym
# następnym jest o jeden większa.
# d. Program ma wyświetlać 20 działań

# Wygląd 4 pierwszych działań:
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30

stala = int(5)
zmienna = int(3)
for i in range(20):
    print(stala, " * ", zmienna, " = ", stala * zmienna)
    zmienna += 1

input("\n\nAby zakończyć wciśnij Enter")
