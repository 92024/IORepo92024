#na potrzeby GitHub

import sys
import csv
import operator
separator = input()
sciezka = input()

plik = open (sciezka, 'r')
czytnik = csv.reader(plik, delimiter = separator)
nadawca_ile_polaczen = dict()
nadawca_dlugosc_polaczen = dict()

for indeks, wiersz in enumerate(czytnik):
    if indeks ==0:
        continue
    try:
        nadawca_ile_polaczen[int(wiersz[0])] += 1
    except:
        nadawca_ile_polaczen[int(wiersz[0])] = 1
    try:
        nadawca_dlugosc_polaczen[int(wiersz[0])] += int(wiersz[3])
    except:
        nadawca_dlugosc_polaczen[int(wiersz[0])] = int(wiersz[3])

nadawca_ppk = sorted (nadawca_ile_polaczen.items(), key = operator.itemgetter(0))
nadawca_wynik = sorted(nadawca_ppk, key = operator.itemgetter(1), reverse = True)
    
print(str(nadawca_wynik[0][0]) +': ' + str(nadawca_dlugosc_polaczen[nadawca_wynik[0][0]]))


