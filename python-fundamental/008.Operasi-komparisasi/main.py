# Operasi komparisi digunakan untuk membandingkan suatu nilai / value
# >, < , >=, <=. ==, !=, is , is not
# Operasi komparasi menghasilkan nilai boolean yaitu true/false

print("\n===== OPERASI >")
a = 10
b = 12
hasil = a > b
print("hasil a > b : ",hasil)

print("\n===== OPERASI <")
hasil2 = a < b
print("hasil a < b :",hasil2)

print("\n===== OPERASI >=")
hasil3 = a >= b
print("hassil a >= b :",hasil3)

print("\n===== OPERASI <=")
hasil4 = a <= b
print("hasil a <= b :",hasil4)

print("\n===== OPERASI ==")
hasil5 = a == b
print("hasil a == b :",hasil5)

print("\n===== OPERASI !=")
hasil6 = a != b
print("hasil a != b :",hasil6)

print("\n===== OPERASI IS")
hasil7 = a is b
print("hasil a is b :",hasil7,"id",hex(id(hasil7)))

print("\n===== OPERASI IS NOT")
hasil8 = a is not b
print("hasil a is not b :",hasil8,"id",hex(id(hasil8)))
