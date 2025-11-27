from rest_framework.routers import DefaultRouter
from library_app.api_views import BooksApiviews
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,)
from rest_framework.authtoken import views
router=DefaultRouter()
router.register('api',BooksApiviews)

urlpatterns = [
    path("",include(router.urls)),
    path('get-api-token/', views.obtain_auth_token,name='get-api-token'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
]