from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from BooksList.models import Books
from BooksList.serializers import BookSerializer, bookReviewSerializer
# from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET", "POST"])
# def API_Home(request, *args, **kwargs): 
#     # Check if the request contains data for book reviews
#     if 'Rating' in request.data and 'Review' in request.data:
#         # Handle book reviews
#         serializer = bookReviewSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             print(serializer.data)
#             return Response(serializer.data)
#     else:
#         # Handle books data
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             print(serializer.data)
#             return Response(serializer.data)
#     return Response({"error": "Invalid data"}, status=400)
def API_Home(request, *args, **kwargs): 
    serializer = BookSerializer(data= request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
