from django.shortcuts import render

from rest_framework import viewsets
from .serailizers import nikitem
from .models import nik
import requests
# Create your views here.


class NikItemViews(viewsets.ModelViewSet):
    # define queryset
    queryset = nik.objects.all()
     
    # specify serializer to be used
    serializer_class = nikitem


def index(request):
    api_url = "http://127.0.0.1:8000/api/"  
    response = requests.get(api_url)
    people = response.json()  # Assuming the API response is a list of people
    return render(request, 'index.html', {'people': people})