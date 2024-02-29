from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import OpenAIQuery
from .serializers import OpenAIQuerySerializer
import openai
from django.conf import settings

class SubmitQueryView(APIView): # submit a query to the OpenAI api and save the response
    def post(self, request, *args, **kwargs):
        query_text = request.data.get('query_text')
        
        if not query_text:
            return Response({"error": "No query text provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        # set key from settings
        openai.api_key = settings.OPENAI_API_KEY

        try: # try to make API call
            response = openai.Completion.create(
              engine="text-davinci-003",
              prompt=query_text,
              max_tokens=100 # for testing
            )
            response_text = response.choices[0].text.strip()
            
            # save both query and response
            openai_query = OpenAIQuery.objects.create(query_text=query_text, response_text=response_text)
            serializer = OpenAIQuerySerializer(openai_query)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class QueryListView(APIView): # list all saved queries and their OpenAI responses.
    def get(self, request, *args, **kwargs):
        queries = OpenAIQuery.objects.all()
        serializer = OpenAIQuerySerializer(queries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)