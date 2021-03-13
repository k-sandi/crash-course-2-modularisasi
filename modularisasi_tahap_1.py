"""
Program menghitung luas segitiga
luas_egitiga = (alas * tinggi) / 2
"""

print(f'Menghitung Luas segitiga 1')
alas = 10
tinggi = 6
luas_segitiga = (alas * tinggi) / 2
print(f'Luas segitiga dengan alas={alas} dan tinggi={tinggi} adalah {round(luas_segitiga)}')

print((f'\nMenghitung Luas segitiga 2 dengan copy paste'))
alas = 20
tinggi = 2
luas_segitiga = (alas * tinggi) / 2
print(f'Luas segitiga dengan alas={alas} dan tinggi={tinggi} adalah {round(luas_segitiga)}')

print(f'\nMembuat fungsi hitung_luas_segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = (alas * tinggi) / 2
    return luas_segitiga

a = 10
t = 20
print(f'Diketahui a={a}cm dan t={t}cm. Maka luas segitiga adalah {round(hitung_luas_segitiga(alas, tinggi))}cm\u00b2')

