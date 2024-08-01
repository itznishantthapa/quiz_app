from rest_framework import serializers

from .models import Option, Question, QuizAttempt, QuestionAttempt


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'option', 'isCorrect']
        required = ['option', 'isCorrect']


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'question', 'category', 'level', 'options']
        required = ['question', 'category', 'level', 'options']

    def create(self, validated_data):
        options = validated_data.pop('options')
        question = Question.objects.create(**validated_data)

        for option in options:
            Option.objects.create(questionId=question, **option)

        return question
    

class QuestionAttemptSerializer(serializers.ModelSerializer):
    question=QuestionSerializer()
    class Meta:
        model = QuestionAttempt
        fields = ['id','question', 'isCorrect']



class QuizAttemptSerializer(serializers.ModelSerializer):
    questions_attempt=QuestionAttemptSerializer(many=True)
    class Meta:
        model = QuestionAttempt
        fields = ['id','attempted_date','total_score','questions_attempt']
    
    def create(self, validated_data,context):
        pass