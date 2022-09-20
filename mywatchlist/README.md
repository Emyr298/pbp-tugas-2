# Tugas 3 PBP

## Perbedaan JSON, XML, HTML
JSON, XML, HTML adalah format dari _data delivery_ yang sering dipakai pada aplikasi platform. Suatu file HTML berisi dari kumpulan _tag_ seperti `h1`, `div`, `p`, `img`, dsb. Pada tiap _tag_, kita bisa menambahkan _attribute_ yang memberi informasi tambahan dari _tag_-nya, seperti `id`, `class`, dsb. Tetapi, _tag_ dan _attribute_ yang ada pada HTML tidak bisa diisi sesuka hati kita karena masing-masing _tag_ memiliki makna bagi desain halaman web, sehingga kurang tepat jika kita ingin menggunakan HTML pada _data delivery_ ketika data yang dikirim tidak dimaksudkan untuk langsung ditampilkan ke halaman web. Pada kasus tersebut, kita bisa menggunakan XML dan JSON. XML memiliki _syntax_ yang mirip dengan HTML, tetapi tidak seperti pemilihan _tag_ dan _attribute_ yang ketat pada HTML, dalam XML kita diberi kebebasan dalam membuat _tag_ dan _attribute_. JSON memiliki _syntax_ yang berbeda jauh dengan keduanya. _Syntax_ dari JSON lebih singkat dibandingkan dengan XML karena tidak memerlukan _tag_ yang penulisannya _redundant_. Selain itu, JSON sudah memiliki tipe data primitif bawaan, sehingga tidak perlu menambahkan informasi mengenai tipe data dari suatu nilai dalam bentuk attribute atau semacamnya. Untuk memberi tipe data dari suatu nilai pada JSON, kita hanya perlu mengatur format penulisan nilainya, seperti menambakan tanda petik dua untuk _string_, langsung menuliskan angka saja pada _number_, dsb. Oleh karena itu, JSON umumnya memiliki ukuran yang lebih kecil dibandingkan dengan XML ketika merepresentasikan data yang sama.

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
- https://www.geeksforgeeks.org/difference-between-json-and-xml/
