# openai_interactions/serializers.py
from rest_framework import serializers
from .models import OpenAIQuery

class OpenAIQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenAIQuery
        fields = ['id', 'assignment_feedback_query', 'assignment_feedback_response']