# operasi bitwise adalah operasi biner(true or false / 1 or 0, and more)
# operasi & | ~ ^

# ======&
print("\n=====&=====")
a = True & False
print("ini adalah hasil True  & False :",a)
b = False & False
print("ini adalah hasil False & False :",b)
c = False & True
print("ini adalah hasil False & True  :",c)
d = True & True
print("ini adalah hasil True  & True  :",d)

# ======|
print("\n=====|=====")
a = True | False
print("ini adalah hasil True  | False :",a)
b = False | False
print("ini adalah hasil False | False :",b)
c = False | True
print("ini adalah hasil False | True  :",c)
d = True | True
print("ini adalah hasil True  | True  :",d)

# ======~
print("\n=====~=====") # setiap operasi ~ valuenya ditambah 1
a = ~False
print("ini adalah hasil ~ False :",a)
b = ~True
print("ini adalah hasil ~ True  :",b)

# ======^
print("\n=====^=====")
a = True ^ False
print("ini adalah hasil True  ^ False :",a)
b = False ^ False
print("ini adalah hasil False ^ False :",b)
c = False ^ True
print("ini adalah hasil False ^ True  :",c)
d = True ^ True
print("ini adalah hasil True  ^ True  :",d)

# geser-geser
  
a = 100
b = -15

print("\n=====>>=====")
 
# print bitwise right shift operator 
print("a >> 1 =", a >> 3) 
print("b >> 1 =", b >> 1) 
  
a = 5
b = -10

print("\n=====<<=====") 
# print bitwise left shift operator 
print("a << 1 =", a << 2) 
print("b << 1 =", b << 1) 