from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','employee_name','employee_designation']
    search_fields=['employee_name']