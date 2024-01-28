from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from django.contrib.auth.models import User

# views.py




class RegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        user = serializer.save()
        user.first_name = serializer.validated_data.get('first_name', '')
        user.last_name = serializer.validated_data.get('last_name', '')
        user.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED, headers=headers)




from django.contrib.auth import authenticate,login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserLoginSerializer  
from rest_framework.authtoken.models import Token





class UserLoginApiView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=self.request.data)
        
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user:
                login(request, user)
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'error': "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': "Invalid Data"}, status=status.HTTP_400_BAD_REQUEST)




    
