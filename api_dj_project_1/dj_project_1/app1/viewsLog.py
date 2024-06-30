from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from rest_framework.decorators import api_view # decorador para poder decirle a la funciòn que protocolo de peticiòn debe recibir
from .serializers import UserSerializer # clase importada de la carpeta serializers de la app1
from rest_framework.authtoken.models import Token # para manejar los tokens generados 
from rest_framework import status # para poder dar mensajes de status

# para el profile valida auth, permisos y token
from rest_framework.decorators import authentication_classes, permission_classes # indica a una funciòn los permisos que debe verificar y la informaciòn que debe tener la rq
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication

from django.contrib.auth.models import User # ayuda a manejar informaciòn del usuario
from django.contrib.sessions.models import Session
from django.shortcuts import get_object_or_404 # ahorra còdigo en donde no coincide un username, devuelve error
from django.contrib.auth import authenticate, logout as logout_django

from datetime import datetime


# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance=user)
        
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)
    
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    serializer = UserSerializer(user)

    return Response({'message':f'You are already login {user}', 'user': serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    user = request.user
    token, created = Token.objects.get_or_create(user=user)
    
    if user:
        all_sessions = Session.objects.filter(expire_date__gte= datetime.now())
        if all_sessions.exists():
            for session in all_sessions:
                session_data = session.get_decoded()
                session_key = session_data.get('_auth_user_id')
                if int(session_key) == user.id:
                    session.delete()
        token.delete()

        session_message = 'You are now logged out of all sessions'
        token_message = 'token has been delete'
        return Response({'session_message': session_message, 'token_message': token_message}, status=status.HTTP_200_OK)
    
    else:
        return Response({'error': 'Token not found or invalid credencials'}, status=status.HTTP_400_BAD_REQUEST)
