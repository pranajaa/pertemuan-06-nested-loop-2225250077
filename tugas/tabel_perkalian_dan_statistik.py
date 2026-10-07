print("Tabel Perkalian dan Statistik")

n = int(input("Masukkan n: "))

while n <= 0:
    print("n harus positif!")
    n = int(input("Masukkan n: "))

total_semua = 0
count_genap = 0

# Loop untuk setiap baris
for i in range(1, n + 1):
    total_baris = 0

    # Loop untuk setiap kolom
    for j in range(1, n + 1):
        hasil = i * j
        print(hasil, end=" ")

        total_baris += hasil
        total_semua += hasil

        if hasil % 2 == 0:
            count_genap += 1

    print()
    print("Jumlah baris", i, "=", total_baris)

print("Total semua hasil =", total_semua)
print("Banyak hasil genap =", count_genap)