from django.shortcuts import render, get_object_or_404, redirect #redirect 방향을 재설정
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

# Create your views here.

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

def question_create(request):
    """
    pybo 질문등록
    """
    if request.method == 'POST': # submit을 통한 POST 요청, 사용자가 입력한 데이터가 들어감
        form = QuestionForm(request.POST)
        if form.is_valid(): # 유효성 검사가 통과하면 아래 실행. (models.py에서 subject, content가 요구됨. 모두 입력되면 유효성검사 통과)
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:                        # GET 요청
        form = QuestionForm() #비어있는 데이터가 들어간다.

    context = {'form': form} #is_valid()가 false가 되면 이쪽으로 바로 넘어옴.
                             #POST 일때는 if아래의 form이, GET 일때는 else 아래의 내용이 비어있는 form이 넘어옴
                             #사용자가 잘못 입력한 값이 있을 경우 if아래의 form이 그것을 기억해 두었다가 반환해줌.
    return render(request, 'pybo/question_form.html', {'form': form})