from django.shortcuts import render

from django.http import HttpResponse
from django.utils import timezone


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class IndexView(generic.ListView):
    template_name = 'catalog/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]
