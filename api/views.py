from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import *
from .serializers import *
from rest_framework.response import Response

# Create your views here.

class CounrtyViewsets(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def list(self,request):
        queryset = Country.objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)


class CharacteristicViewsets(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer

    def list(self,request):
        queryset = Characteristic.objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)


class LeagueViewsets(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

    def list(self,request):
        queryset = League.objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    
class FootballClubViewsets(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = FootballClub.objects.all()
    serializer_class = FootballClubSerializer

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    
    def list(self,request):
        queryset = FootballClub.objects.all()
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        queryset = self.queryset.get(pk=pk)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

    def update(self,request,pk=None):
        queryset = self.queryset.get(pk=pk)
        serializer = self.serializer_class(queryset, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=400)
        
    def destroy(self,request,pk=None):
        queryset = self.queryset.get(pk=pk)
        queryset.delete()
        return Response(status=204)
