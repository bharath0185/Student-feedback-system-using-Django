

# Register your models here.
from django.contrib import admin
from .models import Student, Feedback

admin.site.register(Student)
admin.site.register(Feedback)
