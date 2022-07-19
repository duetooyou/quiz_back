from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import QuizViewSet, UserSignUpView

app_name = 'api'

api_router = routers.DefaultRouter()
api_router.register(r'quizzes', QuizViewSet)


urlpatterns = [
    path('', include(api_router.urls)),
    path('signin/', UserSignUpView.as_view()),
    path('tokens/', TokenObtainPairView.as_view()),
    path('tokens/refresh/', TokenRefreshView.as_view()),
]
