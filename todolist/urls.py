from django.urls import path
from todolist.views import delete_task, todolist, create_task, login_user, register, logout_user, set_finished, set_unfinished, delete_task

app_name = 'todolist'

urlpatterns = [
    path('', todolist, name='todolist'),
    path('create-task/', create_task, name='create_task'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('set_finished/<int:id>/', set_finished, name='set_finished'),
    path('set_unfinished/<int:id>/', set_unfinished, name='set_unfinished'),
    path('delete_task/<int:id>/', delete_task, name='delete_task'),
]