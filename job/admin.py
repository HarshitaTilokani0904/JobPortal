from django.contrib import admin
from .models import * 
from .models import StudentUser,Recruiter
# Register your models here.
admin.site.register(StudentUser)
admin.site.register(Recruiter)
admin.site.register(Job)