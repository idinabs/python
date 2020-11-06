print(50*"=")

mydata = [1,3,5,7,9]
print("ini adalah data saya",mydata)

# menambahkan data
mydata.append(11)
print("data telah ditambahkan",mydata)
mydata.append(13)
print("data telah ditambahkan",mydata)

# melakukan stack / stacking
out = mydata.pop() # pop merupakan built-in python untuk melakukan stacking
print("data ana telah di kurangi",out)
print("data sekarang",mydata)