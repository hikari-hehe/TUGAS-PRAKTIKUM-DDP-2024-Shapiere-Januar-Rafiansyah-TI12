# Minta input jumlah baris dari pengguna
jumlah_baris = int(input("Masukkan jumlah baris: "))

# Menggunakan for loop untuk mencetak bintang
for i in range(1, jumlah_baris + 1):
    print('*' * i)