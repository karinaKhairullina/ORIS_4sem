from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions

schema_view = get_schema_view (
    openapi.Info(
        title='hw4_4sem',
        default_version='v1',
        description='HW 4 semestr 2, authorization + API documentation',
        contact=openapi.Contact(email='karihairullina@gmail.com')

    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hw/', include('jwt_auth.urls')),
    re_path(r'^swagger/$', schema_view.with_ui('swagger'))
]

