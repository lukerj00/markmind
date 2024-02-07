from django.contrib import admin
from django.apps import apps
from .models import *

api_models = apps.get_app_config('api').get_models()

# register all models on admin site
for model in api_models:
    admin.site.register(model)

### testing ###
# admin.site.register(Test)

