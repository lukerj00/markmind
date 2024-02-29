from django.db import models

class OpenAIQuery(models.Model):
    query_text = models.TextField()
    response_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)