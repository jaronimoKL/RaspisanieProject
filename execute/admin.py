from django.contrib import admin
from execute.models import Group, Kabinet, Prepod, Raspisanie


# Register your models here.
@admin.register(Raspisanie)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['number', 'data', 'kabinet', 'group', 'last_name']
    list_editable = ['data', 'kabinet', 'group']
    ordering = ['data', 'number']
    search_fields = ['last_name__last_name', 'data']


admin.site.register(Group)
admin.site.register(Kabinet)
admin.site.register(Prepod)