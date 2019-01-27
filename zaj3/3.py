# Wykonaj wykres funkcji:
# • f(x) = x/(-3) + a dla x <= 0,
# • f(x) = x*x/3 dla x >= 0,
# • gdzie x = <-10;10> z krokiem 0.5.

import matplotlib.pyplot as plt
import pylab as p

a = int(input("Podaj a: "))
x = y = 0
lx = [0]
ly = [0]
r = 1
for i in range(0, a):
    rad = float(p.randint(0, 360)) * p.pi / 180
    x = x + r * p.cos(rad)
    y = y + r * p.sin(rad)

    lx.append(x)
    ly.append(y)
plt.plot(lx, ly, "o:", color="green", linewidth=2, alpha=0.5)
plt.plot([0, x], [0, y], color="blue")

s = p.fabs(p.sqrt(x**2 + y**2))
print("Wektor przesunięcia:", s)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Wykres")
plt.legend(["Dane x, y\nPrzemieszczenie: " + str(s)], loc="upper left")

plt.grid(True)
plt.show()

input("\n\nAby zakończyć wciśnij Enter")
