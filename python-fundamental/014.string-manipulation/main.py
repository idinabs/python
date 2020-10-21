# string manipulation

# 1. menggabungkan string

# menggunakan +
nama_depan = "Abubakar"
nama_akhir = "Sidik"
nama_lengkap = nama_depan + " " + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string

nama = "petot"
print("jumlah characternya adalah :" + " " + str(len(nama))) 

# 3. indexing 

print("indexing 4 adalah :" + " " + nama[4])
print("indexing 0:5 adalah :" + " " + nama[0:5])
print("indexing -3 adalah :" + " " + nama[-1])

# 4. mencari string

gok = "a"
saya = gok in nama
print("string a didalam nama :" + " " + str(saya)) 

gok = "a"
saya = gok not in nama
print("string a didalam nama :" + " " + str(saya)) 



# 5. mencari jumlah character berdasarkan built in dari string itu sendiri

data = "petot"
nama = data.count("t")
print("hasilnya adalah :" + " " + str(nama))

# 6. mencari nilai char menggunakan ascii

nama = "p"
print("ini adalah nilai ascii :" + " " + str(ord(nama)))