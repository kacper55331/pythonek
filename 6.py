# 6
# Kasia i Stasia otrzymują od taty pieniądze przez 30 dni w następujący sposób:
# a. pierwsza otrzymuje pieniądze Kasia i otrzymała od taty pierwszego dnia 20 złotych
# b. każdego dnia pieniądze może otrzymać tylko jedna dziewczynka
# c. dziewczynki otrzymują pieniądze na przemian
# d. wysokość otrzymywanych kwot wzrasta codziennie o 5%


kasia = int(0)
stasia = int(0)
kto = bool(False)
kwota = float(20)
stopa = int(5)  # %
for i in range(30):
    if not kto:
        kasia += kwota
        print(i+1, ". Kasia", round(kasia, 2), "zł, stopa:", round(kwota, 2), "zł")
    else:
        stasia += kwota
        print(i+1, ". Stasia", round(stasia, 2), "zł, stopa:", round(kwota, 2), "zł")
    kto = not kto
    kwota += kwota * (stopa / 100)

input("\n\nAby zakończyć wciśnij Enter")
