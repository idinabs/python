# membuat list
mylist = [1,3,5,7,9]
print(mylist)

# memomtong list/slicing/irisan
Data = mylist[3]
Data = mylist[-2]
Data = mylist[2:]
Data = mylist[:2]
Data = mylist[1:2]
print(Data)

# menambah list
mylist2 = [100,200,300,400]
mydata = mylist + mylist2
print(mydata)

# mengganti isi list
a = mylist
a[2] = 87
print(a) 

# mencopy list ke variable
Data2 = mylist[:]
Data2[3] = 20
print(mylist)

# list dalam list
datalist = [mylist, mylist2]
print(datalist)

# mengganti isi list didalam list berdasarkan 
datalist[0][2] = 90
print(datalist) 

# menghitung panjang list
panjang = len(datalist)
print(panjang)