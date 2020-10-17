# operasi logika menghasilkan boolean
# operasi logika terdiri dari not, or, and, xor


print("\n=====NOT=====") # kebalikan dari value yang dihasilkan
a = True
b = not a
print("hasil not a :",b)

print("\n=====OR=====") # selama sebuah nilai itu true, maka akan mendapatkan hasil true
a = False
b = False
c = a or b
print("hasil a or b :",c, )
a = True
b = False
c = a or b
print("hasil a or b :",c, )
a = False
b = True
c = a or b
print("hasil a or b :",c, )
a = True
b = True
c = a or b
print("hasil a or b :",c, )

print("\n=====AND=====") # jika 2 buah nilai true, maka hasilnya true
a = False
b = False
c = a and b
print("hasil a and b :",c, )
a = True
b = False
c = a and b
print("hasil a and b :",c, )
a = False
b = True
c = a and b
print("hasil a and b :",c, )
a = True
b = True
c = a and b
print("hasil a and b :",c, )


print("\n=====XOR=====") # jika dua buah nilai true maka hasilnya false
a = False
b = False
c = a ^ b
print("hasil a XOR b :",c, )
a = True
b = False
c = a ^ b
print("hasil a XOR b :",c, )
a = False
b = True
c = a ^ b
print("hasil a XOR b :",c, )
a = True
b = True
c = a ^ b
print("hasil a XOR b :",c, )


