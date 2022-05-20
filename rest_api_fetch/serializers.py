from rest_framework import serializers
from .models import Model


class ModelSerializer(serializers.ModelSerializer):

    brand_name = serializers.SlugRelatedField(read_only=True, slug_field='brand_name')

    class Meta:
        model = Model
        fields = ['brand_name','model_name','price','launch_date']
