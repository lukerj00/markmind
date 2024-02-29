# openai_interactions/urls.py
from django.urls import path
from .views import SubmitQueryView, QueryListView

urlpatterns = [
    path('submit-query/', SubmitQueryView.as_view(), name='submit_assignment_feedback_query'),
    path('list-queries/', QueryListView.as_view(), name='list_assignment_feedback_queries'),
]
