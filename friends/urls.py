from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('allauth.urls')),
    path('users/', include(('accounts.urls','accounts'), namespace='users')),
]
