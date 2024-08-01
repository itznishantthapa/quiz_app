from django.urls import path
from .views import create_question, getQuestions,getQuestionById

urlpatterns = [
    path('questions/', getQuestions, name='get-questions'),
    path('question/<int:id>/', getQuestionById, name='get-question-id'),
    path('question/create/', create_question, name='create-question')
]
