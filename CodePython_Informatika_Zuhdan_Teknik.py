Statement adalah sebuah instruksi atau kalimat perintah yang akan dieksekusi oleh
komputer. Contoh:
print("Hello World!")
print("Belajar Python dari Nol")
nama = "python pemula"
bila kita ingin menulis lebih dari satu statement dalam satu baris, maka
kita harus memisahnya dengan titik-koma. Contoh:
print("Hello"); print("World"); print("Tutorial Python untuk Pemula")
nama_depan = "sepuhnya"
nama_belakang = "python"
String adalah teks atau kumpulan dari karakter.
Contoh:
judul = "Belajar Pemrograman Python sampai Bisa"penulis = 'python sepuh'
Atau bisa juga bisa dengan menggunakan triple tanda petik.
Contoh:
judul = """Belajar Python dengan Cepat"""penulis = '''python pemula'''

Sintak Python bersifat case sensitive, artinya teksini dengan TeksIni dibedakan.
Contoh:
judul = "Belajar Dasa-dasar Python"
Judul = "Belajar Membuat Program Python"

Penulisan blok program harus ditambahkan indentasi (tab atau spasi 2x/4x).
Contoh yang benar
if username == 'pythonpemula'
:
print("Selamat Datang Admin")
print("Silakan ambil tempat duduk")
contoh yang salah
if username == 'petanikode'
:
print("Selamat Datang Admin")
print("Silakan ambil tempat duduk")

Variabel di python dapat dibuat dengan format seperti ini:
nama_variabel = <nilai>
Contoh:
variabel_ku = "ini isi variabel"
variabel2 = 20

Ketika sebuah variabel tidak dibutuhkan lagi, maka kita bisa menghapusnya dengan
fungsi del().
Contoh:
>>> nama = "python"
>>> print nama
python
>>> del(nama)
>>> print nama
Traceback (most recent call last):
File "<stdin>"
, line 1, in <module>NameError: name 'nama' is not defined
>>>
