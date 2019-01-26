# Przedstaw na wykresie dwa
# różne wykresy słupkowe losowo
# wybranych liczb
# zmiennoprzecinkowych. Wykres
# porównawczy patrz przykład
# obok.
# • Funkcja f(x)=1 - X / float(n)
# • n – wprowadza użytkownik, x
# jest generowane x=arange(n)

import matplotlib.pyplot as plt
import pylab as p

n = input("Podaj n: ")
x = p.arange(int(n))
y = []

for i in x:
    y.append(p.uniform(0, 1) - i / float(n))

plt.hist(y, 50, density=True, facecolor='green', alpha=0.75)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Wykres")
plt.legend(["Dane y"], loc="upper left")

plt.grid(True)
plt.show()

input("\n\nAby zakończyć wciśnij Enter")
