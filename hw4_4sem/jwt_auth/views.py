from .serializers import UserSerializer
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



@swagger_auto_schema(
    method='post',
    #запросы параметра
    manual_parameters=[
        openapi.Parameter('param', openapi.IN_QUERY, description='Параметр запроса', type=openapi.TYPE_STRING)
    ],
    #тело запроса
    request_body=UserSerializer,
    responses={
        201: openapi.Response('Created', UserSerializer),
        400: openapi.Response('Bad Request'),
    }
)
@api_view(['POST'])
def register(request):
    """
    Регистрация нового пользователя

    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# аутентификация пользователя
@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'user': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username user'),
                    'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password user')
                }
            )
        }
    )
)
@api_view(['POST'])
def login(request):
    """
    Аутентификация пользователя

    """
    username = ''
    password = ''
    user_data = request.data.get('user')
    if user_data:
        username = user_data.get('username')
        password = user_data.get('password')

    user = authenticate(username=username, password=password)
    if user:
        return Response({'token': user.token})
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)



















