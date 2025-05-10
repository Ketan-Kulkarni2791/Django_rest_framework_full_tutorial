from rest_framework import serializers
from ..models import CarList, ShowroomList, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

# Serializer for CarList model
class CarSerializer(serializers.ModelSerializer):
    # Adding a custom field to the serializer
    discounted_price = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)
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
    # This will display all the information about cars associated with showroom.
    showrooms = CarSerializer(many=True, read_only=True)

    # This will display the information given in __str__ method in models.py 
    # showrooms = serializers.StringRelatedField(many=True)

    # This will display list of id of the cars associated with the showroom.
    # showrooms = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # This will display a hyperlink in order to show the dispaly of cars.
    # Also add "context={'request': request}" in showroom_view GET.
    # showrooms = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='car_detail'  # This name is from urls.py car_detail url name.
    # )

    class Meta:
        model = ShowroomList
        fields = '__all__'
