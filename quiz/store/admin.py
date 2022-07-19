from django.contrib import admin

from .forms import QuestionFormSet
from .models import Quiz, Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    formset = QuestionFormSet
    min_num = 4
    max_num = 4


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerInline
    ]
    list_filter = ('quiz__name',)
