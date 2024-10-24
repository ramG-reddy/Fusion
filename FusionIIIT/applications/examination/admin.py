from django.contrib import admin

from .models import authentication, grade, hidden_grades

# Register your models here.

admin.site.register(hidden_grades)
admin.site.register(authentication)
admin.site.register(grade)
