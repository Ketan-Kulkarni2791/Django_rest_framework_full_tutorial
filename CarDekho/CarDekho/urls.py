from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', include('cardekho_app.urls')),
    
    # For session authentication and to get the login option.
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('user-account/', include('user_app.api.urls')),
]
