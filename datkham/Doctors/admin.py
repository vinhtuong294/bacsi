from django.contrib import admin
from .models import UserModel, Role, Department, Doctor, Patient, Shift, Schedule, MedicalRecord, Article

# Đăng ký các model với admin site
admin.site.register(UserModel)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Shift)
admin.site.register(Schedule)
admin.site.register(MedicalRecord)
admin.site.register(Article)
