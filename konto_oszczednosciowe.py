# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 22:05:04 2021

@author: Michał
"""

"""
Obliczanie stanu konta oszczędnosciowego.
"""
ilosc_lat = 5
ilosc_miesiecy_w_roku = 12
procent = 0.10

wplata_miesieczna = 100.0
stan_konta = 0.0

for rok in range(1, ilosc_lat + 1):
    for miesiac in range(1, ilosc_miesiecy_w_roku + 1):
        stan_konta += wplata_miesieczna
        print(stan_konta)
        stan_konta += stan_konta * procent
        
print(stan_konta)

