# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 17:08:21 2021

@author: User
"""
print("====== PROGRAM MENGITUNG JUMLAH RANGE ======")

Angka1 = int(input("Masukkan Angka Pertama : "))
Angka2 = int(input("Masukkan Angka Kedua : "))

def hitung_jumlah_range():
    asal = 0
    for i in range (Angka1, Angka2+1, 1) :
        asal = asal+i
    print("Jumlah Range Adalah = ", asal)
    
hitung_jumlah_range()