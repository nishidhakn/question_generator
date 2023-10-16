from django.contrib import admin
from app1.models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display=['class1','subject','questiontype','question']
admin.site.register(Question,QuestionAdmin)
