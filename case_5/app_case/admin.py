from django.contrib import admin

# Register your models here.

from .models import Question, Tarefa

admin.site.register(Question)
admin.site.register(Tarefa)
