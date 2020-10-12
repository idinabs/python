# memasukan nilai untuk user kemudian dicasting

data = input("nama kamu siapa ? : ")
print(data,type(data))


# jika ingin mengubah type input bisa menggunakan casting

umur = int(input("umur kamu berapa tahun ? : "))
print(umur, "tahun", type(umur))

tinggi = float(input("tinggi kamu berapa tahun ? : "))
print(tinggi, "cm", type(tinggi))


# jika ingin memasukan data biner atau boolean

biner = bool(int(input("masukan nilai kamu! : ")))
print(biner,type(biner))