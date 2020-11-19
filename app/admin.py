from django.contrib import admin
from .models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','phone_number','email']

admin.site.register(Employee,EmployeeAdmin)
