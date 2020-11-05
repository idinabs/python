namakucing = "eryanto" # var global
makanankucing = "beras"

def rubahnamakucing(namarubah):
    global namakucing
    namakucing = namarubah # var local
    print("nama kucing saya adalah",namakucing)

def rubahmakanan(nama,makanan):
    global makanankucing
    makanankucing = makanan
    print("makanan kucing",namakucing,"yaitu",makanankucing)


rubahnamakucing("opik")
rubahmakanan(nama=namakucing,makanan="sereal")


