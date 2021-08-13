from django.urls import path
from products.api.views.general_views import MeasureUnitListAPIView, IndicadorListAPIView ,CategoryProductListAPIView
from products.api.views.product_views import(
    ProductListCreateAPIView,ProductRetrieveUpdateDestroyAPIView, )


urlpatterns=[
    path('measure_unit/',MeasureUnitListAPIView.as_view(),name='measure_unit'),
    path('indicador/',IndicadorListAPIView.as_view(),name='indicador'),
    path('category_product/',CategoryProductListAPIView.as_view(),name='category_product'),
    path('product/',ProductListCreateAPIView.as_view(),name='product_create'),
    path('product/retrieve-update-destroy/<int:pk>',ProductRetrieveUpdateDestroyAPIView.as_view(),name='product_retrieve_update_destroy')

]
