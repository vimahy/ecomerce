from rest_framework.routers import DefaultRouter
from products.api.views.general_views import *
from products.api.views.product_viewsets import ProductViewSet


router = DefaultRouter()

router.register(r'products',ProductViewSet,basename='products')
router.register(r'measure-unit',MeasureUnitViewSet,basename='measure_unit')
router.register(r'indicadors',IndicadorViewSet,basename='indicadors')
router.register(r'category-products',CategoryProductViewSet,basename='category_products')

urlpatterns = router.urls
