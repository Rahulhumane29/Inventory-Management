from rest_framework import serializers
from .models import Inventory_items

class Itemserializers(serializers.ModelSerializer):
    class Meta:
        model = Inventory_items
        fields = '__all__'