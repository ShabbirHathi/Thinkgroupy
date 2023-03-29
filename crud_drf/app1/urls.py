from django.urls import path,include
from .views import *
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from app1 import views

router = DefaultRouter()
router.register(r'', views.DataViewSet, basename='product')
urlpatterns = router.urls



urlpatterns = [


    path('api/', include(router.urls)),
    path('api/create/',createview,name='create'),
    path('api/read/',readview,name='read'),
    path('api/update/<int:pk>/',updateview,name='update'),
    path('api/delete/<int:pk>/',deleteview,name='delete'),


    # path('swagger-ui/', TemplateView.as_view(
    #     template_name='swagger-ui.html',
    #     extra_context={'schema_url':'openapi-schema'}
    # ), name='swagger-ui'),
    # path('redoc/', TemplateView.as_view(
    #     template_name='redoc.html',
    #     extra_context={'schema_url':'openapi-schema'}
    # ), name='redoc'),
]