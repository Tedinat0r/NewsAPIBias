
from rest_framework.parsers import JSONParser
from RequestsModule import NewsRequestsGen
from rest_framework.decorators import *
from rest_framework.response import *
import VocabularyWeighter.VocabularyWeighter as VW
from rest_framework.serializers import *
from rest_framework.renderers import JSONRenderer
stories_dict = {}

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

stories_dict = {}

from django.db import models


class StoryModel(models.Model):
    query = models.CharField(max_length=100)
    source_bias = models.CharField(max_length=100)

    def __str__(self):
        return self.query, self.source_bias



class StorySerializer(ModelSerializer):
    class Meta:
        model = StoryModel
        fields = "__all__"


@api_view(['POST'])
def send_query(request):
    serializer = StorySerializer(data=request.data)
    if serializer.is_valid():
        story_model = serializer.save()
        NewsRequestsGen.story_inst_struct(story_model, stories_dict)
        VW.source_bias_comparator(stories_dict)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        print('Great Success!!!')
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def return_bias(request):
    model = list(stories_dict.values())[-1][-1]
    serializer = StorySerializer(model, many=False)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)










