from django.contrib import admin
from .models import Workshop,Enrollment,WorkshopCategory,Instructor
# Register your models here.

class WorkshopAdmin(admin.ModelAdmin):
    exclude = ["workshopslug"]

admin.site.register(Workshop,WorkshopAdmin)
admin.site.register(WorkshopCategory)
admin.site.register(Instructor)