from django.contrib import admin
from .models import Student

# @admin.register(Question)
# class QuestionModel(admin.ModelAdmin):
#     list_display=("text","pub_date")
#     list_filter=("text","pub_date")
#     date_hierachy=("pub_date")
    
# Register your models here.
admin.site.register(Student)