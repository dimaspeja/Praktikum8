# Latihan 1 : Kalkulator Aman
Kode Python:
```python
def kalkulator():
    try:
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))

        operator = input("Masukkan operator (+, -, *, /): ")

        if operator == "+":
            hasil = angka1 + angka2
        elif operator == "-":
            hasil = angka1 - angka2
        elif operator == "*":
            hasil = angka1 * angka2
        elif operator == "/":
            if angka2 == 0:
                raise ZeroDivisionError("Tidak bisa membagi dengan nol!")
            hasil = angka1 / angka2
        else:
            raise Exception(f"Operator '{operator}' tidak valid!")

        print(f"Hasil: {hasil}")

    except ValueError:
        print("Error: Input harus berupa angka!")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    kalkulator()
```
## 1. Definisi fungsi
```python
def kalkulator():
```
- Membuat fungsi bernama kalkulator
- Semua proses perhitungan ada di dalam fungsi ini
- Tujuannya agar kode rapi, terstruktur, dan bisa dipanggil ulang

## 2. Blok try
- Digunakan untuk menangkap error yang mungkin terjadi
- Jika ada kesalahan, program tidak langsung berhenti, tapi masuk ke except

## 3. Input Angka
```python
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
```
- Meminta input dari pengguna
- int() mengubah input menjadi bilangan bulat
- Jika pengguna memasukkan huruf → akan muncul ValueError

## 4. Input Operator
```python
operator = input("Masukkan operator (+, -, *, /): ")
```
- Meminta operator matematika dari pengguna
- Operator akan menentukan jenis operasi

## 5. Percabangan Operasi (if-elif)
```python
if operator == "+":
    hasil = angka1 + angka2
```
- Jika operator + → melakukan penjumlahan
```python
elif operator == "-":
    hasil = angka1 - angka2
```
- Jika - → pengurangan
```python
elif operator == "*":
    hasil = angka1 * angka2
```
- Jika * → perkalian

## 6. Pembagian dan Error Nol
```python
elif operator == "/":
    if angka2 == 0:
        raise ZeroDivisionError("Tidak bisa membagi dengan nol!")
    hasil = angka1 / angka2
```
- Mengecek apakah pembagi nol
- Jika iya → memunculkan ZeroDivisionError
- Jika tidak → lakukan pembagian

## 7. Operator Tidak Valid
```python
else:
    raise Exception(f"Operator '{operator}' tidak valid!")
```
- Jika operator bukan + - * /
- Program secara sengaja memunculkan error
- Agar pengguna tahu input salah

## 8. Menampilkan Hasil
```python
print(f"Hasil: {hasil}")
```
- Menampilkan hasil perhitungan
- Menggunakan f-string agar lebih rapi

## 9. Penanganan Error (except)
### a. Error Input Bukan Angka
```python
except ValueError:
    print("Error: Input harus berupa angka!")
```
- Terjadi jika pengguna memasukkan huruf atau simbol
### b. Error Pembagian Nol
```python
except ZeroDivisionError as e:
    print(f"Error: {e}")
```
- Menangkap error pembagian nol
- Menampilkan pesan error yang sudah dibuat
### c. Error Umum
```python
except Exception as e:
    print(f"Error: {e}")
```
- Menangkap semua error lain
- Contoh: operator tidak valid

## 10. Blok if __name__ == "__main__"
```python
if __name__ == "__main__":
    kalkulator()
```
- Memastikan fungsi hanya dijalankan jika file ini dieksekusi langsung
- Jika file di-import ke file lain, fungsi tidak otomatis jalan
- Ini adalah best practice di Python

## Output
<img width="1437" height="640" alt="image" src="https://github.com/user-attachments/assets/3070bc90-76b1-45bb-9f96-87d0f5c4a6d7" />

# Latihan 2: Validasi daftar nilai
Kode python:
```python
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
```
## 1. Data awal
```python
nilai = [80, 90, 'A', 70, 100, 'B']
```
nilai adalah list yang berisi campuran data:
- Angka: 80, 90, 70, 100
- huruf (string): 'A', 'B'

Tujuannya: menghitung rata-rata hanya dari data angka, dan mengabaikan huruf.

## 2. Inisialisasi variabel
```python
total = 0
jumlah_data = 0
```
- total → menyimpan jumlah seluruh angka valid
- jumlah_data → menghitung berapa banyak data angka yang valid

## 3. Perulangan data
```python
for n in nilai:
```
- Loop untuk mengambil setiap elemen dalam list nilai
- Nilai n akan berisi: 80 → 90 → 'A' → 70 → 100 → 'B'

## 4. Blok try-except (penanganan error)
int(n) mencoba mengubah data menjadi angka
- Jika n adalah angka → berhasil
- Jika n adalah huruf → error (ValueError)

Jika berhasil:
- Tambahkan ke total
- Tambah jumlah_data

## 5. Menangani data tidak valid
```python
except ValueError:
    continue
```
Jika terjadi error (misalnya 'A' atau 'B'):
- Program tidak berhenti
- continue → langsung lanjut ke data berikutnya

Ini membuat program aman dari crash

## 6. Mengecek apakah ada data valid
```python
if jumlah_data > 0:
```
- Untuk memastikan tidak membagi dengan nol
- Jika ada minimal 1 angka valid → lanjut hitung rata-rata

## 7. Menghitung dan menampilkan rata-rata
```python
rata_rata = total / jumlah_data
print(f"Rata-rata nilai (data valid saja): {rata_rata}")
```
- Rata-rata = total ÷ jumlah_data
- Output ditampilkan dengan f-string

Perhitungan nyata:
```python
Angka valid: 80, 90, 70, 100
Total = 340
Jumlah data = 4
Rata-rata = 85.0
```
## 8. Jika tidak ada data angka
```python
else:
    print("Tidak ada data angka yang valid.")
```
- Jika semua data bukan angka → tampilkan pesan ini

## Output
<img width="1435" height="128" alt="image" src="https://github.com/user-attachments/assets/d07024cd-0e7f-4fdd-b146-00f7eb60b870" />
