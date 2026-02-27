from django.urls import path, include
from rest_framework import routers
from .views import LibroViewSet

router = routers.DefaultRouter()
router.register(r'libros', LibroViewSet, basename='libro')
urlpatterns = [
    path('api/', include(router.urls)),
]

