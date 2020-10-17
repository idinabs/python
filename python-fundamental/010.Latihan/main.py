# soal nomor 1 (----0+++++5----8++++11------)
# soal nomor 2 (++++0-----5++++8----11++++++)

# soal 1

print("\n===== lebih dari 0 kurang dari 5 ======")
inputUser1 = float(input("Masukan angka lebih dari 0 kurang dari 5 : "))

# ===== lebih dari 0
lebihdari0 = inputUser1 > 0
print("hasil lebih dari 0 :",lebihdari0 )

# kurang dari 5
krgdari5 = inputUser1 < 5
print("hasil kurang dari 5 :",krgdari5)

# ===== lebih dari 0 kurang dari 5 ======
print("\n===== lebih dari 0 kurang dari 5 ======")
hasil1= lebihdari0 and krgdari5
print("hasilnya adalah",hasil1)

print("\n===== lebih dari 8 kurang dari 11 ======")
inputUser1 = float(input("Masukan angka lebih dari 0 kurang dari 5 : "))

# ===== lebih dari 8
lebihdari8 = inputUser1 > 8
print("hasilnya lebih dari 8 :",lebihdari8)

# kurang dari 11 ======
krgdari11 = inputUser1 < 11
print("hasilnya kurang dari 11 :",krgdari11)

print("\n===== lebih dari 8 kurang dari 11 ======")
hasil2= lebihdari8 and krgdari11
print("hasilnya adalah",hasil1)

print("\nHasil dari ----0+++++5----8++++11------")

# ===== lebih dari 0 kurang dari 5 ======
hasilgabung = (lebihdari0 and krgdari5) or (lebihdari8 and krgdari11)
print("hasilnya adalah",hasilgabung) 


