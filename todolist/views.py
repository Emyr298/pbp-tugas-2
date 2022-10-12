import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.utils import timezone

from todolist.models import Task

# Referensi
# https://stackoverflow.com/questions/4195242/django-model-object-with-foreign-key-creation
# https://www.geeksforgeeks.org/if-django-template-tags/

# Create your views here.
@login_required(login_url='/todolist/login/')
def todolist(request):
    user = request.user
    #task_list = Task.objects.filter(user__pk=user.pk)
    context = {
        'username': user.username,
        #'task_list': task_list,
    }
    return render(request, 'todolist_ajax.html', context)

@login_required(login_url='/todolist/login/')
def todolist_json(request):
    user = request.user
    task_list = Task.objects.filter(user__pk=user.pk)
    return HttpResponse(serializers.serialize('json', task_list), content_type='application/json')

@login_required(login_url='/todolist/login/')
def create_task_post(request):
    user = request.user
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = timezone.now()
        
        if title != '':
            Task.objects.create(user_id=user.id, title=title, description=description, date=date)
            
            user = request.user
            task_list = Task.objects.filter(user__pk=user.pk)
            return HttpResponse(serializers.serialize('json', task_list), content_type='application/json')
        else:
            return JsonResponse({'message': 'Title tidak boleh kosong'}, status=400);
    
    return JsonResponse({'message': 'Not Found'}, status=404);

@login_required(login_url='/todolist/login/')
def delete_task_delete(request, id):
    user = request.user
    task = Task.objects.get(pk=id)
    
    if user.id == task.user_id and request.method == 'DELETE':
        task.delete()
        return JsonResponse({'message': 'Success'}, status=200);
    
    return JsonResponse({'message': 'Not Found'}, status=404);

@login_required(login_url='/todolist/login/')
def create_task(request):
    user = request.user
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.now()
        
        if title != '':
            Task.objects.create(user_id=user.id, title=title, description=description, date=date)
            return redirect('todolist:todolist')
        else:
            messages.info(request, 'Title tidak boleh kosong')
    
    context = {}
    return render(request, 'create_task.html', context)

@login_required(login_url='/todolist/login/')
def set_finished(request, id):
    user = request.user
    task = Task.objects.get(pk=id)
    
    if user.id == task.user_id:
        task.is_finished = True
        task.save()
    
    return redirect('todolist:todolist')

@login_required(login_url='/todolist/login/')
def set_unfinished(request, id):
    user = request.user
    task = Task.objects.get(pk=id)
    
    if user.id == task.user_id:
        task.is_finished = False
        task.save()
    
    return redirect('todolist:todolist')

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    user = request.user
    task = Task.objects.get(pk=id)
    
    if user.id == task.user_id:
        task.delete()
    
    return redirect('todolist:todolist')

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