print("\nMencari rumus dari kelvin\n")
f = int(input("masukan suhu anda : "))
c = ((5 / 9) * f) - 32
k = (c + 273)
print("suhu anda adalah", k)

print("\nMencari rumus fahrenheit\n")
k1 = int(input("masukan suhu anda : "))
c1 = k1 - 273
f1 = ((9 / 5) * c1) + 32
print("suhu anda adalah", f1)