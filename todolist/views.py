import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from todolist.models import Task

# Create your views here.
@login_required(login_url='/todolist/login/')
def todolist(request):
    user = request.user
    task_list = Task.objects.filter(user__pk=user.pk)
    context = {
        'username': user.username,
        'task_list': task_list,
    }
    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    user = request.user
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.now()
        Task.objects.create(user_id=user.id, title=title, description=description, date=date)
        return redirect('todolist:todolist')
    
    context = {}
    return render(request, 'create_task.html', context)

def register(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun berhasil dibuat')
            return redirect('todolist:login')
    
    context = { 'form': form }
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('todolist:todolist'))
            return response
        else:
            messages.info(request, 'Username atau password salah')
    
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    return response