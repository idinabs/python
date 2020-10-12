# tipe data merupakan banyak nilai yang bisa dimasukan ke dalam variable

# tipe data angka (integer)
jumlah = 12
print(jumlah, "anak", type(jumlah))


# tipe data karakter (string)
nama = "Abubakar Sidik"
print(nama, "adalah anak", type(nama))


# tipe data angka koma (float)
nilai = 92.2
print(nilai, "anak", type(nilai))


# tipe data biner, true/false (boolean)
benar = True
print(benar, "anak", type(benar))


# tipe data khusus

# complex
kompleks = complex(79,6)
print(kompleks,type(kompleks))

# tipda data dari bahasa c

# import library/packages
from ctypes import c_double, c_bool, c_long # dll

nilai = c_double(92.2)
print(nilai, "anak", type(nilai))


nilai = c_bool(False)
print(nilai, "anak", type(nilai))







