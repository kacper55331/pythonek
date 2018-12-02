# 2
# Samochód spala 5,5 litra benzyny na 100 km. 1 litr benzyny kosztuje 4,85 zł. Z Gdańska do
# Gdyni jest 32 km. Określ specyfikację i zapisz za pomocą listy kroków, pseudojęzyka i
# schematu blokowego algorytm, który oblicza koszt przejazdu z Gdańska do Gdyni.

spalanie = float(5.5)
cena = float(4.85)
trasa = int(32)

print("Koszt przejazdu: ", round(spalanie*(trasa/100)*cena, 2), "zł")

input("\n\nAby zakończyć wciśnij Enter")
