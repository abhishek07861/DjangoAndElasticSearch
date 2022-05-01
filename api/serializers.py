from pyexpat import model
from .models import ElasticSearchDemo
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import *

class NewsDocumentSerializer(DocumentSerializer):
    class Meta:
        model = ElasticSearchDemo
        document = NewsDocument
        fields = ('title','content')
        
        def get_location(self,obj):
            try:
                return obj.location.to_dict()
            except:
                return {}
            
            
class StateDocumentSerializer(DocumentSerializer):
    class Meta:
        model = SateCity
        document = StateDocument
        fields = ('city','growth','latitude','longitude','state')
        
        def get_location(self,obj):
            try:
                return obj.location.to_dict()
            except:
                return {}