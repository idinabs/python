# casting yaitu merubaha tipe data suata nilai ke tipe data lainnya
# tipe data int, str, float, bool

print("======INTEGER======") 

data_int = 9
data_str = str(data_int)
data_float = float(data_int)
data_bool = bool(data_int)
print(data_int, "type", type(data_int))
print(data_str, "type", type(data_str))
print(data_float, "type", type(data_float))
print(data_bool, "type", type(data_bool)) # selain angka 0 akan bernial falsa


print("======FLOAT======")

data_float = 8.5
data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)

print(data_float, "type", type(data_float))
print(data_int, "type", type(data_int)) # akan dibulatkan menjadi angka pertama
print(data_str, "type", type(data_str))
print(data_bool, "type", type(data_bool)) # selain angka 0 akan bernilai false


print("======BOOLEAN======")

data_bool = True
data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)


print(data_bool, "type", type(data_bool)) # selain angka 0 akan bernilai false
print(data_int, "type", type(data_int))
print(data_float, "type", type(data_float))
print(data_str, "type", type(data_str))

print("======STRING======")

data_str = str("10")
data_bool = (data_str)
data_int = int(data_str)
data_float = float(data_str)

print(data_str, "type", type(data_str))
print(data_bool, "type", type(data_bool)) # selain angka 0 akan bernilai false
print(data_int, "type", type(data_int))
print(data_float, "type", type(data_float))

