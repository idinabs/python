# 1. cara membuat string

    # 1. menggunakan single quotes
    # 2. menggunakan double quotes

print('\n=====Menggunakan single quotes=====')
data = 'nama saya idin'
print(data,type(data))

print("\n=====Menggunakan double quotes=====")
data = "nama saya idin"
print(data,type(data))

# 2. command tambahan string
    # menggunakan backslash(\) agar quotes tetap terbaca sebagai string
print("\n=====Menggunakan backslash=====")
print('ini adalah hari jum\'at')

    # menggunakan line feed(LF) /n
    # menggunakan carriage return(CR) /r
    # menggunakan carriage return line feed(CRFL) /r/n

print("\n=====Menggunakan line feed(LF)=====")
# lf memberikan enter atau line baru
print("Nama saya \nadalah idin")

# hanya menampilkan value yang diberi tanda CR itu saja
print("\n=====Menggunakan Carriage return(CR)=====")
print("Nama saya \radalah idin")

# berlaku seperti LF
print("\n====Menggunakan Carriage Return Life Feed(CR)====")
print("Nama saya \r\nadalah idin")

# menggunakan backspaces
print("\n=====Menggunakan backspaces=====")
print("nama saya \badalah idin")

# menggunakan tab
print("\n=====Menggunakan tab=====")
print("nama saya \t\tadalah idin")


# 3. linear dan row

# menggunakan 6 quotes,digunakan untuk memberikan nilai string jika dibutuhkan karakter yang banyak
print("\n=====Menggunakan linear=====")
print("""
nama saya abubakar sidik,biasa dipanggil petot,idin,udin petot,idik,dan sebagainya
""")

# menggunakan raw 
print(r'nama saya adalah idin \b \b \t')

