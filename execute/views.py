from django.shortcuts import render, redirect

# Create your views here.
from execute.forms import TaskForm
from execute.models import Task


def index(request):
    tasks = Task.objects.order_by('-id')
    # order_by - сортирует по конкретному полю ('title')[:5] - ограничил до 5 записей
    return render(request, '../templates/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была не верной'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, '../templates/tickets.html', context)