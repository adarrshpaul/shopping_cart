from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.http import HttpResponse

#import the views for implementing class based views
from rest_framework.views import APIView

#Used class based views
class Books(APIView):
    def get(self, request):  
        author = request.GET.get('author')
        return Response({'author': f'{author}'}, status=status.HTTP_200_OK)
    def post(self, request):
        return Response({"title": ""}, status=status.HTTP_201_CREATED )
    
class Book(APIView):
    def get(self, request, pk):
        return Response(f"Hi, this is the {pk}", status=status.HTTP_200_OK)


# Using the api_view of DRF makes it very easy to make APIs in Django
# @api_view(['GET', 'POST'])
# def books(request, pk): 
#     return Response("any data", status=status.HTTP_200_OK)

# #Using native django HTTP Response
# def books(request):
#         return HttpResponse("data")
