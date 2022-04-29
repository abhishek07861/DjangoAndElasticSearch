from django.shortcuts import render
from django.http import JsonResponse
import requests,json
from .models import *
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend,
)
from .documents import *
from .serializers import *

# Create your views here.
# d7ef92a516c84fa3bee10ee4c06cc78b d7ef92a516c84fa3bee10ee4c06cc78b
def random_data_feeding():
    url = 'https://newsapi.org/v2/everything?q=apple&from=2022-04-28&to=2022-04-28&sortBy=popularity&apiKey=d7ef92a516c84fa3bee10ee4c06cc78b'
    r = requests.get(url)
    payload = json.loads(r.text)
    count = 1
    for data in payload.get('articles'):
        print(count)
        ElasticSearchDemo.objects.create(
            title = data.get('title'),
            content = data.get('content')
        )
        
def index(request):
    random_data_feeding()
    return JsonResponse({'status':200})


class PublisherDocumentView(DocumentViewSet):
    document = NewsDocument
    serializer_class = NewsDocumentSerializer
    filter_backends = [
        FilteringFilterBackend,
        CompoundSearchFilterBackend,
    ]
    
    search_fields = ('title','content')
    multi_match_search_fields = ('title','content')
    fields_fields = {
        'title':'title',
        'content':'content',
    }