from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from users.models import User
from users.api.serializers import UserSerializer, TestUserSerializer, UserListSerializer



@api_view(['GET','POST'])
def user_api_view(request):

    if request.method =='GET':
        users =User.objects.all().values('id','username','email','password','name')
        user_serializer=UserListSerializer(users, many=True) 
        return Response(user_serializer.data,status = status.HTTP_200_OK)
    elif request.method=='POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'Usuario creado correctamente'},status = status.HTTP_201_CREATED)
        return Response(user_serializer.errors)
        
        
@api_view(['GET','PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):
   # AQUI SE HACE LA CONSULTA
   user = User.objects.filter(id=pk).first()
   # AQUI SE HACE LA VALIDACION
   if user:
   
       # RETRIVE
       if request.method == 'GET':
       ##Aqui se pueden hacer validaciones
           user_serializer = UserSerializer(user)
           return Response(user_serializer.data,status = status.HTTP_200_OK)
       # UPDATE
       elif request.method == 'PUT':
           user_serializer = TestUserSerializer(user,data= request.data)
           if user_serializer.is_valid():
               user_serializer.save()
               return Response(user_serializer.data,status = status.HTTP_200_OK)
           return Response(user_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
       # DELETE    
       elif request.method == 'DELETE':
           user.delete()
           return Response({'message':'usuario Eliminado correctamente'},status = status.HTTP_200_OK)
   
   return Response({'message':'No se ha encontrado un usuario'},status = status.HTTP_400_BAD_REQUEST)
           
