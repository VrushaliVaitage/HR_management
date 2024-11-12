from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hr.urls')),
    path('a1/', include('auth_app.urls')),
]
