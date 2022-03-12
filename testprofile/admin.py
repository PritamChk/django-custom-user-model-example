from django.contrib import admin

from .models import Department, Student


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'id','domain', 'degree')
    search_fields = ('name',)
    readonly_fields = ['id']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'university_roll', 'current_sem', 'depertment')
    list_filter = ('current_sem', 'depertment')
    # readonly_fields = ['user']
