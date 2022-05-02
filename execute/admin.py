from django.contrib import admin
from execute.models import Group, Kabinet, Prepod, Raspisanie


# Register your models here.
# @admin.register(Task)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ("data", "day", "para1", "kab1", "para2", "kab2", "para3", "kab3", "para4", "kab4", "para5", "kab5", "para6", "kab6")
#     search_fields = ("data", "day")
#
#
# admin.site.register(Task1)
admin.site.register(Group)
admin.site.register(Kabinet)
admin.site.register(Prepod)
admin.site.register(Raspisanie)