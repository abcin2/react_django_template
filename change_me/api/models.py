from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.


### EXAMPLE MODEL:

# class Example(models.Model):
#     body = models.TextField(null=True, blank=True)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.body[0:50]