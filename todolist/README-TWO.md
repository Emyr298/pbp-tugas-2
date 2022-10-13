# Tugas 6 PBP

## Perbedaan _Asynchronous Programming_ dengan _Synchronous Programming_
Pada _synchronous programming_, ketika pengguna me-_request_ ke server, jalannya dari aplikasi pengguna akan terhenti sampai pengguna menerima _response_ dari server. Pada _synchronous programming_, pengguna hanya bisa mengirim satu _request_ dalam satu waktu. Contoh dari _synchronous programming_ yaitu ketika keseluruhan konten dari suatu halaman web langsung diberikan pada pengguna ketika pengguna me-_request_ _static files_ dari suatu URL. Pada saat itu, browser pengguna tidak menampilkan apa-apa sampai _static files_ yang dikirim dari server sampai ke tangannya.

Pada _asynchronous programming_, ketika pengguna me-_request_ ke server, jalannya dari aplikasi pengguna tidak berhenti meskipun _response_ dari server belum sampai. Hanya saja halaman web yang ditampilkan pada browser pengguna belum ada kontennya (biasanya tampil dalam bentuk _loading_). Pada _asynchronous programming_, pengguna bisa mengirim lebih dari satu _request_ dalam satu waktu. Contoh dari _asynchronous programming_ yaitu ketika keseluruhan konten dari suatu halaman web tidak langsung diberikan pada pengguna ketika pengguna me-_request_ _static files_ dari suatu URL sehingga setelah pengguna mendapatkan _static files_, pengguna harus me-_request_ kembali ke server untuk mendapatkan konten yang diinginkannya. Namun, sambil menunggu _response_ dari server, pengguna tetap bisa melakukan hal-hal lainnya pada halaman web, bahkan melakukan _request_ lagi.

## _Event-Driven Programming_ dan Satu Contoh Penerapannya dalam Project
_Event-driven programming_ adalah salah satu paradigma pemrograman dimana alur dari program berfokus pada terjadinya _events_. Pada paradigma ini, suatu fungsi yang disebut _event handler_ akan dipanggil ketika suatu _event_ terjadi. Hal yang menyebabkan suatu _event_ terjadi bisa bermacam-macam, seperti dikliknya suatu _button_ oleh pengguna, di-_hover_-kannya _mouse_ pada suatu elemen HTML, dll. Contoh penerapan dari _event-driven programming_ pada tugas 6 ini yaitu fungsi `showAddTaskModal()` yang berfungsi untuk menampilkan modal untuk _add task_ yang akan dijalankan setiap pengguna mengklik tombol `Tambah Task Baru` pada halaman utama aplikasi `todolist`.

## Penerapan _Asynchronous Programming_ pada AJAX
Dengan menggunakan AJAX, kita bisa mengirimkan _request_ pada suatu URL dan mendapatkan _response_-nya. Fitur ini dapat kita manfaatkan untuk menerapkan _asynchronous programming_ pada halaman web kita. HTML yang diberikan di awal oleh server masih hanya berisi struktur dari halaman web saja, belum ada konten yang ditampilkan. Untuk menampilkan konten, konten perlu didapatkan dari server melalui _request_ yang dikirim melalui AJAX. Karena AJAX bersifat _asynchronous_, pengguna tetap dapat berinteraksi dengan halaman web sambil menunggu _response_ sampai. Setelah _response_ sampai, AJAX akan menjalankan fungsi _callback_ yang berfungsi menampilkan data yang telah didapatkan dari _response_ seperti menambahkan elemen HTML baru pada _content list_, dsb.

## Cara Implementasi
### Tahap 1: AJAX GET


### Tahap 2: AJAX POST


## Referensi
- https://api.jquery.com/
- https://stackoverflow.com/questions/8918248/ajax-success-and-error-function-failure
- https://stackoverflow.com/questions/6506897/csrf-token-missing-or-incorrect-while-post-parameter-via-ajax-in-django
- https://stackoverflow.com/questions/4592493/check-if-element-exists-in-jquery
- https://scele.cs.ui.ac.id/pluginfile.php/161284/mod_resource/content/1/04%20-%20Data%20Delivery.pdf
- https://courses.cs.washington.edu/courses/cse154/12au/lectures/slides/lecture22-ajax.shtml#slide1
- https://www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_eventdriven_programming.htm#
- https://www.w3schools.com/js/js_events.asp