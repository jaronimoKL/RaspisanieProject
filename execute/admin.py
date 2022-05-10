from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from execute.models import Group, Cabinet, Teacher, Pair


# Register your models here.
@admin.register(Pair)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['number', 'teacher', 'date', 'group', 'cabinet', 'shortcut']
    list_editable = ['date', 'cabinet', 'group', 'teacher', 'shortcut']
    # ordering = ['data', 'number']
    search_fields = ['teacher__last_name', 'date']
    list_filter = (('date', DateRangeFilter), )
    save_as = True


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'third_name')
    search_fields = ('first_name', 'last_name', 'third_name')


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    search_fields = ['group_name__startswith']
    ordering = ['group_name']


@admin.register(Cabinet)
class CabinetAdmin(admin.ModelAdmin):
    search_fields = ['cabinet_name__startswith']
    ordering = ['cabinet_name']


admin.site.site_header = 'ЕЭТК'
admin.site.index_title = 'Админка сайта'