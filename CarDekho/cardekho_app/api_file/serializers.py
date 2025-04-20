from rest_framework import serializers
from ..models import CarList, ShowroomList


class CarSerializer(serializers.ModelSerializer):
    # Adding a custom field to the serializer
    discounted_price = serializers.SerializerMethodField()
    class Meta:
        model = CarList
        fields = '__all__'

    def get_discounted_price(self, obj):
        discount_percentage = 0.10
        discounted_price = float(obj.price) * (1 - discount_percentage)
        return discounted_price
    
    
    # Field level validations
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Price should be positive.')
        elif value <= 20000:
            raise serializers.ValidationError('Price should be greater than 20000.')
        return value
    
    # Object level validations
    def validate(self, attrs):
        if attrs['name'] == attrs['description']:
            raise serializers.ValidationError('Name and description should not be same.')
        return attrs


class ShowroomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowroomList
        fields = '__all__'