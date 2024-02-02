from django.db import models

# Create your models here.

class Test(models.Model):
    field_a = models.CharField(max_length=50)
    field_b = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
