#! /usr/bin/env python3
# -*- coding: utf-8 -*-

KLUCZ = 3


def zaszyfruj(txt):
    tekst_do_zaszyfrowania = ""
    for i in range(len(txt)):
        if ord(txt[i]) > 122 - KLUCZ:
            tekst_do_zaszyfrowania += chr(ord(txt[i]) + KLUCZ - 26)
        else:
            tekst_do_zaszyfrowania += chr(ord(txt[i]) + KLUCZ)
    return tekst_do_zaszyfrowania


def main(args):
    tekst = input("Podaj ciąg do zaszyfrowania:\n")
    print("Ciąg zaszyfrowany:\n", zaszyfruj(tekst))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
