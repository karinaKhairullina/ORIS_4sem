from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import logout
from GoogleAuth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', views.login, name='login'),
    path('', include('social_django.urls', namespace='social')),
    path('test/', views.index, name='index')
]

