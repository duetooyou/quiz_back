from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import QuizSerializer, QuestionSerializer, UserSerializer
from store.models import Quiz, Question, Answer


class UserSignUpView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()


class QuizViewSet(ReadOnlyModelViewSet):
    permissions_classes = (permissions.AllowAny,)
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

    @action(detail=True,
            url_path='questions')
    def get_quiz_questions(self, request, pk=None):
        queryset = Question.objects.filter(quiz__id=pk).select_related('quiz')
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True,
            methods=['POST'],
            url_path='results')
    def get_quiz_result(self, request, pk=None):
        true_answers = list(Answer.objects.filter(question__id=pk, correct=True).
                            select_related('question').values_list('text', flat=True))
        if request.data.get('answer') == true_answers:
            return Response(True)
        else:
            return Response(False)
