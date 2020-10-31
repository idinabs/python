# while adalah jenis pengulangan yang sama seperti for

angka = 0

while angka < 5:
    print("ini adalah angka ke",angka)
    angka += 1

print("udah diluar while")

print("\n============================\n")

# looping menggunakan boolean 

start = True
angka = 1

while start:
    print("ini adalah permulaan")
    if angka is 20:
        print("ini adalah angka ke 20")
        start = False
    angka += 1

# break, continue, pass

print("\n============================\n")

angka = 0

while angka < 11:
    
    if angka is 2:
        print("ini adalah angka 2")
        # break # sama seperti fungsi break pada for 
        # continue # akan ngeprint kembali nilai dari awal lagi dan nggak akan lanjur
        pass
        print("lanjut bro")
    print("print didalam while")
    angka += 1
    
else:
    print("tidak ada itu disini")
    
