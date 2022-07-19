from django.views import generic
from .models import Quiz


class QuizListView(generic.ListView):
    model = Quiz
    context_object_name = 'quizzes'
    # template_name = 'store/quiz_list.html'


class QuizDetailView(generic.DetailView):
    model = Quiz
