#! /usr/bin/env python
# -*- coding: utf-8 -*-

import math

op = "t"
while op != "n":
    a = int(input("Podaj bok a: "))
    b = int(input("Podaj bok b: "))
    c = int(input("Podaj bok c: "))

    if a + b > c and a + c > b and b + c > a:
        if (a**2 + b**2 == c**2 or
                a**2 + c**2 == b**2 or
                b**2 + c**2 == a**2):
            print("Z podanych boków można zbudować trójkąt prostokątny")
            print("Obwód wynosi:", (a + b + c))
            p = 0.5 * (a + b + c)
            P = math.sqrt(p * (p - a) * (p - b) * (p - c))
            print("Pole wynosi:", P)
            op = "n"
        else:
            print("Z podanych boków da się zbudować trójkąt, ale nie jest on prostokątny!")
    else:
        print("Z podanych boków nie da się zbudować trójkąta prostokątnego.")
        op = input("Spróbujesz jeszcze raz (t/n): ")
