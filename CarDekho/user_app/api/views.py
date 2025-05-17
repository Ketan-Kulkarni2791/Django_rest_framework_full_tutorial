from rest_framework.decorators import api_view, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from user_app.api.serializers import RegisterSerializer


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
def logout_view(request):
    if request.method == 'POST':
        try:
            request.user.auth_token.delete()
            return Response({'status': 'User logged out successfully!'}, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=400)
    return Response({'error': 'Invalid request method.'}, status=405)


@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'User created successfully!'}, status=201)
        return Response(serializer.errors, status=400)
    return Response({'error': 'Invalid request method.'}, status=405)