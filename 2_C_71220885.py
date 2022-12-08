angka = str(input("Masukkan angka: "))
hitung = str(input("Masukkan angka yang dihitung : "))

c = 0
for d in list(angka):
    if d == hitung:
        c = c+1
print("Angka",hitung,"muncul sebanyak",c,"kali")
