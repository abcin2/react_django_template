from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
   path('', views.getRoutes, name='API routes') 
   ### EXAMPLE
   # path('examples/', views.getExamples, name="examples"),
   # path('examples/<str:pk>/', views.getExample, name="example"),
   # path('examples/<str:pk>/update/', views.updateExample, name="update-example"),
   # path('examples/<str:pk>/delete/', views.deleteExample, name="delete-example"),
   # path('examples/create/', views.createExample, name="create-example"),
]