# Tugas 4 dan 5 PBP

## Tugas 4
### Kegunaan `{% csrf_token %}`
Pada aplikasi web, terdapat suatu threat yang bernama _Cross Site Request Forgeries_ (CSRF). Seorang _hacker_ dapat membuat sebuah _request_ dalam bentuk URL untuk keperluan mereka, menaruhnya pada sebuah _link_, dan mengirimkan _link_ tersebut pada seorang pengguna aplikasi web yang ingin diserang. Harapannya, pengguna sedang ter-_login_ pada aplkasi web tersebut. Ketika pengguna tersebut mengklik _link_ tersebut, _request_ yang dibentuk _hacker_ akan dikirimkan pada aplikasi web dan aplikasi web tersebut akan menjalankannya karena mengira bahwa _request_ tersebut dikirimkan oleh pemilik akun karena aplikasi web mengenali pemilik akun berdasarkan _cookie_ pengguna. Hal ini sangat berbahaya karena _request_ yang dikirimkan bisa saja menyuruh aplikasi web untuk mengirimkan data, data, atau akses kepada _hacker_. Kegunaan dari `{% csrf_token %}` dalam form django adalah untuk melindungi aplikasi web dari serangan CSRF _attack_ dengan melakukan pengecekan validitas pada _request_ untuk memastikan bahwa benar-benar pemilik akun lah yang mengirimkan form lewat situsnya. Apabila  `{% csrf_token %}` tidak disertakan dalam form django, maka tidak akan ada pengecekan validitas _request_ sehingga aplikasi web tersebut rentan terhadap CSRF _attack_.

### Pembuatan form tanpa _generator_
Pembuatan form dalam django bisa dilakukan tanpa menggunakan _generator_. Hal ini dilakukan dengan membuat elemen form dalam _template_ HTML seperti `<input>`, `<textarea>`, dsb. dan menambahkan atribut `name` pada elemen tersebut. Untuk mendapatkan input pada suatu field dari pengguna dalam `view.py`, kita bisa memanggil `request.POST.get()` (ganti `POST` dengan nama _method_-nya jika _method_ dari _request_ bukan `POST`) dengan nilai atribut `name` dari elemen form yang bersesuaian sebagai argumen.

### Alur Submisi
Ketika pengguna menekan tombol _submit_, sebuah _request_ dengan suatu _method_ (`POST`, `DELETE`, dsb.) berisikan input dari pengguna akan dikirimkan ke URL atau _relative_ URL yang merupakan nilai dari atribut action pada elemen `<form>`. Aplikasi django akan menerima _request_ tersebut, mengecek validitas penggunanya (jika ada `{% csrf_token %}` pada form), mendapatkan input pengguna melalui `request.POST.get()` (ganti `POST` dengan nama _method_-nya jika _method_ dari _request_ bukan `POST`), dan mengolah data tersebut. Dengan data yang diperoleh dari pengguna, aplikasi django dapat melakukan perubahan pada data yang ada di _database_ dengan memanfaatkan berbagai _method_ yang ada pada suatu _model class_. Karena data yang ada pada _database_ sudah berubah, ketika suatu saat pengguna meminta aplikasi django untuk me-_render_ _template_ HTML, data yang ditampilkan akan berbeda dengan sebelumnya (fungsi pada `views.py` yang meng-_handle_ _request_ dari pengguna terhadap HTML mengambil data dari _database_ yang sudah berubah sebelum memasukkannya ke _context_ dan melakukan _render_).

### Tahapan Pengerjaan
#### Tahap 1: Membuat aplikasi `todolist`
Untuk membuat aplikasi `todolist`, saya menjalankan _command_ `python manage.py startapp todolist` pada terminal.

#### Tahap 2: Menambahkan _path_ `todolist`
Agar aplikasi `todolist` dapat diakses melalui `/todolist`, saya menambahkan `path('todolist/', include('todolist.urls'))` ke list `url_patterns` pada `urls.py` di `project_django`.

#### Tahap 3: Membuat model `Task`
Pada `models.py` dari `todolist`, saya membuat _class_ baru bernama `Task` yang meng-_inherit_ dari `django.db.models.Model`. Setelah itu, saya menambahkan berbagai field ke dalam _class_ tersebut. Berikut adalah _fields_-_fields_-nya:
- `user`: `ForeignKey` yang menunjuk ke sebuah objek dari _class_ `User`. Ketika objek `User` di-_delete_, setiap objek `Task` yang menunjuk kepadanya melalui field ini akan ikut ter-_delete_. Hal ini dilakukan dengan menambahkan `on_delete=models.CASCADE` pada argumen `ForeignKey`.
- `date`: `DateTimeField`
- `title`: `CharField` dengan batas maksimal 255 karakter
- `description`: `TextField`

