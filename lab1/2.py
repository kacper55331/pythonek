#! /usr/bin/env python3
# -*- coding: utf-8 -*-

masa_ciala = float(input("Podaj swoją aktualną wagę [kg]: "))
wzrost = float(input("Podaj swoj wzrost [m]: "))
bmi = masa_ciala / wzrost**2
print(bmi)

if bmi < 18.5:
    print("Masz niedowagę")
elif bmi >= 18.5 and bmi < 25:
    print("Twoja waga jest w normie")
else:
    print("Masz nadwagę")
