# for adalah struktur kendali yang digunakan untuk melakukan looping atau pengulangan
# for menggunakan iterable untuk string dan list

# menggunakan list
mylist = ["idin", "eryan", "opik", "dayat", "haris"]

for a in mylist: #looping for membuat sebuah variable baru yaitu variable a
    print(a)
    for b in a: #disini saya melakukan nesting loop paa for sehingga nanti bisa mencetak list kedalam string
        print(b)


# menggunakan  string
for a in "idin":
    print(a)



