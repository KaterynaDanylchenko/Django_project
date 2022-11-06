from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Question

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'catalog/detail.html', {'question': question})
