#! /usr/bin/env python3
# -*- coding: utf-8 -*-

print("Alfabet:")
x = 0
for i in range(65, 91):
    litera = chr(i)
    x += 1
    tmp = litera + litera.lower()
    print(tmp, end=" ")

x = -1
print("\nAlfabet odwrócony:")
for i in range(122, 96, -1):
    litera = chr(i)
    x += 1
    tmp = litera + litera.upper()
    print(tmp, end=" ")

