from products.models import MeasureUnit, CategoryProduct, Indicador

from rest_framewor import serializers


class MeasureUnitSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = MeasureUnit
        exlude=('state',)
	
	


class CategoryProductSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = CategoryProduct
        exlude=('state',)
        
class IndicadorSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = Indicador
        exlude=('state',)
