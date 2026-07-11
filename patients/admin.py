from django.contrib import admin
from .models import Patient, Doctor, Visit, Department, Appointment

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'sub_county', 'created_at')
    search_fields = ('first_name', 'last_name', 'phone')
    list_filter = ('sub_county', 'gender')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'specialty', 'department', 'phone')
    search_fields = ('first_name', 'last_name', 'specialty')
    list_filter = ('department',)

@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'visit_date', 'diagnosis', 'status')
    list_filter = ('status', 'visit_date')
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__first_name')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')
    search_fields = ('name',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'appointment_date', 'status', 'created_at')
    list_filter = ('status', 'appointment_date')
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__first_name')
    date_hierarchy = 'appointment_date'