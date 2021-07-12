from geometri.persegipanjang import hitung_luas_persegipanjang
from geometri.segitiga import hitung_luas_segitiga

# import geometri.segitiga as gs

a = 10
t = 3
print(f'Menghitung luas segitiga : {round(hitung_luas_segitiga(a, t))}')

p = 10
l = 2
print(f'\nMenghitung luas persegi panjang : {round(hitung_luas_persegipanjang(p, l))}')
