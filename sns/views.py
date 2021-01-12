from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from sns.serializers import SNSSerializer


class SNSView(generics.CreateAPIView):
    serializer_class = SNSSerializer
