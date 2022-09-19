# Tugas 3 PBP

## Perbedaan JSON, XML, HTML
JSON, XML, HTML adalah format dari data delivery yang sering dipakai pada aplikasi platform. Suatu file HTML berisi dari kumpulan tag seperti h1, div, p, img, dan sebagainya. Ada dua jenis dari tag dalam HTML, yaitu self-closing dan non-self-closing. Dalam non-self-closing tag, kita bisa menaruh berbagai tag lainnya. Tetapi, tags beserta syntax lainnya yang ada pada HTML didesain untuk mendefinisikan struktur dari halaman web, sehingga kurang tepat jika ingin digunakan untuk data yang akan langsung ditampilkan. Untuk data delivery yang datanya tidak akan langsung ditampilkan, kita bisa menggunakan XML dan JSON. XML memiliki syntax yang mirip dengan HTML, tetapi kita bebas menentukan nama dari tags yang ada. Hal ini dikarenakan XML yang didesain bukan untuk data yang akan langsung ditampilkan.

## Pentingnya Data Delivery

## Cara Implementasi
### Tahap 1: Membuat aplikasi `mywatchlist`
Untuk membuat aplikasi baru bernama `mywatchlist`, saya menjalankan command `python manage.py startapp mywatchlist`. Setelah itu, saya mendaftarkan `mywatchlist` pada `INSTALLED_APPS` di `settings.py` dari `project_django`.

### Tahap 2: Menambahkan path
Pada `urlpatterns` dari `urls.py` dalam `project_django`, saya menambahkan path baru untuk aplikasi `mywatchlist`, yaitu `path('mywatchlist/', include('mywatchlist.urls'))`. Hal ini bertujuan agar aplikasi dapat diakses melalui `/mywatchlist`.

### Tahap 3: Membuat model `MyWatchList`
Pada `models.py` dari `mywatchlist`, saya menambahkan class baru bernama `MyWatchList`, lalu saya memberinya field beserta tipe datanya sesuai yang diminta soal.

1. `watched = models.BooleanField()`: Nilai hanya `false` atau `true`
2. `title = models.CharField(max_length=255)`: Nilai berupa string pendek dengan panjang maksimum 255 karakter
3. `rating = models.IntegerField()`: Nilai berupa bilangan bulat (akan diisi oleh bilangan di antara 1 sampai 5)
4. `release_date = models.DateField()`: Nilai berupa tanggal tanpa waktu
5. `review = models.TextField()`: Nilai berupa string panjang

Setelah itu, saya lakukan migrasi dengan `python manage.py makemigrations` dan `python manage.py migrate` untuk mengaplikasikan perubahan model pada database schema.

## Referensi
- https://www.geeksforgeeks.org/html-vs-xml/
