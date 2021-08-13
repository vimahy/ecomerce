from rest_framework import viewsets
from rest_framework.response import Response

from base.api import GeneralListApiView
from products.models import MeasureUnit
from products.api.serializers.general_serializers import MeasureUnitSerializer, IndicadorSerializer,CategoryProductSerializer

class MeasureUnitViewSet(viewsets.GenericViewSet):
    """
    Hola des de la unidad de medida
    """
    model= MeasureUnit
    serializer_class = MeasureUnitSerializer

    def get_queryset(self, request):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    
    def list(self, request):
        """
        Retorna las unidades de medida
        
        params.
        name: nombre de las unidades
        """

        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)
        
    def create(self, request):
        return Response({})

class IndicadorViewSet(viewsets.ViewSet):
    serializer_class = IndicadorSerializer
    def get_queryset(self, request):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    
    def list(self, request):
        """
        Retorna las unidades de medida
        
        params.
        name: nombre de las unidades
        """

        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        return Response(data.data)
        
    def create(self, request):
        return Response({})
    	
class CategoryProductViewSet(viewsets.ViewSet):
    serializer_class = CategoryProductSerializer
    

