from django.db import models


class Group(models.Model):
    # Группы
    name = models.CharField('Название группы', max_length=55, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группы'
        verbose_name_plural = 'Группы'


class Kabinet(models.Model):
    # Кабинеты
    name = models.CharField('Название кабинета', max_length=55, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'


class Prepod(models.Model):
    last_name = models.CharField('Фамилия Преподавателя', max_length=55, default='')
    first_name = models.CharField('Имя Преподавателя', max_length=55, default='')
    third_name = models.CharField('Отчество Преподавателя', max_length=55, default='')

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'ФИО Преподавателей'
        verbose_name_plural = 'Преподаватели'


class Raspisanie(models.Model):
    number = models.CharField('Номер пары', max_length=55, default='')
    data = models.DateField('Дата пары', max_length=55, default='')
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    kabinet = models.ForeignKey(Kabinet, on_delete=models.SET_NULL, null=True)
    last_name = models.ForeignKey(Prepod, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Расписание пары'
        verbose_name_plural = 'Расписание'
