from django.test import TestCase

# Create your tests here.

from pybo.models import Question
from django.utils import timezone

for i in range(300):
    q = Question(
        subject = f'테스트 데이터: [{i:03d}]',
        content = f'테스트 데이터 내용: [{i:03d}]',
        create_date = timezone.now()
    )
    q.save()