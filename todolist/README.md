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

### Tag HTML5

### Tipe-Tipe CSS _Selector_

### Implementasi _Checklist_

### Referensi
- https://tailwindcss.com/
- https://tailwindcss.com/docs/installation/play-cdn
- https://nerdcave.com/tailwind-cheat-sheet
- https://css-tricks.com/snippets/css/a-guide-to-flexbox/
- https://www.w3schools.com/html/html_css.asp