from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('test_list/', views.test_list, name='test_list'), 
    path('test_detail/<int:id>', views.test_detail, name='test_detail'), # no trailing slash so suffixes work
    # paths for other views
]

urlpatterns = format_suffix_patterns(urlpatterns)