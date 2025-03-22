from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('converter.urls')),  # 🔥 Now Angular can call /api/convert/
]
