from django.forms import ModelForm, TextInput
from execute.models import Raspisanie


class TaskForm(ModelForm):
    class Meta:
        model = Raspisanie
        fields = ["number", "data", "group", "kabinet", "last_name"]
        widgets = {
            "number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер пары'
            }),
            "data": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату пары'
            }),
            "group": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите группу'
            }),
            "kabinet": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите кабинет'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите фамилию препода'
            })
        }



# class TaskForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ["data", "day", "para1", "kab1", "para2", "kab2", "para3", "kab3", "para4", "kab4", "para5", "kab5", "para6", "kab6"]
#         widgets = {
#         "data": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите название'
#         }),
#         "day": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите описание'
#         }),
#         "para1": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "para2": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "para3": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "para4": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "para5": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "para6": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "kab1": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "kab2": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "kab3": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "kab4": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "kab5": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "kab6": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         })
#         }
#
#
# class TaskForm1(ModelForm):
#     class Meta:
#         model = Task1
#         fields = ["data_1", "day_1", "para1_1", "kab1_1", "para2_1", "kab2_1", "para3_1", "kab3_1", "para4_1", "kab4_1", "para5_1", "kab5_1", "para6_1", "kab6_1"]
#         widgets = {
#         "data_1": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите название'
#         }),
#         "day_1": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите описание'
#         }),
#         "para1_1": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "para2_1": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "para3_1": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "para4_1": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "para5_1": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "para6_1": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "kab1_1": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "kab2_1": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "kab3_1": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "kab4_1": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "kab5_1": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         }),
#         "kab6_1": TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Введите что-то крутое'
#         })
#         }