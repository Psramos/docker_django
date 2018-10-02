from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Dummy
from api.serializers import DummySerializer


@api_view(['GET'])
def health():
    return HttpResponse('Everything ok!')
