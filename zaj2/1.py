#! /usr/bin/env python
# -*- coding: utf-8 -*-

start = int(input("Podaj początkową liczbę: "))
stop = int(input("Podaj końcową liczbę: "))
krok = int(input("Podaj krok: "))

print("Twoje liczby to: ")
for x in range(start, stop, krok):
    print(x)
