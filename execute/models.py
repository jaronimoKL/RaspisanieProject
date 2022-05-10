from django.db import models


class Group(models.Model):
    # Группы
    group_name = models.CharField("Группа", max_length=20, default='')

    def __str__(self):
        return f"{self.group_name}"

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Cabinet(models.Model):
    # Кабинеты
    cabinet_name = models.CharField('Кабинета', max_length=55, default='')

    def __str__(self):
        return f"{self.cabinet_name}"

    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'


class Teacher(models.Model):
    last_name = models.CharField('Фамилия Преподавателя', max_length=55)
    first_name = models.CharField('Имя Преподавателя', max_length=55)
    third_name = models.CharField('Отчество Преподавателя', max_length=55)

    def __str__(self):
        return f"{self.last_name}"

    class Meta:
        verbose_name = 'ФИО Преподавателей'
        verbose_name_plural = 'Преподаватели'


class Pair(models.Model):
    number = models.PositiveSmallIntegerField('Номер пары', default=1)
    date = models.DateField('Дата пары')
    group = models.ForeignKey(Group,verbose_name="Группа", on_delete=models.CASCADE)
    cabinet = models.ForeignKey(Cabinet, verbose_name="Кабинет", on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, verbose_name="Преподаватель", on_delete=models.CASCADE)
    shortcut = models.BooleanField('Сокращенный день?', default=False)


    def __str__(self):
        return f"{self.date} - {self.teacher.last_name} - {self.group} - {self.cabinet}"

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'
