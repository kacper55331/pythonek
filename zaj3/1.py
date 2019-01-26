# Napisz program, którego
# efektem będzie (patrz w prawo),
# wykres funkcji f(x) = a*x + b,
# gdzie x = <-10;10>, natomiast
# a i b będzie pobierane od
# użytkownika. Na wykresie
# powinna się pokazać informacja
# czy to jest funkcja rosnąca,
# malejąca czy stała

import matplotlib.pyplot as plt
import pylab as p

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
x = p.arange(-10, 10, 0.01)

y = a * x + b

r = plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Wykres f(x) = a*x + b")
plt.figlegend((r), ('Funkcja liniowa', ), loc='upper left')
if a > 0:
    plt.text(-3, 30, "funkcja rosnąca")
elif a < 0:
    plt.text(-3, 30, "funkcja malejąca")
else:
    plt.text(-3, 30, "funkcja stała")

plt.grid(True)
plt.show()

input("\n\nAby zakończyć wciśnij Enter")
