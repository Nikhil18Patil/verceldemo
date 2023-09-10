from rest_framework import serializers
from .models import nik

class nikitem(serializers.ModelSerializer):
    

    class Meta:
        model = nik
        fields = ('name' , 'village')