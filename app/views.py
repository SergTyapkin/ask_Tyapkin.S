from django.http import HttpResponse
from django.shortcuts import render


from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from blog.models import Question


# Create your views here.
def listing(request):
    return render(request, "listing.html", {})


answers_dict = [
    {
        'id': idx,
        'title': f'title{idx}',
        'text': 'text text',
    } for idx in range(10)
]


def login(request):
    return render(request, 'login.html', {})


def signup(request):
    return render(request, 'signup.html', {})


def ask(request):
    return render(request, 'ask.html', {})


def hot(request):
    questions = Question.objects.all()
    paginator = Paginator(questions, 4)
    page = request.GET.get('page', 1)
    questions = paginator.get_page(page)
    return render(request, 'hot.html', {'questions': questions})


def tag(request, tag):
    questions = Question.objects.filter()
    paginator = Paginator(questions, 4)
    page = request.GET.get('page', 1)
    questions = paginator.get_page(page)
    return render(request, 'tag.html', {'tag': tag})


def listing(request):
    questions = Question.objects.all()
    paginator = Paginator(questions, 2)
    page = request.GET.get('page', 1)
    questions = paginator.get_page(page)
    return render(request, 'index.html', {'questions': questions})


def settings(request):
    return render(request, 'settings.html', {})


def question(request):
    paginator = Paginator(answers_dict, 2)
    page = request.GET.get('page', 1)
    answers = paginator.get_page(page)
    return render(request, 'question.html', {'answers': answers})


def question(request, id):
    question = Question.objects.get(id=id)
    paginator = Paginator(answers_dict, 2)
    page = request.GET.get('page', 1)
    answers = paginator.get_page(page)
    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
    })
