from datetime import datetime, timedelta
from django import views
from django.db.models import Q
from djangoProject.settings import USER_RANGE_START, USER_RANGE_END
from execute.models import Pair


class LessonsDetail(views.generic.ListView):
    model = Pair
    template_name = 'index.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Pair.objects.all().order_by('-date')
        else:
            return Pair.objects.filter(date__range=[datetime.now() - timedelta(days=USER_RANGE_START),
                                                    datetime.now() + timedelta(days=USER_RANGE_END)]).order_by('-date')


class LessonFilterView(views.generic.ListView):
    model = Pair
    template_name = 'index.html'

    def get_queryset(self):
        search = self.request.GET.get('search')
        start_date = self.request.GET.get("date_start")
        end_date = self.request.GET.get("date_end")
        if not self.request.user.is_superuser:
            start_date = ''
            end_date = ''
        if start_date == '' and end_date == '':
            if self.request.user.is_superuser:
                return Pair.objects.filter(
                    Q(teacher__first_name=search) | Q(teacher__last_name=search) |
                    Q(teacher__third_name=search) | Q(cabinet__cabinet_name=search) | Q(
                        group__group_name__startswith=search
                    )).order_by('-number').order_by('-date')
            else:
                return Pair.objects.filter(
                    Q(teacher__first_name=search) | Q(teacher__last_name=search) |
                    Q(teacher__third_name=search) | Q(cabinet__cabinet_name=search) | Q(
                        group__group_name__startswith=search
                    ), date__range=[datetime.now() - timedelta(days=USER_RANGE_START),
                                    datetime.now() + timedelta(days=USER_RANGE_END)]).order_by('-date')
        if end_date == '':
            end_date = f'{datetime.now():%Y-%m-%d}'
            return Pair.objects.filter(
                Q(teacher__first_name=search) | Q(teacher__last_name=search) |
                Q(teacher__third_name=search) | Q(cabinet__cabinet_name=search) |
                Q(date__range=[start_date, end_date]) | Q(
                    group__group_name__startswith=search
                )).order_by('-number').order_by('-date')
        if start_date == '':
            return Pair.objects.filter(
                Q(teacher__first_name=search) | Q(teacher__last_name=search) |
                Q(teacher__third_name=search) | Q(cabinet__cabinet_name=search) | Q(
                    group__group_name__startswith=search
                )).order_by('-number').order_by('-date')
        else:
            if self.request.user.is_superuser:
                return Pair.objects.filter(
                    Q(teacher__first_name=search) | Q(teacher__last_name=search) |
                    Q(teacher__third_name=search) | Q(cabinet__cabinet_name=search) |
                    Q(date__range=[start_date, end_date]) | Q(
                        group__group_name__startswith=search
                    )).order_by('-number').order_by('-date')
            else:
                return Pair.objects.filter(
                    Q(teacher__first_name=search) | Q(teacher__last_name=search) |
                    Q(teacher__third_name=search) | Q(cabinet__cabinet_name=search) | Q(
                        group__group_name__startswith=search
                    ), date__range=[datetime.now() - timedelta(days=USER_RANGE_START),
                                    datetime.now() + timedelta(days=USER_RANGE_END)]).order_by('-number').order_by('-date')
# class RaspisanieTable(View):
#     def get(self, request):
#         para = Raspisanie.objects.all()
#         return render(request, "../templates/index.html", {"para": para})


# class CreatePara(View):
#     def create(request):
#         error = ''
#         if request.method == 'POST':
#             form = TaskForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('home')
#             else:
#                 error = 'Форма была не верной'
#         form = TaskForm()
#         context = {
#             'form': form,
#             'error': error
#         }
#         return render(request, '../templates/tickets.html', context)