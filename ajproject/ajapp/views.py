from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from ajapp.models import Countries, States, Cities
from ajapp.serializers import CountryAPISerializer, StateAPISerializer
from django.views.generic import View,TemplateView
# Create your views here.

class HomePage(View):
    def get(self,request,*args,**kwargs):
        countries = Countries.objects.all()
        return render(request,'ajapp/index.html',{'countries':countries})
    def post(self,request,*args,**kwargs):
        return HttpResponse('')

class CountryAPIView(APIView):
    def get(self, request, format=None):
        countries_qs = Countries.objects.all()
        serializer = CountryAPISerializer(countries_qs, many=True)
        serialized_data = serializer.data
        return Response(serialized_data)


class StateAPIView(APIView):
    def get(self, request,name, format=None):
        country_obj = Countries.objects.get(name=name)
        states_qs = country_obj.statesofcountry.all()
        serializer = StateAPISerializer(states_qs, many=True)
        serialized_data = serializer.data
        return Response(serialized_data)


class CityAPIView(APIView):
    def get(self, request, pk, name, format=None):
        country_obj = Countries.objects.get(name=name)
        state_obj = States.objects.get(pk=pk)
        cities_qs = state_obj.citiesofstate.all()
        serializer = StateAPISerializer(cities_qs, many=True)
        serialized_data = serializer.data
        print(len(serialized_data))
        return Response(serialized_data)

def doNothing(request):
    if request.method =='POST':
        return HttpResponse()
