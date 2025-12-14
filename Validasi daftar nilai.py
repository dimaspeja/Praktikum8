nilai = [80, 90, 'A', 70, 100, 'B']

total = 0
jumlah_data = 0

for n in nilai:
    try:
        angka = int(n)
        total += angka
        jumlah_data += 1
    except ValueError:
        continue

if jumlah_data > 0:
    rata_rata = total / jumlah_data
    print(f"Rata-rata nilai (data valid saja): {rata_rata}")
else:
    print("Tidak ada data angka yang valid.")