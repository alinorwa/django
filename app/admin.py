from django.contrib import admin
from .models import *

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fields = ["date", "question"]

admin.site.register(Question , QuestionAdmin)
admin.site.register(Choice)