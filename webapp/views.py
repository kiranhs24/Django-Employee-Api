# -*- coding: utf-8 -*-

# Create your views here.

from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employee
from . serializers import employeeSerializer
from django.views.decorators.csrf import csrf_exempt
from braces.views import CsrfExemptMixin

class Object(CsrfExemptMixin, APIView):
    authentication_classes = []

class employeeList(APIView) :

    def get(self,request):
        employee1 =  employee.objects.all()
        serializer1 = employeeSerializer(employee1, many=True)
        return Response(serializer1.data)

    def post(self, request, format=None):
        serializer1 = employeeSerializer(data=request.data)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data, status=status.HTTP_201_CREATED)
        return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)