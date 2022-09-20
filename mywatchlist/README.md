# Tugas 3 PBP

## Perbedaan JSON, XML, HTML
JSON, XML, HTML adalah format dari _data delivery_ yang sering dipakai pada aplikasi platform. Suatu file HTML berisi dari kumpulan _tag_ seperti `h1`, `div`, `p`, `img`, dsb. Pada tiap _tag_, kita bisa menambahkan _attribute_ yang memberi informasi tambahan dari _tag_-nya, seperti `id`, `class`, dsb. Tetapi, _tag_ dan _attribute_ yang ada pada HTML tidak bisa diisi sesuka hati kita karena masing-masing _tag_ memiliki makna bagi desain halaman web, sehingga kurang tepat jika kita ingin menggunakan HTML pada _data delivery_ ketika data yang dikirim tidak dimaksudkan untuk langsung ditampilkan ke halaman web. Pada kasus tersebut, kita bisa menggunakan XML dan JSON. XML memiliki _syntax_ yang mirip dengan HTML, tetapi tidak seperti pemilihan _tag_ dan _attribute_ yang ketat pada HTML, dalam XML kita diberi kebebasan dalam membuat _tag_ dan _attribute_. JSON memiliki _syntax_ yang berbeda jauh dengan keduanya. _Syntax_ dari JSON lebih singkat dibandingkan dengan XML karena tidak memerlukan _tag_ yang penulisannya _redundant_. Selain itu, JSON sudah memiliki tipe data primitif bawaan, sehingga tidak perlu menambahkan informasi mengenai tipe data dari suatu nilai dalam bentuk attribute atau semacamnya. Untuk memberi tipe data dari suatu nilai pada JSON, kita hanya perlu mengatur format penulisan nilainya, seperti menambakan tanda petik dua untuk _string_, langsung menuliskan angka saja pada _number_, dsb. Oleh karena itu, JSON umumnya memiliki ukuran yang lebih kecil dibandingkan dengan XML ketika merepresentasikan data yang sama.

## Pentingnya Data Delivery
Dalam aplikasi platform, akan sering terjadi pertukaran data antara satu _stack_ dengan _stack_ lainnya, contohnya yaitu pertukaran data antara _client_ dengan _server_. Oleh karena itu, diperlukan suatu format yang dapat merepresentasikan data yang dikirim sehingga _stack_ penerima bisa mendapatkan data yang sama persis dengan data yang ada pada _stack_ pengirim dengan efisien.

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

### Tahap 4: Menambahkan 10 data untuk objek `MyWatchList`
Saya membuat folder `fixtures` dengan file `initial_watchlist_data.json` dalam `mywatchlist`. Setelah itu, saya mengisi file JSON-nya dengan format yang mirip dengan file `initial_catalog_data.json` pada aplikasi `katalog`, namun seluruh field-nya diubah menyesuaikan dengan class `MyWatchList`.

Setelah itu, saya menjalankan command `python manage.py loaddata initial_watchlist_data.json` untuk memasukkan data-datanya ke database.

### Tahap 5: Fitur untuk menyajikan data dalam HTML, JSON, dan XML
Saya membuat fungsi `show_html`, `show_json`, dan `show_xml` dalam `views.py` milik `mywatchlist`. Ketiga fungsi mengambil tiap objek `MyWatchList` dengan memanggil method `MyWatchList.objects.all()` dan me-return dengan cara yang berbeda-beda. Fungsi `show_html` membuat context untuk mapping ke template terlebih dahulu lalu me-return `render(request, 'mywatchlist.html', context)` dimana `mywatchlist.html` adalah template HTML yang saya buat pada folder `templates` di `mywatchlist`. Fungsi `show_json` me-return `HttpResponse(serializers.serialize('xml', my_watch_lists), content_type='application/xml')`. Fungsi `show_xml` me-return `return HttpResponse(serializers.serialize('json', my_watch_lists), content_type='application/json')`.

### Tahap 6: Routing
Saya membuat `urls.py` pada `mywatchlist`. Setelah itu, saya membuat variabel `app_name` dengan nilai `"mywatchlist"` dan `urlpatterns` dengan array yang berisi path dari fungsi `show_html`, `show_json`, dan `show_xml`, yaitu `path('html/', show_html, name='show_html')`, `path('xml/', show_xml, name='show_xml')`, dan `path('json/', show_json, name='show_json')`.

### Tahap 7: _Deployment_ ke Heroku
Ketika saya mengecek ketiga halaman, 10 data yang sudah saya buat tidak ada dalam database Heroku. Setelah mengecek `Procfile`, ternyata permasalahannya ada pada command loaddata yang tidak dipanggil dalam komputer Heroku, sehingga saya tambahkan `python manage.py loaddata initial_watchlist_data.json` di belakang `python manage.py loaddata initial_catalog_data.json`.

Catatan: Deployment ke Heroku yang memasukkan API key dan APP key sudah dilakukan pada tugas 2 kemarin (memang disuruh begitu), sehingga tahapan tersebut ada pada README.md dari katalog. 

## Referensi
- https://www.geeksforgeeks.org/html-vs-xml/
- https://www.geeksforgeeks.org/difference-between-json-and-xml/
- https://scele.cs.ui.ac.id/pluginfile.php/161284/mod_resource/content/1/04%20-%20Data%20Delivery.pdf
- https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-2/
