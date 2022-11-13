from django.contrib import admin
from .models import StudentData
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class StudentResource(resources.ModelResource):
    class Meta:
        model = StudentData


class StudentAdmin(ImportExportModelAdmin):
    resource_class = StudentResource


admin.site.register(StudentData, StudentAdmin)
