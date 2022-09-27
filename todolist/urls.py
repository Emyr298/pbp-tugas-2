from django.urls import path
from todolist.views import todolist, create_task, login_user, register, logout_user

app_name = 'todolist'

urlpatterns = [
    path('', todolist, name='todolist'),
    path('create-task/', create_task, name='create_task'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
]