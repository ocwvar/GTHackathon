from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class RequestEvent(APIView):
    def get(self, request, *args, **kwargs):
        return Response("hello world!")
