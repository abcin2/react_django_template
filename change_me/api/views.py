from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    return Response('API is up and running with REST framework!')

## SHOULD CREATE API VIEWS FOR EACH ITEM WITHIN EACH ROUTE ALL W/ GET REQUESTS

### EXAMPLES

# @api_view(['GET'])
# def getExamples(request):
#     examples = Example.objects.all()
#     serializer = ExampleSerializer(examples, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getExample(request, pk):
#     examples = Example.objects.get(id=pk)
#     serializer = ExampleSerializer(examples, many=False)
#     return Response(serializer.data)

# @api_view(['POST'])
# def createExample(request):
#     data = request.data
#     example = Example.objects.create(
#         body=data['body']
#     )
#     serializer = ExampleSerializer(example, many=False)
    
#     return Reponse(serializer.data)

# @api_view(['PUT'])
# def updateExample(request, pk):
#     data = request.data
#     example = Example.objects.get(id=pk)
#     serializer = ExampleSerializer(instance=example, data=data)
    
#     if serializer.is_valid():
#         serializer.save()
        
#     return Response(serializer.data)

# @api_view(['DELETE'])
# def deleteExample(request, pk):
#     example = Example.objects.get(id=pk)
#     example.delete()
#     return Response('Note was deleted!')