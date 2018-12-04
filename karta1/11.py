# 11
# Określ specyfikację i zapisz za pomocą listy kroków, pseudojęzyka i schematu blokowego
# algorytm wypisujący n elementów ciągu Fibonnaciego
# Gdzie n jest liczbą naturalną większą od 2. Ciąg Fibonacciego - ciąg liczb naturalnych
# określony w sposób następujący: pierwszy wyraz i drugi wyraz są równe 1, każdy następny
# jest sumą dwóch poprzednich.
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, itd

n = int(input("Podaj n: "))


def F():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def SubFib(startNumber, endNumber):
    for cur in F():
        if cur > endNumber: return
        if cur >= startNumber:
            yield cur


for i in SubFib(1, n):
    print(i)

input("\n\nAby zakończyć wciśnij Enter")
