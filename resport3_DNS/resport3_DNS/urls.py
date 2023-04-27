from django.urls import path, include

urlpatterns = [
    path('dns/', include('DNS.urls')),
]

