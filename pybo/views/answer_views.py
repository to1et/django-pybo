from django.shortcuts import render, get_object_or_404, redirect #redirect 방향을 재설정
from ..models import Question, Answer
from django.utils import timezone
from ..forms import AnswerForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='common:login')
def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    # print(request.method)
    # print(request.GET)       #dict
    # print(request.POST)      #dict
    # content = request.POST['content']           #1) 키가 없으면, 예외 발생
    # print('[content]', content)

    # content = request.POST.get('content', '')       #2) 키가 없으면, None 리턴, 키가 없을 때 기본값('')을 줄 수 있다.
    # print('get(content)', content)
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question #FK 직접 처리
            answer.save()
            return redirect ('pybo:detail', question_id=question.id)
        else:
            form = AnswerForm()
            
        context = {'question': question, 'form': form}
        return render(request, 'pybo/question_detail.html', context)
    # question.answer_set.create(content=request.POST.get('content'), # answer_set:관계매니저
    #                            #관계매니저는 모델명_set의 구조를 갖는다. fk가 Answer에 있기 때문에
    #                            #answer_set이 자동으로 생긴다.
    #                            create_date=timezone.now())
    # return redirect('pybo:detail', question_id=question.id)

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """
    pybo 답변수정
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('pybo:detail', question_id=answer.question.id)
    
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('pybo:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)

    context = {'answer': answer, 'form': form}

    return render(request, 'pybo/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    """
    pybo 답변삭제
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제 권한이 없습니다')
    else:
        answer.delete()
    return redirect('pybo:detail', question_id=answer.question.id)

