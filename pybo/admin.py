from django.contrib import admin

# Register your models here.
from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    list_display = ['id', 'subject', 'create_date']
    ordering = ['-id'] # 오름차순 정렬. 앞에 -를 붙이면 내림차순 정렬이 된다. 
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)

