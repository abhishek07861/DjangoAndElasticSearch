from django_elasticsearch_dsl import (
    Document,fields,Index
)

from .models import ElasticSearchDemo,SateCity

PUBLISHER_INDEX = Index('elastic_search_demo')
PUBLISHER_INDEX.settings(
    number_of_shards = 1,
    number_of_replicas = 1
)

# @PUBLISHER_INDEX.doc_type
class NewsDocument(Document):
    id = fields.IntegerField(attr="id")
    title = fields.TextField(
        fields = {
            'raw':{
                'type':'keyword',
            }
        }
    )
    content = fields.TextField(
        fields = {
            'raw':{
                'type':'keyword',
            }
        }
    )
    class Django(object):
        model = ElasticSearchDemo
        
@PUBLISHER_INDEX.doc_type
class StateDocument(Document):
    id = fields.IntegerField(attr="id")
    city = fields.TextField(
        fields = {
            'raw':{
                'type':'keyword',
            }
        }
    )
    growth = fields.TextField(
        fields = {
            'raw':{
                'type':'keyword',
            }
        }
    )
    latitude = fields.TextField(
        fields = {
            'raw':{
                'type':'keyword',
            }
        }
    )
    longitude = fields.TextField(
        fields = {
            'raw':{
                'type':'keyword',
            }
        }
    )
    state = fields.TextField(
        fields = {
            'raw':{
                'type':'keyword',
            }
        }
    )
    class Django(object):
        model = SateCity