from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect #redirect 방향을 재설정

from ..models import Question


def index(request):
    """
    pybo 목록 출력
    """ # document string 함수 정의의 제일 첫번째로 나와야 한다.
    # 입력 파라미터
    page = request.GET.get('page', '1')
    # 조회
    question_list = Question.objects.order_by('-create_date')
    #페이징 처리
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}

    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)
