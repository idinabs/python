print(50*"=")

from collections import deque

mydata = deque([1,2,3,4,5,6])
print("ini adalah data sekarang", mydata)

# menambahkan data
mydata.append(7)
print("ini adalah data sekarang", mydata)

mydata.append(8)
print("ini adalah data sekarang", mydata)

# mengurangi data
datakeluar = mydata.popleft()
print("ini adalah data keluar",datakeluar)
print("ini adalah data sekarang",mydata)