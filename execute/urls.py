from django.urls import path
from execute import views

urlpatterns = [
    path('', views.LessonsDetail.as_view(), name='lessons_detail'),
    path('filter/', views.LessonFilterView.as_view(), name='lesson_filter'),
]
