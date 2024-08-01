from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from .serializers import QuestionSerializer
from django.http import Http404, JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Question

# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_question(request):
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message": "Question created successfully!", "status": HTTP_201_CREATED})
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getQuestions(request):
    questions = Question.objects.all()
    # questions = Question.objects.()
    serializer = QuestionSerializer(instance = questions , many = True)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getQuestionById(request,id):
    question = get_object_or_404(Question, pk=id)
    # questions = Question.objects.()
    serializer = QuestionSerializer(instance = question)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
