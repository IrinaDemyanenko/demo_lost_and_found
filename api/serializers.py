from rest_framework import serializers
from finditem.models import FoundItem


class FoundItemSearchSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=500)
    found_date = serializers.DateField()
    station = serializers.IntegerField()
    category = serializers.IntegerField()


class FoundItemSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    station = serializers.CharField(source='station.name')

    class Meta:
        model = FoundItem
        fields = ['description', 'found_date', 'station', 'category', 'image_url', 'status']
