from django.forms import ModelForm, TextInput


# class TaskForm(ModelForm):
#     class Meta:
#         model = Raspisanie
#         fields = ["number", "data", "group", "kabinet", "last_name"]
#         widgets = {
#             "number": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите номер пары'
#             }),
#             "data": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите дату пары'
#             }),
#             "group": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите группу'
#             }),
#             "kabinet": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите кабинет'
#             }),
#             "last_name": TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Введите фамилию препода'
#             })
#         }