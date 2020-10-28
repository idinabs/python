nilai = 75

if nilai == 70:
    print("nilai anda adalah :",nilai)

if nilai is 60:
    print("nilai anda adalah :",nilai)

if nilai is not 50:
    print("nilai anda bukan :",nilai)

print(45*'=')

# menghitung range nilai 

nilai = 65
if 80 <= nilai <= 100:
    print("nilai anda", nilai, "dan anda mendapatkan nilai A")

elif 75 <= nilai <= 80:
    print("nilai anda", nilai, "dan anda mendapatkan nilai B")

elif 60 <= nilai <= 75:
    print("nilai anda", nilai, "dan anda mendapatkan nilai C")

else:
    print("anda harus mengulang kembali / remidi")

print(45*'=')

# mencari value menggunakan in dalam list
nama = ["idin","eryanto","opik"]
mau = "haris"
if mau in nama:
    print("nama itu ada di",nama)
if mau not in nama:
    print("maaf nama itu tidak ada")