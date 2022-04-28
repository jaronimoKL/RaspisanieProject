from django.db import models


# Create your models here.
class Task(models.Model):
    data = models.DateField('Дата', default='')
    day = models.CharField('День', max_length=55, default='')
    para1 = models.CharField('Первая пара', max_length=55, default='')
    kab1 = models.CharField('Кабинет', max_length=55, default='')
    para2 = models.CharField('Вторая пара', max_length=55, default='')
    kab2 = models.CharField('Кабинет', max_length=55, default='')
    para3 = models.CharField('Третья пара', max_length=55, default='')
    kab3 = models.CharField('Кабинет', max_length=55, default='')
    para4 = models.CharField('Четвертая пара', max_length=55, default='')
    kab4 = models.CharField('Кабинет', max_length=55, default='')
    para5 = models.CharField('Пятая пара', max_length=55, default='')
    kab5 = models.CharField('Кабинет', max_length=55, default='')
    para6 = models.CharField('Шестая пара', max_length=55, default='')
    kab6 = models.CharField('Кабинет', max_length=55, default='')

    def __str__(self):
        return self.day

    class Meta:
        verbose_name = 'Немешаева Анастасия Андреевна'
        verbose_name_plural = 'Немешаева А.А.'


class Task1(models.Model):
    data_1 = models.DateField('Дата', default='')
    day_1 = models.CharField('День', max_length=55)
    para1_1 = models.CharField('Первая пара', max_length=55)
    kab1_1 = models.CharField('Кабинет', max_length=55)
    para2_1 = models.CharField('Вторая пара', max_length=55)
    kab2_1 = models.CharField('Кабинет', max_length=55)
    para3_1 = models.CharField('Третья пара', max_length=55)
    kab3_1 = models.CharField('Кабинет', max_length=55)
    para4_1 = models.CharField('Четвертая пара', max_length=55)
    kab4_1 = models.CharField('Кабинет', max_length=55)
    para5_1 = models.CharField('Пятая пара', max_length=55)
    kab5_1 = models.CharField('Кабинет', max_length=55)
    para6_1 = models.CharField('Шестая пара', max_length=55)
    kab6_1 = models.CharField('Кабинет', max_length=55)

    def __str__(self):
        return self.day_1

    class Meta:
        verbose_name = 'Аминова Анастасия Сергеевна'
        verbose_name_plural = 'Аминова А.С.'
