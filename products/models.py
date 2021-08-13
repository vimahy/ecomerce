from django.db import models
from simple_history.models import HistoricalRecords
from base.models import BaseModel


class MeasureUnit(BaseModel):


    description = models.CharField('Description', max_length=50, blank=False,null=False,unique=True)
    historical = HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
        
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value
        
    
    class Meta:
    
    
        verbose_name ='Unidad de Medida'
        verbose_name_plural ='Unidades de Medidas'
        
        
    def __str__(self):
        return self.description
        
class CategoryProduct(BaseModel):

    description=models.CharField('Desciption',max_length=50,unique=True,null=False,blank=False)
    measure_unit = models.ForeignKey(MeasureUnit,on_delete=models.CASCADE,verbose_name='Unidad de Medida')
    historical=HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
        
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value
        
    
    class Meta:
    
        verbose_name ='Categoria de Producto'
        verbose_name_plural ='Categoria de Productos'
        
        
    def __str__(self):
        return self.description



class Indicador(BaseModel):


    descount_value=models.PositiveSmallIntegerField(default=0)
    category_product= models.ForeignKey(CategoryProduct, on_delete=models.CASCADE,verbose_name='Indicador de Oferta')
    historical= HistoricalRecords()
    
    
    @property
    def _history_user(self):
        return self.changed_by
        
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value
        
    
    class Meta:
    
        verbose_name ='Indicador de oferta'
        verbose_name_plural ='Indicador de ofertas'
        
        
    def __str__(self):
        return f'Oferta de la categoria {self.category_product} : {self.descount_value}%'



class Product(BaseModel):
    name=models.CharField('Nombre del Producto',max_length=150,unique=True,blank=False,null=False)
    description= models.TextField('Descripcion del producto',blank=False,null=False)
    image = models.ImageField('Imagen del producto', upload_to='products/',blank=True,null=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE,verbose_name='Unidda de Medida',null=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE,verbose_name='Categoria de Producto',null=True)
    historical=HistoricalRecords()
    
    
    
    @property
    def _history_user(self):
        return self.changed_by
        
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value
    def __str__(self):
    	return self.name
    
        
        
    
