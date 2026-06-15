from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import (
SpectacularAPIView,
SpectacularSwaggerView,
)

from rest_framework_simplejwt.views import (
TokenObtainPairView,
TokenRefreshView,
)

urlpatterns = [
    path('', include('dashboard.urls')),


    path('admin/', admin.site.urls),

    path('api/auth/', include('accounts.urls')),
    path('api/categories/', include('categories.urls')),
    path('api/appeals/', include('appeals.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),


    path('', include('accounts.web_urls')),
    path('', include('appeals.web_urls')),
]

if settings.DEBUG:
    urlpatterns += static(
settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT
)
