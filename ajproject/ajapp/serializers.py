from rest_framework import serializers
from ajapp.models import Countries,States,Cities

class CountryAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = '__all__'
class StateAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields='__all__'