#### Tahap 4: Implementasi _Authentication_
Saya membuat _function_ `register`, `login_user`, dan `logout_user` pada `views.py` berdasarkan pada assignment lab 3 sebelumnya yang masing-masing berfungsi untuk register, login, dan logout. Setelah itu, saya membuat template `login.html` dan `register.html` sebagai template untuk halaman login dan register.

#### Tahap 5: Membuat Halaman `todolist`
Saya membuat _function_ `todolist` dalam `views.py`. _function_ ini hanya dapat diakses ketika pengguna sedang ter-_login_ sehingga saya menambahkan _decorator_ `@login_required(login_url='/todolist/login/')` di atas _function_ tersebut agar pengguna akan ter-_redirect_ ke halaman login jika belum ter-_login_. _function_ ini akan menampilkan _task_ yang dimiliki pengguna ter-_login_ (bukan seluruhnya) sehingga kita mengambil objek-objek `Task` dengan memanfaatkan _primary key_ dari user, yaitu menggunakan `Task.objects.filter(user__pk=user.pk)`. Setelah itu objek-objek tersebut dimasukkan ke dalam `context` untuk keperluan _rendering_.

Saya juga membuat _template_ HTML `todolist.html` untuk tampilan _to-do list_. Disana username dari pengguna yang didapat dari `request.user.username` akan ditampilkan. Setiap objek-objek dari `Task` yang di-_pass_ melalui `context` juga akan diiterasi untuk ditampilkan dalam tabel. Ada juga tombol logout yang akan me-_redirect_ pengguna ke URL dari `todolist:logout` sehingga pengguna akan ter-_logout_ ketika mengklik tombol tersebut.

#### Tahap 6: Membuat Halaman Tambah _Task_
Saya membuat _function_ `create_task` dalam `views.py`. _function_ ini hanya dapat diakses ketika pengguna sedang ter-_login_ sehingga saya menambahkan _decorator_ `@login_required(login_url='/todolist/login/')` di atas _function_ tersebut agar pengguna akan ter-_redirect_ ke halaman login jika belum ter-_login_. _function_ ini akan me-_render_ form jika _method_ dari _request_ bukan `POST` dan akan menerima input pada form serta membuat objek `Task` berdasarkan input pengguna jika _method_-nya `POST`. Saya juga mem-_prevent_ _task_ yang dibuat memiliki `title` kosong dengan hanya menjalankan penambahan _task_ jika `title != ''` bernilai _True_.

Saya juga membuat _template_ HTML `create_task` untuk tampilan pembuatan _task_. Disana pengguna diminta _title_ dan _description_ dari _task_ yang ingin dibuat. Selain itu, saya menambahkan tombol "Tambah Task Baru" pada `todolist.html` yang akan me-_redirect_ pengguna ke halaman ini.

#### Tahap 7: Membuat _Routing_
Saya membuat `urls.py` pada `todolist` dan menambahkan `app_name = 'todolist'` dan sebuah list `urlpatterns` yang berisi _path_ beserta _function_-nya.

```python
urlpatterns = [
    path('', todolist, name='todolist'),
    path('create-task/', create_task, name='create_task'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
]
```

#### Tahap 8: Deployment ke Heroku
Saya melakukan _add_, _commit_, dan _push_ ke GitHub. Setelah itu, _deployment_ akan dijalankan secara otomatis (karena ada _workflow_-nya) sehingga tugas ini ter-_deploy_ secara otomatis ke Heroku.

