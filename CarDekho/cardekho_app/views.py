from django.shortcuts import render
from .models import CarList, ShowroomList
from django.http import JsonResponse
from .api_file.serializers import CarSerializer, ShowroomListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


class ShowrowView(APIView):
    def get(self, request):
        showrooms = ShowroomList.objects.all()
        serializer = ShowroomListSerializer(showrooms, many=True)
        return Response(serializer.data)



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