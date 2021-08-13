from products.models import MeasureUnit, CategoryProduct, Indicador

from rest_framework import serializers


class MeasureUnitSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = MeasureUnit
        exclude=('state','modified_date','deleted_date')
	
	


class CategoryProductSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = CategoryProduct
        exlude=('state','created_date,','modified_date','deleted_date')
        
class IndicadorSerializer(serializers.ModelSerializer):
	
    class Meta:
        model = Indicador
        exlude=('state','created_date,','modified_date','deleted_date')
        
        

