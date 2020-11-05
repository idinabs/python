# tambahan bahwa list bisa dikatakan array

myfriends = ["eryan","opik","dayat"]

# menambah list
myfriends.append("harris") #menambah list menggunakan local var
print(myfriends)

myfriends.extend("ilham") #menambahkan list berdasarkan karakter 1 per 1
print(myfriends)

myfriends.insert(2,"imam") #menambah list berdasarkan urutan listnya
print(myfriends)

# menghitung jumlah list
jumlah = myfriends.count("harris")
print(jumlah)

# remove list
myfriends.remove("eryan")
print(myfriends)

myfriends.reverse()
print(myfriends)

coba = myfriends
coba.copy() #akan mncopy hasil list terakhir
coba.append("ok")
print(coba)

