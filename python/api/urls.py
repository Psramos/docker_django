from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'api'

urlpatterns = [
    url(r'^health', views.health)
]

urlpatterns = format_suffix_patterns(urlpatterns)