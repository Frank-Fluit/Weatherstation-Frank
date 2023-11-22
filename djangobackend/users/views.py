from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserRegistrationSerializer
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


@permission_classes([AllowAny])
@csrf_exempt
@api_view(['POST'])
def user_registration_view(request):
    print(request.user)
    if request.method == 'POST':
        request.data['password'] = make_password(request.data.get('password'))

        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'detail': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)