#### Tahap 9: Membuat Dua Akun dengan Masing-Masing Tiga Data _Dummy_
Saya membuat dua akun bernama `Emyr298` dan `Ymir` lalu menambahkan tiga data _dummy_ pada situs Herokunya, yaitu pada [https://pbp-tugas-2-emyr298.herokuapp.com/todolist](https://pbp-tugas-2-emyr298.herokuapp.com/todolist).

### Referensi
- https://stackoverflow.com/questions/4195242/django-model-object-with-foreign-key-creation
- https://www.okta.com/identity-101/csrf-attack/
- https://www.squarefree.com/securitytips/web-developers.html#CSRF
- https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-3
- https://docs.djangoproject.com/en/4.1/topics/forms/
- https://www.w3schools.com/tags/att_form_action.asp
- https://www.geeksforgeeks.org/if-django-template-tags/

## Tugas 5

### Perbedaan _Inline_, _Internal_, dan _External_ CSS dan Kelebihannya
Perbedaan dari _Inline_, _Internal_, dan _External_ CSS ada pada cara pengimplementasian dari CSS._Inline_ CSS digunakan untuk memberikan sebuah elemen HTML _style_ yang unik dengan menuliskan propertinya pada atribut `style` dari elemen tersebut. Contoh dari _inline_ CSS yaitu atribut `style` pada `<h1 style="color:red;">Red Heading</h1>`. Kelebihan dari _inline_ CSS yaitu kita bisa menambahkan `style` pada elemen yang spesifik dan `style`-nya dapat langsung terlihat pada elemennya karena dekat, tidak seperti id selector yang mengharuskan kita pindah _file_ atau pindah ke barisan kode yang lain. Kekurangan dari _inline_ CSS yaitu kita hanya bisa menambahkan _style_ pada satu elemen sehingga ketika ada dua elemen dengan _style_ serupa, kita perlu kerja dua kali. _Internal_ CSS digunakan untuk mendefinisikan style dari sebuah halaman HTML (bukan hanya satu elemen seperti _Inline_ CSS) dengan menuliskan _selector_ beserta properti-properti dalam elemen HTML `<style>` pada `<head>`. Contoh dari _internal_ CSS yaitu `<style>body {background-color:red;} h1 {color:red;}</style>`. Kelebihan dari _inline_ CSS yaitu kita bisa menggunakan properti yang sama pada banyak elemen yang berbeda dengan menggunakan _selector_. Kekurangan dari _inline_ CSS yaitu tempatnya yang jauh dari elemen (ada pada `<head>`) sehingga kita perlu mengingat struktur elemen jika ingin mendesainnya. Selain itu, karena _inline_ CSS menggunakan _selector_, kita tidak dapat dengan cepat mengetahui elemen apa yang memiliki suatu _style_ (harus memikirkannya terlebih dahulu). _External_ CSS digunakan untuk mendefinisikan _style_ dari banyak halaman HTML dengan menggunakan file berekstensi `.css` dan me-_load_-nya melalui elemen HTML `<link>` pada `<head>`. Kelebihan dari _external_ CSS yaitu kita bisa mendefinisikan _style_ untuk berbagai page yang memiliki _style_ serupa, tidak perlu berulang kali menuliskan CSS-nya. Kekurangan dari _external_ CSS mirip dengan _internal_ CSS karena lokasinya yang berbeda dengan elemen yang ingin diaplikasikan _style_-nya. Selain itu, halaman tidak akan ditampilkan dengan benar sampai _external_ CSS-nya selesai di-_load_.

### Tag HTML5
- `<a>`: Membuat _hyperlink_
- `<b>`: Membuat teks menjadi _bold_
- `<body>`: Membuat _body_ dari dokumen
- `<button>`: Membuat tombol yang bisa diklik
- `<div>`: Membuat _section_ dalam dokumen
- `<embed>`: Membuat container untuk sebuah aplikasi eksternal
- `<form>`: Membuat form HTML untuk input pengguna
- `<h1>` sampai `<h6>`: Membuat _heading_
- `<head>`: Menyimpan metadata atau informasi dari dokumen
- `<input>`: Membuat tempat input
- `<nav>`: Membuat link navigasi
- `<p>`: Membuat paragraf
- `<script>`: Membuat _client-side script_
- `<span>`: Membuat _section_ dalam dokumen, biasanya untuk teks
- `<style>`: Meyimpan informasi _style_ (_internal_ CSS)

### Tipe-Tipe CSS _Selector_
- `.myclass`: Memilih elemen dengan _class_ `myclass`
- `#myid`: Memilih elemen dengan _id_ `myid`
- `*`: Memilih semua elemen
- `selector1 selector2`: Memilih _descendant_ yang memenuhi syarat _selector2_ pada elemen yang memenuhi syarat _selector1_.
- `selector1 > selector2`: Memilih _child_ yang memenuhi syarat _selector2_ pada elemen yang memenuhi syarat _selector1_.
- `selector1 + selector2`: Memilih elemen yang berada *tepat* setelah elemen yang memenuhi syarat _selector1_ yang memenuhi syarat _selector2_.
- `selector1 ~ selector2`: Memilih elemen yang berada setelah elemen yang memenuhi syarat _selector1_ yang memenuhi syarat _selector2_.

### Implementasi _Checklist_
#### Tahap 1: Setup Tailwind
Pada blok meta di setiap template HTML, saya menambahkan `<script src="https://cdn.tailwindcss.com"></script>` agar tailwind dapat digunakan.

#### Tahap 2: Mendesain Halaman Login
Pada halaman login, saya mengelompokkan elemen-elemen pada tugas sebelumnya ke dalam suatu elemen `<div>`. Setelah itu saya membuat elemen `<h1>` yang berfungsi menunjukkan identitas aplikasi (_To-Do List_). Saya mendesain kedua elemen tersebut dan pada akhirnya untuk menaruh keduanya di tengah halaman, saya memanfaatkan `mx-auto` (untuk penempatan `<div>` secara horizontal), `text-center` (untuk penempatan `<h1>` secara horizontal), dan flex box (untuk penempatan secara vertikal).

#### Tahap 3: Mendesain Halaman Register
Pada halaman ini, saya melakukan _copy-paste_ dari _style_ yang saya buat di halaman login dan menyesuaikannya dengan konten halaman ini. Tetapi, karena saya memanfaatkan `form.as_table` milik django form, _style_ dari elemen dalam `<div>` sebelumnya saya berikan dengan cara yang berbeda, yaitu dengan menggunakan _internal_ CSS dengan id elemen sebagai _selector_. Selain itu, agar tampilannya lebih seragam, saya mengganti `form.as_table` menjadi `form.as_div`.

#### Tahap 4: Mendesain Halaman To-Do List
Saya memindahkan posisi dari elemen-elemen agar mempercantik tampilannya. Setelah itu, saya membuat _navigation bar_ di atas halaman yang berisi link ke halaman utama aplikasi _to-do list_, username, dan tombol logout. Saya juga mengganti format _task_ yang awalnya ada dalam bentuk `<table>` ke bentuk `<div>` agar memudahkan saya dalam membuat _cards_. Setelah itu, saya memberikan _style_ pada elemen-elemen yang ada pada halaman tersebut.

#### Tahap 5: Mendesain Halaman Create Task
Pada halaman ini, saya melakukan _copy-paste_ dari _style_ yang saya buat di halaman login dan _to-do list_ (_navigation bar_-nya) dan menyesuaikannya dengan konten halaman ini. Namun, karena _navigation bar_ pada halaman _to-do list_ menampilkan _user name_ dan halaman ini tidak diberi _user name_ pada `context`, saya menghapus teks yang berisi _user name_-nya.

#### Tahap 6: Menerapkan _Responsive Design_
_Style_ yang telah saya buat memiliki permasalahan ketika diakses melalui perangkat dengan layar resolusi kecil seperti _smartphone_. Oleh karena itu, saya memanfaatkan _media queries_ pada Tailwind untuk mengubah properti-properti elemen sesuai dengan resolusinya. Contohnya pada resolusi kecil, saya me-_resize_ _task cards_ menjadi lebih kecil agar cukup untuk ditampilkan pada layar dengan resolusi tersebut.

#### Tahap 7: Memberikan Efek pada _Task Cards_ Ketika Di-_hover_
Pada `<div>` terluar dari _task cards_ saya membuat elemen tersebut di-scale menjadi 105% ukuran asli ketika dilakukan hover dengan menambahkan properti melalui _class_ `hover:scale-105`. Setelah itu, agar terlihat lebih cantik saya memperlambat durasi perubahan menjadi 300ms dengan menambahkan `duration-300`. Sayangnya, masih ada masalah pada _style_ _task cards_, yaitu ketika halaman di-_load_, _task cards_ menjadi hitam sebelum berubah menjadi warna yang seharusnya (putih) sehingga saya menambahkan `transition-transform` untuk mencegah warna dan properti lainnya yang tidak diinginkan berubah.

### Referensi
- https://tailwindcss.com/
- https://tailwindcss.com/docs/installation/play-cdn
- https://nerdcave.com/tailwind-cheat-sheet
- https://css-tricks.com/snippets/css/a-guide-to-flexbox/
- https://www.w3schools.com/html/html_css.asp
- https://www.w3schools.com/tags/
- https://www.w3schools.com/css/css_combinators.asp
- https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-4#tips--trik-untuk-css