# get data from model to json to json
from rest_framework import routers, serializers, viewsets
from .models import Job

# Serializers define the API representation.
class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields ='__all__'
