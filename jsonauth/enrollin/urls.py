from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student') 

urlpatterns = [
    path('', include(router.urls)),  
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
 #for session authentication;
    # path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtain token
    # path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),     # Refresh token
    # path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),        # Verify token
]
