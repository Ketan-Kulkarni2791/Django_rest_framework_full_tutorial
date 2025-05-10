from .models import (CarList, ShowroomList, Review)
from django.http import JsonResponse
from .api_file.serializers import (
    CarSerializer, 
    ShowroomListSerializer,
    ReviewSerializer
)
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,    
    TokenAuthentication
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    AllowAny
)


class ReviewDetailView(mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ReviewListView(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ShowroomwView(APIView):

    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser]

    def get(self, request):
        showrooms = ShowroomList.objects.all()
        serializer = ShowroomListSerializer(
            showrooms, 
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ShowroomListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowroomDetailView(APIView):
    def get(self, pk):
        try:
            showroom = ShowroomList.objects.get(pk=pk)
            serializer = ShowroomListSerializer(showroom)
            return Response(serializer.data)
        except ShowroomList.DoesNotExist:
            return Response({'error': 'Showroom not found'}, status=404)
    
    def put(self, request, pk):
        try:
            showroom = ShowroomList.objects.get(pk=pk)
            serializer = ShowroomListSerializer(showroom, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ShowroomList.DoesNotExist:
            return Response({'error': 'Showroom not found'}, status=404)
    
    def delete(self, pk):
        try:
            showroom = ShowroomList.objects.get(pk=pk)
            showroom.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ShowroomList.DoesNotExist:
            return Response({'error': 'Showroom not found'}, status=404)

# def car_list_view(request):
#     cars = CarList.objects.all()
#     data = {
#         'cars': list(cars.values())
#     }
#     return JsonResponse(data)


# def car_detail_view(request, pk):
#     try:
#         car = CarList.objects.get(id=pk)
#         data = {
#             'car': car.name,
#             'description': car.description,
#             'active': car.active	
#         }
#         return JsonResponse(data)
#     except CarList.DoesNotExist:
#         return JsonResponse({'error': 'Car not found'}, status=404)

@api_view(['GET', 'POST'])
def car_list_view(request):
    if request.method == 'GET':
        cars = CarList.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def car_detail_view(request, pk):
    if request.method == 'GET':
        car = CarList.objects.get(pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        car = CarList.objects.get(pk=pk)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        car = CarList.objects.get(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 