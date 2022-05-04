from django.shortcuts import render, redirect
from django.views import View
from execute.forms import TaskForm
from execute.models import Raspisanie


class RaspisanieTable(View):
    def get(self, request):
        para = Raspisanie.objects.all()
        return render(request, "../templates/index.html", {"para": para})


# def index(request):
#     tasks = Raspisanie.objects.order_by('-id')
#     return render(request, '../templates/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})

class CreatePara(View):
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