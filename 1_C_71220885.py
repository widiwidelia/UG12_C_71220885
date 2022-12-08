def reverse(isi):
    teks=""
    for i in isi:
        teks=i+teks
    return teks

print(reverse(input("Masukkan Kata atau angka : ")))
