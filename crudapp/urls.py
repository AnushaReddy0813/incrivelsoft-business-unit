from django.urls import include, path
#from rest_framework import routers
from .views import *
# router = routersDefaultRouter()
# router.register(r'timestamp', TimeStampViewSet)
# router.register(r'business', BusinessViewSet)
# router.register(r'owner', OwnerDetailsViewSet)

urlpatterns = [
    path('api/create',BusinessCreateApi.as_view()),
    path('api',BusinessGetApi.as_view()),
    path('api/<int:pk>',BusinessUpdateApi.as_view()),
    path('api/<int:pk>/delete',BusinessDeleteApi.as_view()),
]

