import pandas as pd

dataframe_csv = pd.read_csv('data-sampah-jabar.csv')

# 1. Buatlah sebuah DataFrame dari data jumlah produksi sampah berdasarkan Kabupaten/Kota di Jawa Barat. 
# Membuat dataframe baru hanya berisi kolom 'Kabupaten/Kota', 'Jumlah Produksi Sampah (ton)', dan 'Tahun'.
dataframe_baru = dataframe_csv[['nama_kabupaten_kota', 'jumlah_produksi_sampah', 'satuan','tahun' ]] 

#2. Hitunglah total produksi sampah di seluruh Kabupaten/Kota di Jawa Barat untuk tahun tertentu. 
#Menggunakan itterows untuk menjumlahkan yang sesuai tahun yang diinputkan.

jumlah = 0

tahun = int(input("Masukkan tahun: "))
for index, row in dataframe_baru.iterrows():
    if row['tahun'] == tahun:
        jumlah = jumlah + row['jumlah_produksi_sampah']

print(f"Total produksi sampah pada tahun {tahun} adalah {jumlah:.2f} Ton")


#3. Jumlahkan Data Pertahun
#Menggunakan itterows untuk menjumlahkan data pertahun

jumlah_per_tahun = {}

for index, row in dataframe_baru.iterrows():
    tahun = row['tahun']
    jumlah_produksi = row['jumlah_produksi_sampah']

    if tahun in jumlah_per_tahun:
        jumlah_per_tahun[tahun] += jumlah_produksi
    else:
        jumlah_per_tahun[tahun] = jumlah_produksi

# Menampilkan hasil
for tahun, jumlah in jumlah_per_tahun.items():
    print(f"Jumlah produksi sampah tahun {tahun} adalah {jumlah:2f}")


#4. Jumlahkan data per Kota/Kabupaten per tahun

jumlah_per_tahun_kabupaten = {}

# Iterasi setiap baris pada DataFrame
for index, row in dataframe_baru.iterrows():
    tahun = row['tahun']
    kabkot = row['nama_kabupaten_kota']
    jumlah_produksi = row['jumlah_produksi_sampah']
    
    # Menambahkan jumlah produksi sampah ke key terkait
    if tahun in jumlah_per_tahun_kabupaten:
        jumlah_per_tahun_kabupaten[(tahun, kabkot)] += jumlah_produksi
    else:
        jumlah_per_tahun_kabupaten[(tahun, kabkot)] = jumlah_produksi

# Menampilkan hasil
print("\nJumlah produksi sampah Kabupaten/kota per tahun:")
for (tahun, kabkot), jumlah in jumlah_per_tahun_kabupaten.items():
    print(f"Tahun {tahun}, {kabkot}: {jumlah:.2f}")

# per Kota/Kabupaten

jumlah_per_kabkot = {}

# Iterasi setiap baris pada DataFrame
for index, row in dataframe_baru.iterrows():
    kabkot = row['nama_kabupaten_kota']
    jumlah_produksi = row['jumlah_produksi_sampah']

    # Menambahkan jumlah produksi sampah ke kabupaten/kota terkait
    if kabkot in jumlah_per_kabkot:
        jumlah_per_kabkot[kabkot] += jumlah_produksi
    else:
        jumlah_per_kabkot[kabkot] = jumlah_produksi

# Menampilkan hasil
print("\nJumlah produksi sampah Kabupaten/kota keseluruhan:")
for kabkot, jumlah in jumlah_per_kabkot.items():
    print(f"{kabkot}: {jumlah:.2f}")

dataframe_baru.to_csv('data-sampah-baru.csv', index=False)

dataframe_baru.to_excel('data-sampah-baru.xlsx', index=False)

