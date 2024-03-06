# Masukkan nilai 
hari_kerja = int(input("Masukkan jumlah hari kerja dalam sebulan: "))
hari_kerja_perbulan = int(input("Masukkan jumlah hari kerja penuh dalam sebulan: "))
hari_lembur = int(input("Masukkan jumlah hari lembur dalam sebulan: "))

#Tetapkan gaji dan tarif lembur
gaji = 3000000
tarif_lembur = 50000

# Hitung gaji pokok
gaji_pokok = (hari_kerja / hari_kerja_perbulan) * gaji

# Hitung gaji lembur jika ada
if hari_lembur > 0:
    gaji_lembur = hari_lembur * tarif_lembur
else:
    gaji_lembur = 0

# Hitung total gaji
total_gaji = gaji_pokok + gaji_lembur

# Format dan cetak total gaji
total_gaji = f"{total_gaji:,.2f}"
print("Total gaji: Rp", total_gaji)
