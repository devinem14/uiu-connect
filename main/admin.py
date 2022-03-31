from django.contrib import admin
from .models import ToDoList, Item
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(ToDoList)
admin.site.register(Item)
