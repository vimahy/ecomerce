from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from base.api import GeneralListApiView
from users.authentication_mixins import Authentication
from rest_framework.response import Response
from products.api.serializers.product_serializers import ProductSerializer


#AQUI SE DEFINE UN CRUD

class ProductViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class=ProductSerializer
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk,state=True).first()
            
    def create(self,request):
        serializer =self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'producto creado correctamente'}, status= status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            
    def delete(self,request):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state=False
            product.save()
            return Response({'message':'product eliminado correctamente'},status=status.HTTP_200_OK)
        return Response({'error':'No exisitio un producto con estos datos'},status=status.HTTP_400_BAD_REQUEST)
        
        
    def update(self,request):
        if self.get_queryset(pk):
            product_serializer =self.serializer_class(self.get_queryset(pk),data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status= status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        product_serializer=self.get_serializer(self.get_queryset(),many=True)
        return Response(product_serializer.data,status=status.HTTP_200_OK)
    
    
#CLASES GENERICAS DE DRF Y reeescribimos sus metodos
class ProductListAPIView(GeneralListApiView):
    serializer_class = ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.filter(state=True)
    #para interceptar una peticion POST
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Prodcuto creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#Esta clase una tres acciones updae, list, destroy
class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= ProductSerializer
    
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk,state=True).first()

    def patch(self,request,pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data,status=status.HTTP_200_OK)
        return Response({'error':'No exisitio un producto con estos datos'},status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk=None):
        if self.get_queryset(pk):
            product_serializer =self.serializer_class(self.get_queryset(pk),data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status= status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
                    




        
        

            
