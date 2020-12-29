from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from api_app.views import UserViewSet, GroupViewSet, add_order
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api-token-auth/',views.obtain_auth_token,name='api-token-auth'),
    path('add_order/',add_order),
]
