# menggunakan upper dan lower case

# menggunakan upper
data = "Abubakar sidik"
nama = data.upper()
print(nama)

# menggunakan lower
data = "Abubakar SIDIK"
nama = data.lower()
print(nama)

# mengecek menggunakan isX method
# menggunakan isalpha = untuk mengecek huruf
# menggunakan isalnum = untuk mengecek huruf dan angka
# menggunakan isdecimal = untuk mengecek semua angka
# menggunakan isspace = untuk memberikan jarak seperti /t /n
# menggunakan istitle = untuk mengecek juduk


# mengecek apakah case

# menggunakan upper
data = "Abubakar Sidik".isupper()
print("ini adalah uppercase : " + str(data))

data = "ABUBAKAR SIDIK".isupper()
print("ini adalah uppercase : " + str(data))

# menggunakan lower
data = "abubakar sidik".islower()
print("ini adalah lower : " + str(data))


# membuat title
judul = "It Is Work To Be Work".istitle()
print("ini adalah titile : " + str(judul))

print("ini adalah titile : " + str(judul))

# menggunakan startswitch dan endswitch

# menggunakan startswitch
judul = "Let's Try".startswith("Let's")
print("startswitchnya adalah : " + str(judul))

# menggunakan endswitch 
judul = "Let's Try".endswith("Let's")
print("endswitchnya adalah : " + str(judul))


# memberikan side pada string menggunakan rjust , ljust, centerJust

# example string
string = 'cat'
width = 10

# print right justified string
print(string.rjust(width))



# example string
string = 'cat'
width = 10

# print right justified string
print(string.ljust(width))

# example string
string = 'cat'
width = 10

# print right justified string
print(string.center(width))