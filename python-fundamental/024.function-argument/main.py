def favouritesongs(genre):
    print(" genre lagu favorit",genre)

favouritesongs("indie")


def songs(nama, genre):
    print("si", nama)
    print("dia suka genre musik", genre)

print(40*"=")
songs("petot", "rock")
print(40*"=")
songs("eryan", "indie")
print(40*"=")
songs("opik", "shalawat")

# menggunakan keyword argumen

print(40*"=")
def songs(nama, genre):
    print("si", nama)
    print("dia suka genre musik", genre)

songs(nama="eryanto", genre="rock")

# menggunakan default argumen
print(40*"=")
def songs(nama, genre="shalawat",hobi="masak"):
    print("si", nama)
    print("dia suka genre musik", genre)
    print("hobinya adalah", hobi)

songs("opik")