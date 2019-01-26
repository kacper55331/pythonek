# Wykonaj wykres funkcji:
# • f(x) = x/(-3) + a dla x <= 0,
# • f(x) = x*x/3 dla x >= 0,
# • gdzie x = <-10;10> z krokiem 0.5.

import matplotlib.pyplot as plt
import pylab as p

a = int(input("Podaj a: "))
x = p.arange(-10, 0, 0.5)
x2 = p.arange(0, 10, 0.5)

y = x/(-3) + a
y2 = x2*x2/3

r = plt.plot(x, y)
r2 = plt.plot(x2, y2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Wykres")
plt.figlegend((r, r2), ("x/(-3) + a", "x^2/3"), loc='upper left')

plt.grid(True)
plt.show()

input("\n\nAby zakończyć wciśnij Enter")
