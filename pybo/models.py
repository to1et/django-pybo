from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_question')
                                #이름 변경 voter의 User와 겹치기 때문에 이를 방지하기 위해 이름을 변경해준다.
    subject = models.CharField('제목', max_length=200,
                                help_text='질문의 제목을 한 줄로 작성하세요.')
    content = models.TextField('내용', help_text='질문의 내용을 상세히 작성하세요.')
    create_date = models.DateTimeField('생성일')
    modify_date = models.DateTimeField(null=True, blank=True)
    
    voter = models.ManyToManyField(User, related_name='voter_question')
    def __str__(self):
        return f'{self.id} {self.subject}'

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField('답변 내용')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    voter = models.ManyToManyField(User, related_name='voter_answer')
    def __str__(self):
        return self.content
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True,
                                 on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.content