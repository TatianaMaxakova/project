from django.contrib import admin

from . import models
  
# Register your models here. 
 
@admin.register(models.Service) 
class ServiceAdmin(admin.ModelAdmin): 
    list_display = [field.name for field in models.Service._meta.get_fields()]  
    
@admin.register(models.Appointment) 
class AppointmentAdmin(admin.ModelAdmin): 
    list_display = [field.name for field in models.Appointment._meta.get_fields()]      


@admin.register(models.Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Visit._meta.get_fields()]