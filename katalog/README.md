# Tugas 2 PBP

## Aplikasi Heroku
- Link Aplikasi: https://pbp-tugas-2-emyr298.herokuapp.com/katalog

## Bagan Interaksi Client dengan Aplikasi Web django
![image](https://user-images.githubusercontent.com/101683735/190184552-917f0bec-2fe7-4d8e-9758-f7af3d765dc7.png)

## Penggunaan _Virtual Environment_
Virtual Environment membantu memisahkan _package_ yang dibutuhkan dalam berbagai _project_ terpisah dengan _package_ yang ter-_install_ pada komputer, sehingga menciptakan lingkungan yang terisolasi.

Sebenarnya, kita bisa saja membuat aplikasi web berbasis django tanpa menggunakan _virtual environment_. Hal ini dilakukan dengan meng-_install_ setiap _package_ yang dibutuhkan pada komputer. Tetapi, akan lebih baik jika kita menggunakan _virtual environment_. Hal ini karena dengan terisolasinya lingkungan _project_ kita, kita dapat memiliki _project_ berbeda yang menggunakan versi _package_ berbeda. Selain itu, kita juga dapat menjaga konsistensi versi _package_ ketika _project_ dipindahkan ke komputer lain.

## Pengerjaan
### Nomor 1: Fungsi pada `views.py`
Dalam `view.py`, saya menambahkan fungsi show_catalog yang menerima parameter `request` (objek yang menyimpan isi _request_ dari _client_) yang berfungsi untuk mengirimkan _item_-_item_ pada katalog yang tersedia kepada _client_. Setelah itu, saya dapatkan data dari seluruh _item_ yang tersedia pada katalog dengan memanggil `CatalogItem.objects.all()`. Setelah itu, saya simpan data katalog yang telah didapat beserta nama dan NPM saya pada _dictionary_ `context` untuk dipetakan pada HTML template (`katalog.html`) nantinya. Setelah `context` terbentuk, saya panggil fungsi `render(request, 'katalog.html', context)` untuk membuat HTML yang telah terisi data dan me-_return_ fungsi `show_catalog` dengan _return value_-nya. HTML inilah yang akan dikirim ke _client_ sebagai _response body_ untuk ditampilkan pada _browser_-nya.

### Nomor 2: _Routing_
Pada `urlpatterns` di `urls.py` milik `project_django`, saya tambahkan `path('katalog/', include('katalog.urls'))`. Hal ini bertujuan untuk memberikan _route_ pada aplikasi katalog sehingga _browser_ bisa mengaksesnya melalui `/katalog`. Setelah itu, pada `urls.py` milik katalog _app_, saya tambahkan `app_name` berupa `'katalog'` dan saya tambahkan _list_ `urlpatterns` berisi `path('', show_catalog, name='show_catalog')` sehingga ketika _browser_ mengunjungi _path_ `/katalog`, fungsi `show_catalog` akan dipanggil.

### Nomor 3: Pemetaan Data ke HTML
Saya sudah mengirimkan data yang akan dimasukkan ke HTML-nya melalui `context` pada fungsi `show_catalog`, tetapi `katalog.html` (template HTML yang dipakai) belum bisa menggunakannya karena tidak ada pemanggilan data dari `context`, sehingga perlu saya buat pemanggilannya. Saya mengganti setiap `Fill me!` dengan `{{name}}` dan `{{student_id}}` sehingga nama dan NPM saya akan ditampilkan. Setelah itu, saya menambahkan `{% for catalog_item in catalog_items %}` untuk mengiterasi tiap elemen dari `catalog_items`. Di dalam _for-loop_ tersebut saya isi dengan kolom dari tabel HTML yang memanggil seluruh atribut dari elemen dari `catalog_items` yang sedang diiterasi, sehingga akan terbentuk tabel yang berisi data dari tiap _item_ yang ada di katalog.

Setelah menjalankan _local server_, halaman katalog sudah berhasil terlihat, namun tabel yang ada masih kosong. Hal ini terjadi karena _database_-nya masih kosong, sehingga untuk memastikan bahwa aplikasi katalog saya sudah berjalan dengan baik, saya memasukkan data yang ada pada `initial_catalog_data.json` ke _database_ dengan memanggil `python manage.py loaddata initial_catalog_data.json`. Setelah saya jalankan _local server_-nya kembali, tabel sudah menunjukkan _item_-_item_ yang tersedia di katalog.

### Nomor 4: _Deployment_ ke Heroku
Pada template, sudah disediakan workflow yang akan men-_deploy_ aplikasi django ke Heroku secara otomatis setiap _commit_ dilakukan. Namun, workflow tersebut belum bisa berjalan dengan baik karena membutuhkan `HEROKU_APP_NAME` dan `HEROKU_API_KEY`, sehingga saya mendapatkan keduanya terlebih dahulu. Saya membuat aplikasi heroku baru bernama `pbp-tugas-2-emyr298` dan menggunakan nama tersebut sebagai `HEROKU_APP_NAME`. Saya mengambil `HEROKU_API_KEY` dari halaman _account settings_ dari akun Heroku saya. Setelah mendapatkan keduanya, saya membuat _key-pair_ pada GitHub Secrets dengan nama dan nilai yang sesuai. Setelah menjalankan kembali workflow yang gagal, akhirnya aplikasi django ini ter-_deploy_ ke Heroku.

## Referensi
- https://stackoverflow.com/questions/4319825/python-unittest-opposite-of-assertraises
- https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-1
- https://scele.cs.ui.ac.id/pluginfile.php/159934/mod_resource/content/1/02%20-%20Introduction%20to%20the%20Internet%20and%20Web%20Framework.pdf
- https://scele.cs.ui.ac.id/pluginfile.php/160675/mod_resource/content/1/Slides-3%20MTV%20Django%20Architecture.pdf
- https://www.geeksforgeeks.org/python-virtual-environment/
