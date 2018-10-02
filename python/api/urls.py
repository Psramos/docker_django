from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = {
    url(r'^health', views.health)
}

urlpatterns = format_suffix_patterns(urlpatterns)