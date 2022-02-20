from rest_framework.serializers import ModelSerializer
from .models import *

### EXAMPLE SERIALIZER

# class ExampleSerializer(ModelSerializer):
#     class Meta:
#         model = Example
#         fields = '__all__'
#         # or
#         fields = ['body', 'etc...']