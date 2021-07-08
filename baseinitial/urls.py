from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rest Framework Urls
    path('api-auth/', include('rest_framework.urls')),

    # JWT Urls
    path('api/v1/account/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/account/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/account/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # API Endpoints
    # path('api/v1/manage/', include('mymodule_api_routes')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)