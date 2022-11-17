cepat = int(input("Masukkan kecepatan tempuh:"))
waktu = int(input("Masukkan waktu yang diperlukan:"))
#rumus
jarak = cepat*waktu
Bensin = jarak//10
biaya = 15.0000 * Bensin
#hasil
print("Teman Anda mengisi bensin sebanyak",Bensin,"liter")
print("Biaya yang dikeluarkan untuk mengisi bensin adalah Rp.",biaya)
