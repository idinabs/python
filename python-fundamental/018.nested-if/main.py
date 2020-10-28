# nestef if adalah statetment didalam statetment
# jika statement pertama berhasil dijalankan maka statement selanjutnya akan dijalan kan

nilai = 70

if  nilai <= 90:
    print("Selamat kamu mendapatkan A")
    if nilai <= 80:
        print("selamat kamu mendapatkan B")
    elif nilai == 70:
        print("selamat kamu mendapatkan C")
else:
    print("Yah kamu harus remidi deh")