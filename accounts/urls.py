# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegistrationViewSet,UserLoginApiView

router = DefaultRouter()
router.register('register', RegistrationViewSet,basename='registser')



urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginApiView.as_view(), name='login'),
   


]

    
