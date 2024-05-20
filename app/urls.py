from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('authentication.urls')),    
    path('api/v1/', include('categoria.urls')),
    path('api/v1/', include('nivel0.urls')),
    path('api/v1/', include('nivel1.urls')),
    path('api/v1/', include('nivel2.urls')),
    path('api/v1/', include('nivel3.urls')),
    path('api/v1/', include('nivel4.urls')),
    path('api/v1/', include('nivel5.urls')),
]
